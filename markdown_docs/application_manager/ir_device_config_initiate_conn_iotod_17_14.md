# IR Device Configuration and Initiating Connection to OD (17.14.1)

## Configuring devices managed by CLI/Local Manager 

>**IMPORTANT**: When you manage an IR device, ensure that the configuration necessary for the DNS resolution of the IoT OD URL is set in the CLI. You can use either the IP name server or the static IP host config. This feature will not operate without proper DNS resolution. Execute the required CLI command to configure the IoT OD **Services** on the IR device.

### Prerequisite

* Ensure that the router has a minimum version of IOS XE 17.14.1 installed.
* Add a single externally-managed device in IoT OD Application Manager using the UI. For details see section, <a href="https://developer.cisco.com/docs/iotod/onboarding-externally-managed-ir-devices/#AddingSingleDevice">**To add a single externally managed device**</a>.

### Steps
**A. Prepare the device.**
   1. Attach the required networking cables.
   2. Power up the device.

**B. Configure and enable IOx.**

   IOx is a container hosting platform that runs on Cisco IOS XE, and it is used to install and execute a number of services that Cisco IoT Operations Dashboard can deliver such as Edge Intelligence (EI), Secure Equipment Access (SEA) or third party applications packaged as IOx Apps. As a first step, we will now configure and enable IOx.
   1. Configure DHCP Pool, VPG Interface and NAT Rules on the device for IOx Network.
   
      1. The virtual interface that connects IOx Apps to IOS XE is called VirtualPortGroup0. These Apps will need IP connectivity through that interface, which includes receiving an IP address. Provide that interface and IP address. Below is an example, but feel free to change the IP address to suit your requirements. These configuration commands will need to be entered on the router console, in the config mode.
        <pre>
        ! Example
        conf t    
        interface VirtualPortGroup0
        description IOx Interface
        ip address 192.168.16.1 255.255.255.0
        ip nat inside
        ipv6 enable
        end
        </pre>

      2. When the IOx Apps start, they will request an IP address via DHCP. Therefore, it is necessary to configure a DHCP pool for IOx Apps. Below is an example of IP pool and DNS server but these can be customized for your own requirements. Ensure that the default-router IP address must be the IP address previously configured for the VirtualPortGroup0 interface.
        <pre>
        ! Example
        conf t
        ip dhcp pool ioxpool
        network 192.168.16.0 255.255.255.0
        default-router 192.168.16.1
        dns-server 192.168.16.1 8.8.8.8 
        end
        </pre>

      3. Since the IOx Apps will use private IP addresses obtained from the DHCP, they require Network Address Translation (NAT) to access the internet. Add NAT Rules for the DHCP pool to enable IOx App traffic to access the internet.

         In the example below, we assume that the connection to the internet will be through Cellular 0/1/0. Make sure to change/adjust the interface if it is not Cellular 0/1/0. For example, it could be GigabitEthernet 0/0/0 or Cellular 0/3/0.
        <pre>
        ! Example of a NAT rule for using Cellular0/1/0 as an uplink:
        conf       
        interface Cellular0/1/0
        ip nat outside
        ip access-list extended NAT_ACL
        10 permit ip 192.168.16.0 0.0.0.255 any
        route-map RM_WAN_ACL2 permit 10
        match ip address NAT_ACL
        match interface Cellular0/1/0
        ip nat inside source route-map RM_WAN_ACL2 interface Cellular0/1/0 overload
        end
        </pre>
        
   2. Enable IOx.
      
      <pre>
      conf t
      iox
      end
      </pre>
      
   3. Verify that IOx is running correctly by executing this command in exec mode:
      
      <pre>
      show iox-service
      ! Example 1: When IOx is up and running, both the “IOx service (CAF)” and “dockerd” will be running.
      Router#sh iox-service
      IOx Infrastructure Summary:
      ---------------------------
      IOx service (CAF)         : Running
      IOx service (HA)          : Not Supported
      IOx service (IOxman)      : Running
      IOx service (Sec storage) : Running
      Libvirtd 5.5.0            : Running
      Dockerd v19.03.13-ce      : Running
      </pre>
      
**C. Configure the IR device to connect to IoT OD.**

   1. We are now going to execute a set of IOS commands on the device's CLI to establish a connection to the IoT OD.
      The [Device Profile](/application_manager/device_profiles.md) in the IoT Operations Dashboard is associated with devices such as routers, with a set of username / password for managing them. To manage the IOx Apps, the Cisco IoT Operations Dashboard requires valid level 15 user credentials in IOS XE. If such a user is currently not present on the device, the following configuration should be applied to create a privilege 15 user.

      The credentials should match the values configured in the Device Profile in the Cisco IoT Operations Dashboard:
      <pre>
      conf t
      username &lt;DEVICE PROFILE USERNAME&gt; privilege 15 algorithm-type scrypt secret &lt;DEVICE PROFILE PASSWORD&gt;
      end
      </pre>
   2. Configure the authentication-related settings and WSMA settings.

      >**IMPORTANT**: Usage of the WSMA service relies on http, therefore "ip http server" is required to be enabled in the configuration. To deploy applications securely, add “ip http secure-server” as well.

      >**Note**: Please review running-config on the device first. Some related configurations might be available out of the box.
      
      <pre>
      conf t 
      aaa new-model
      aaa authentication login default local
      aaa authorization exec default local
      ip http server
      ip http authentication local
      ip http secure-server
      wsma agent exec
      profile exec
      wsma profile listener exec
      transport http path /wsma/exec
      cgna gzip
      end
      </pre>
      
   3. Configure the IDA transport profile for your Cisco IoT Operations Dashboard cluster (EU or US). This configuration will enable a secure TLS connection using WebSocket to Cisco IoT Operations Dashboard and will initiate an outgoing connecting to the cluster using TLS with port TCP 443. This connection is used as a transport for the rest of the Cisco IoT Operations Dashboard functions and APIs. 
      
      <pre>
      ! For US Cluster:
      conf t     
      ida transport-profile wst
      callhome-url wss://device-us.ciscoiot.com/wst/cgna
      execution-url http://192.168.16.1
      active
      end
      ! For EU Cluster:
      conf t
      ida transport-profile wst
      callhome-url wss://device-eu.ciscoiot.com/wst/cgna
      execution-url http://192.168.16.1
      active
      end
      </pre>
      
   4. Now that we have configured a secure connection, we need to configure the CGNA registration profile. This will initiate a router registration to the Cisco IoT Operations Dashboard cloud, leveraging the previously configured transport profile.
      
      <pre>
      conf t
      cgna profile cg-nms-register
      transport-profile wst
      add-command show version | format flash:/managed/odm/cg-nms.odm
      add-command show inventory | format flash:/managed/odm/cg-nms.odm
      interval 3
      active
      url https://localhost/cgna/ios/registration
      gzip
      end
      </pre>
      
      Once the configuration is completed, the device will establish a connection with the IoT OD and initiate the onboarding process.
      
   5. (Optional) Enable DNS on the router, if it is not already acquired through DHCP server.
      >**Note**: This is important if the router is configured with static IP and the static default gateway and not explicitly given a DNS server to use. In this example, we use a Cisco DNS. Use any DNS server.
      
      <pre>
      conf t
      ip name-server 208.67.222.222
      end
      </pre>
      
**D. Verify the configuration on the device.**

   Use the following commands to verify that the device is configured correctly  to connect to IoT OD.
   
   * Show ida transport-profile-state all
      <pre>
      ! Verify that IDA status is connected for the "wst" transport profile
      ! Notice the line "IDA Status: Connected" in the show command output below for the "wst" transport profile. 
      Router#sh ida transport-profile-state all
      Transport Profile 1:
      Profile Name: wst
      Activated at: Fri Jun  7 07:26:42 2024
      Reconnect Interval: 30 seconds
      keepalive timer Interval: 50 seconds
      Source interface: [not configured]
      callhome-url: wss://device-us.ciscoiot.com/wst/cgna
      Local TrustPoint: CISCO_IDEVID_SUDI
      Remote TrustPoint: [not configured]
      Execution-url: http://192.168.16.1  
      Proxy-Addr: [not configured]
      IDA Status: Connected
      State: Wait for activation
      Last successful response at Fri Jun  7 08:25:29 2024
      Last failed response:
      Last failed reason:
      </pre>
   * Show cgna profile name cg-nms-register 
      <pre>
      ! This is an example output for the above command
      ! That is the expected state after successful registration
      Router# sh cgna profile-state all
      Profile 1:
      Profile Name: cg-nms-register
      Activated at: Tue Mar 12 10:14:03 2024
      URL: https://localhost/cgna/ios/registration
      Transport-profile: wst
      Payload content type: xml
      Interval: 3 minutes
      Transfer count: 95
      gzip: activated
      Profile command:
      show version | format flash:/managed/odm/cg-nms.odm
      show inventory | format flash:/managed/odm/cg-nms.odm
      State: Wait for timer for next action
      Timer started at Tue Mar 12 14:59:30 2024
      Next update will be sent in 1 minute 18 seconds
      Last successful response not found
      Last failed response not found
      </pre>
      
**E. Using proxy server to connect to IoT OD.**

   If you are required to use proxy server to connect to IoT OD, apply the following proxy-addr CLI in your IDA config.
   Replace the ```ipv4:port``` with your proxy server’s IP address and port number.
   
   <pre>
   ! For US Cluster:
   conf t 
   ida transport-profile wst
   callhome-url wss://device-us.ciscoiot.com/wst/cgna
   proxy-addr &lt;ipv4:port&gt;
   active
   end
   ! For EU Cluster:
   conf t
   ida transport-profile wst
   callhome-url wss://device-eu.ciscoiot.com/wst/cgna
   proxy-addr &lt;ipv4:port&gt;
   active
   end
   </pre>

**F. Verifying the Device Status in the IoT OD.**

 After successful registration on IoT OD, the IR device will be automatically moved from **Devices** > **Staged** tab to **Registered** tab in your IoT OD Organization.<br>
 
  {%note info %}
   **Note**:
   1. The IR device will move to **Devices** > **Registered** with **Up** status if the device registration is finished successfully.
   2. If IoT OD received a registration attempt but had some issues, (e.g., incorrect credentials), the IR device will move to **Devices** > **Staged** with **Config Failure** status.
   3. If IoT OD didn't receive any registration attempt, the IR device will stay in the **Devices** > **Staged** list.
   {%endnote%}






