# IR Device Configuration and Initiating Connection to OD (17.13.1)

## Configuring devices managed by CLI/Local Manager 

>**IMPORTANT**: When you manage an IR device, ensure that the configuration necessary for the DNS resolution of the IoT OD URL is set in the CLI. You can use either the IP name server or the static IP host config. This feature will not operate without proper DNS resolution. Execute the required CLI command to configure the IoT OD **Services** on the IR device.

### Prerequisite

* Ensure that the router has a minimum version of IOS XE 17.13.1 installed.
* Add a single externally-managed device in IoT OD Application Manager using the UI. For details see section, <a href="https://developer.cisco.com/docs/iotod/onboarding-externally-managed-ir-devices/#AddingSingleDevice">**To add a single externally managed device**</a>.

### Steps
**A. Prepare the device.**
   1. Attach the required networking cables.
   2. Power up the device.

**B. Configure and enable IOx:**
   IOx is a container hosting platform that runs on Cisco IOS XE, and it is used to install and execute a number of services that Cisco IoT Operations Dashboard can deliver such as Edge Intelligence (EI), Secure Equipment Access (SEA) or third party applications packaged as IOx Apps. As a first step, we will now configure and enable IOx.
   
   1. Configure DHCP Pool, VPG Interface and NAT Rules on the device for IOx Network.
   
       1. The virtual interface that connects IOx Apps to IOS XE is called VirtualPortGroup0. These Apps will require an IP address to connect through this interface. Please set up this interface and assign an IP address. Below is an example, but feel free to change the IP address to suit your requirements. You will need to enter these configuration commands in config mode on the router console.
        
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

         In the example below, we assume that the connection to the internet will be through Cellular 0/3/0. Make sure to change/adjust the interface if it is not Cellular 0/3/0. For example, it could be GigabitEthernet 0/0/0 or Cellular 0/1/0.
         
         <pre>
         ! Example of a NAT rule for using Cellular0/3/0 as an uplink:
         conf t
        
         interface Cellular0/3/0
          ip nat outside
        
         ip access-list extended NAT_ACL
          10 permit ip 192.168.16.0 0.0.0.255 any
                 
         route-map RM_WAN_ACL2 permit 10
          match ip address NAT_ACL
          match interface Cellular0/3/0
        
         ip nat inside source route-map RM_WAN_ACL2 interface Cellular0/3/0 overload
         end
         </pre>
   2. Enable IOx.
      <pre>
      conf t
      iox
      end
      </pre>

   3. Verify that IOx is running correctly.
      <pre>
      show iox-service
        
      Example : IOx is up and running
        
      Router#sh iox-service
        
      IOx Infrastructure Summary:
      IOx service (CAF)              : Running
      IOx service (HA)               : Not Supported
      IOx service (IOxman)           : Running
      IOx service (Sec storage)      : Running
      Libvirtd 5.5.0                 : Running
      Dockerd v19.03.13-ce           : Running    
      </pre>

**C. Configure the IR device to connect to IoT OD.**
   1. We are now going to execute a set of IOS commands on the device's CLI to establish a connection to the IoT OD.
      The [Device Profile](/application_manager/device_profiles.md) in the IoT Operations Dashboard is associated with devices such as routers, with a set of username / password for managing them. To manage the IOx Apps, the Cisco IoT Operations Dashboard requires valid level 15 user credentials in IOS XE. If such a user is currently not present on the device, the following configuration should be applied to create a privilege 15 user.
      <pre>
      conf t
      username &lt;DEVICE PROFILE USERNAME&gt; privilege 15 algorithm-type scrypt secret &lt;DEVICE PROFILE PASSWORD&gt;
      end</pre>
   2. Configure the authentication-related settings and WSMA settings. 
        >**IMPORTANT**: Usage of the WSMA service relies on http, therefore "ip http server" is required to be enabled in the configuration. To deploy applications securely, add “ip http secure-server” as well.

        >**Note**: Please review running-config on the device first. Some related configurations might be available out of the box.
        
        <pre>
        conf t
        aaa new-model
        aaa authentication login default local
        aaa authorization exec default local
        
        ip http secure-server
        ip http server
        ip http authentication local
        
        wsma agent exec
        profile exec
        wsma profile listener exec
        transport http path /wsma/exec
        
        cgna gzip
        end
        </pre>
   3. This step is applicable for IR1101 devices only. You must enter IoT OD certificate manually on the IR1101 devices.
        <pre>
        conf t
        crypto pki trustpoint iotod-cert
          revocation-check none
        crypto pki certificate chain iotod-cert
         certificate ca 7D5B5126B476BA11DB74160BBC530DA7
         30820613 308203FB A0030201 0202107D 5B5126B4 76BA11DB 74160BBC 530DA730 
         0D06092A 864886F7 0D01010C 05003081 88310B30 09060355 04061302 55533113 
         30110603 55040813 0A4E6577 204A6572 73657931 14301206 03550407 130B4A65 
         72736579 20436974 79311E30 1C060355 040A1315 54686520 55534552 54525553 
         54204E65 74776F72 6B312E30 2C060355 04031325 55534552 54727573 74205253 
         41204365 72746966 69636174 696F6E20 41757468 6F726974 79301E17 0D313831 
         31303230 30303030 305A170D 33303132 33313233 35393539 5A30818F 310B3009 
         06035504 06130247 42311B30 19060355 04081312 47726561 74657220 4D616E63 
         68657374 65723110 300E0603 55040713 0753616C 666F7264 31183016 06035504 
         0A130F53 65637469 676F204C 696D6974 65643137 30350603 55040313 2E536563 
         7469676F 20525341 20446F6D 61696E20 56616C69 64617469 6F6E2053 65637572 
         65205365 72766572 20434130 82012230 0D06092A 864886F7 0D010101 05000382 
         010F0030 82010A02 82010100 D67333D6 D73C20D0 00D21745 B8D63E07 A23FC741 
         EE3230C9 B06CFDF4 9FCB1298 0F2D3F8D 4D010C82 0F177F62 2EE9B848 79FB1683 
         4EADD732 2593B707 BFB9503F A94CC340 2AE939FF D981CA1F 163241DA 8026B923 
         7A87201E E3FF209A 3C95446F 87750690 40B43293 16091008 233ED2DD 870F6F5D 
         51146A0A 69C54F01 7269CFD3 934C6D04 A0A31B82 7EB19AB9 EDC59EC5 37789F9A 
         0834FB56 2E58C409 0E06645B BC37DCF1 9F2868A8 56B092A3 5C9FBB88 98081B24 
         1DAB3085 AEAFB02E 9E7A9DC1 C0421CE2 02F0EAE0 4AD2EF90 0EB4C140 16F06F85 
         424A64F7 A430A0FE BF2EA327 5A8E8B58 B8ADC319 178463ED 6F56FD83 CB6034C4 
         74BEE69D DBE1E4E5 CA0C5F15 02030100 01A38201 6E308201 6A301F06 03551D23 
         04183016 80145379 BF5AAA2B 4ACF5480 E1D89BC0 9DF2B203 66CB301D 0603551D 
         0E041604 148D8C5E C454AD8A E177E99B F99B05E1 B8018D61 E1300E06 03551D0F 
         0101FF04 04030201 86301206 03551D13 0101FF04 08300601 01FF0201 00301D06 
         03551D25 04163014 06082B06 01050507 03010608 2B060105 05070302 301B0603 
         551D2004 14301230 06060455 1D200030 08060667 810C0102 01305006 03551D1F 
         04493047 3045A043 A041863F 68747470 3A2F2F63 726C2E75 73657274 72757374 
         2E636F6D 2F555345 52547275 73745253 41436572 74696669 63617469 6F6E4175 
         74686F72 6974792E 63726C30 7606082B 06010505 07010104 6A306830 3F06082B 
         06010505 07300286 33687474 703A2F2F 6372742E 75736572 74727573 742E636F 
         6D2F5553 45525472 75737452 53414164 64547275 73744341 2E637274 30250608 
         2B060105 05073001 86196874 74703A2F 2F6F6373 702E7573 65727472 7573742E 
         636F6D30 0D06092A 864886F7 0D01010C 05000382 02010032 BF61BD0E 48C34FC7 
         BA474DF8 9C781901 DC131D80 6FFCC370 B4529A31 339A5752 FB319E6B A4EF54AA 
         898D4017 68F81110 7CD2CAB1 F15586C7 EEB33691 86F63951 BF46BF0F A0BAB4F7 
         7E49C42A 36179EE4 68397AAF 944E566F B27B3BBF 0A86BDCD C5771C03 B838B1A2 
         1F5F7EDB 8ADC4648 B6680ACF B2B5B4E2 34E467A9 3866095E D2B8FC9D 283A1740 
         27C2724E 29FD213C 7CCF13FB 962CC531 44FD13ED D59BA969 68777CEE E1FFA4F9 
         36380853 39A28434 9C19F3BE 0EACD524 37EB23A8 78D0D3E7 EF924764 623922EF 
         C6F711BE 2285C666 4424268E 10328DC8 93AE079E 833E2FD9 F9F5468E 63BEC1E6 
         B4DCA6CD 21A8860A 95D92E85 261AFDFC B1B65742 6D95D133 F6391406 824138F5 
         8F58DC80 5BA4D57D 9578FDA7 9BFFFDC5 A869AB26 E7A7A405 875BA9B7 B8A3200B 
         97A94585 DDB38BE5 89378E29 0DFC0617 F638400E 42E41206 FB7BF3C6 116862DF 
         E398F413 D8154F8B B169D910 60BC642A EA31B7E4 B5A33A14 9B26E30B 7BFD028E 
         B699C138 975936F6 A874A286 B65EEBC6 64EACFA0 A3F96E9E BA2D11B6 86980858 
         2DC9AC25 64F25E75 B438C1AE 7F5A4683 EA51CAB6 F1991135 6BA56A7B C600B0E7 
         F8BE64B2 ADC8C2F1 ACE351EA A493E079 C8E18140 C90A5BE1 123CC160 2AE397C0 
         8942CA94 CF469812 69BB98D0 C2D30D72 4B476EE5 93C43228 638743E4 B0323E0A 
         D34BBF23 9B142941 2B9A041F 932DF1C7 39483CAD 5A127F
        quit 
        end
       </pre>
        
   4. Configure the IDA transport profile for your Cisco IoT Operations Dashboard cluster (EU or US). This configuration will enable a secure TLS connection using WebSocket to Cisco IoT Operations Dashboard and will initiate an outgoing connection to the cluster using TLS with port TCP 443. This connection is used as a transport for the rest of the Cisco IoT Operations Dashboard functions and APIs. 
       * Configure IDA with the virtualportgroup 0 interface IP as the execution URL. 
        <pre>
        ! For US Cluster:
        conf t
        ida transport-profile wst
        callhome-url wss://device-us.ciscoiot.com/wst/cgna
        execution-url http://192.168.16.1  <!--add &lt and &gt to show the angular brackets in the url--->
        remote-trustpoint iotod-cert
        active
        end
        </pre>
        <pre>
        ! For EU Cluster::
        conf t
        ida transport-profile wst
        callhome-url wss://device-eu.ciscoiot.com/wst/cgna
        execution-url http://192.168.16.1  <!--add &lt and &gt to show the angular brackets in the url--->
        remote-trustpoint iotod-cert
        active
        end
        </pre>
         
   5. Now that we have configured a secure connection, we need to configure the CGNA registration profile. This will initiate a router registration to the Cisco IoT Operations Dashboard cloud, leveraging the previously configured transport profile.<br> 
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
       Once the configuration is done, the device will connect to IoT OD and trigger the onboarding process.<br>
   6. (Optional) Enable DNS on the router, if it is not already acquired through DHCP server.
      >**Note**: This is important if the router is configured with static IP and the static default gateway and not explicitly given a DNS server to use. In this example, we use a Cisco DNS. Use any DNS server.
        <pre>
        conf t
        ip name-server 208.67.222.222
        end
        </pre>
        
**D. Verify the configuration:**
    Use the following commands to verify if the device is configured correctly inorder to connect to IoT OD.<br>

   * Show ida transport-profile name wst
     
     
     <pre>
        ! This is an example output for the above command
        ! Verify that IDA status is connected
        ! Notice the line "IDA Status: Connected" in the show command out below.  Router#sh ida transport-profile-state all
        Transport Profile 1:
        Profile Name: wst
        Activated at: Wed Dec 13 02:11:55 2023
        Reconnect Interval: 30 seconds
        keepalive timer Interval: 50 seconds
        Source interface: [not configured]
        callhome-url: wss://device-us.ciscoiot.com:443/wst/cgna/IR1831-K9+FCW2522P2R3
        Local TrustPoint: CISCO_IDEVID_SUDI
        Remote TrustPoint: iotod-cert
        Execution-url: http://192.168.16.1
        Proxy-Addr: [not configured]
        IDA Status: Connected
        State: Wait for activation
        Last successful response at Wed Dec 13 02:14:25 2023
        Last failed response at Wed Dec 13 02:13:25 2023
        Last failed reason: Closed before conn
        </pre>
      
   * Show cgna profile name cg-nms-register
      
      
        
        <pre>
        ! This is an example output for the above command
        ! That is the expected state after successful registration 
        Router# sh cgna profile-state all
        Profile 1:
        Profile Name: cg-nms-register
        Activated at: Wed Dec 13 01:05:07 2023
        URL: https://device-us.ciscoiot.com/cgna/ios/registration
        Transport-profile: wst
        Payload content type: xml
        Interval: 3 minutes
        Transfer count: 7
        gzip: deactivated
        Profile command:
        show version | format flash:/managed/odm/cg-nms.odm
        show inventory | format flash:/managed/odm/cg-nms.odm
        State: Wait for timer for next action
        Timer started at Wed Dec 13 01:26:36 2023
        Next update will be sent in 1 minute 55 seconds
        Last successful response not found
        Last failed response not found
        </pre>
        
        
 **E. Verifying the Device Status in the IoT OD.**
 
 After successful registration on IoT OD, the IR device will be automatically moved from **Devices** > **Staged** tab to **Registered** tab in your IoT OD Organization.<br>
 
  {%note info %}
   **Note**:
   1. The IR device will move to **Devices** > **Registered** with **Up** status if the device registration is finished successfully.
   2. If IoT OD received a registration attempt but had some issues, (e.g., incorrect credentials), the IR device will move to **Devices** > **Staged** with **Config Failure** status.
   3. If IoT OD didn't receive any registration attempt, the IR device will stay in the **Devices** > **Staged** list.
   {%endnote%}



























