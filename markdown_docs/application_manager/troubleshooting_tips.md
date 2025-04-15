# Technotes: Troubleshooting Tips

The following information provides assistance when working with the IoT OD Application Manager.

|Issue|Action|
|---|---|
|Adding an application fails.|* Check the file type and the format of the application package.<br>* Check that the latest IOx client release is used to package the application.<br>* Check if only one application is being uploaded at a time.<br>* Retry to check if it is a temporary issue.<br>* Ensure that the application package size is within the limits as specified in the application upload UI workflow.|
|Changing the version of an application fails.|* Ensure that the device has sufficient resources required for the new version.<br>* Check the current version and transitional status from the application instance page or the **Applications** tab in the **Device Details** page.<br>* Check if any errors are displayed in the application instance status field.<br>* Check the application logs for any initial errors if the new application version fails to launch.<br>* Download the tech support bundle and analyze the CAF logs for any issues during the application upgrade or startup. |
|The device is not present in the list of available devices on application installation screen.|Go to **Devices** > Select **Device Name**.<br>In the **Summary** tab, check the **IOx Status**. If it's down, click on **View Details** to check for more information, and also review the **Event Log**.|
|When the IOx status in the Device **Summary** page is down, and the following conditions are met:<br> * The device is up.<br>* You are able to execute "show iox" command using the **Troubleshooting** tab.<br>* The output of the command shows that IOx is running on the device<br>* You are able to trigger an IOx refresh and the **Last Heard Time** field is updated, but **Last Error on the device** field contains a value such as **connection refused**.<br> | This happens when IOx on the device is prevented from becoming fully functional due to an internal issue. To recover, disable IOx, clear the current state, and then restart IOx.<br> Try executing the following command on the device (these steps are not applicable for IR8x9 devices).<br>* no iox <br>* clear iox <br>* iox<br> Then, try an IOx refresh again from IoT OD GUI.
|The device appears in the list of available devices for installing applications, but the **Install Readiness Status** of the device is **Device Capabilities not yet discovered**, **Device unreachable** and the error message in the tool tip indicates Unauthorized or Too many failed login requests please try after some time.	|This happens due to a mismatch between the GOS (guest-os) image version and the IOS version and this mismatch happens when there is an error during firmware upgrade due to which the GOS does not get upgraded.<br>Use following commands to verify versions and contact Cisco support to confirm the issue:<br>* Show version<br>* Show platform hyper<br>* Show platform guest-OS<br>Upgrade to one of the latest firmware versions.|
|The device appears in the list of available devices for installing applications, but the **Install Readiness Status** of the device is **Device Capabilities not yet discovered**, **Device unreachable**.	|Check if the device and IoT OD are connected.<br>* If the device is an Externally-Managed device, see the section below for more troubleshooting steps.<br> Go to **Devices** > Select **Device Name** > **Summary**. Platform details will appear on the screen.<br>* Click **View Details** tab of the device details page to see if IOx is running successfully on the device and the status of IOx.<br>* Try using Refresh IOx.<br>* Resolve the issue mentioned in the **Last error on the device** field. Retry Refresh IOx.<br>* Check if IOx is running on the device using "show" commands related to IOx (exact commands will depend on the device type) from the device troubleshooting page.<br>* Try to download the **Tech support bundle** and analyze the CAF logs for any issues in the IOx startup.|
|A blank browser tab results from a client-side failure to download the tech support log bundle.|This happens when the size of the tech support log bundle is very large. The maximum size depends on the available RAM in your computer where the browser is running.<br>Refresh the page and close other applications to free up RAM and try again.|
|During the installation of an application, a device is highlighted in grey and marked as "Incompatible architecture."	|This happens when a device is not compatible with the CPU architecture for which the application was developed. For instance, the device supports CPU architecture aarch64, but the application is designed for CPU architecture x86_64.|
|During the installation of an application, a device is highlighted in grey and marked as "Device supports only Cisco-signed applications."|This happens when the application is not Cisco-signed and the device's IOx platform does not support such applications.|

## Troubleshooting of Externally Managed Devices

After following the IoT OD Service activation on an externally-managed IE3x00 device steps to onboard a device in IoT OD, the following INFO lines should appear in the **Event Log** tab of the device and its status should now appear as **UP**. 

![Troubleshooting](../graphics/app_mgr/am_ts_01.png)

The following information provides assistance when working with device onboarding issues (indicated in Event Logs).

|Issue|Action|
|---|---|
|IOx is not enabled|Enable IOx and verify if it is running correctly.|
|IOx is not configured correctly	|Configure AppGigabitEthernet1/1 in trunk mode with a unique native VLAN.|
|IOx is configured, but it still is not running correctly|Follow Cisco's recommendation and configure the trunk with an uncommon native VLAN. You can also choose to limit the allowed VLANs on this trunk to those needed for application and internet communication, though it's not mandatory. If you use a native VLAN number greater than 1004, ensure the switch is set to "vtp mode transparent" to allow VLAN creation. This setup allows applications to be deployed in any desired VLAN for better control of application traffic.|
|SD card is missing or not partitioned correctly for IOx usage|If the SD card is missing, insert an SD card. If the required IOx partition is not already set up in the SD card, format or partition the SD card accordingly.<br>**Note**: This process will delete all data on the card. Prior to formatting, remember to backup or transfer any necessary files/data from the SD card to the boot flash.|
|* Device is not **UP**<br>* The event log contains entries indicating authentication error or connection timeouts|Confirm that the admin username and password is identical to user credentials added to device IOS configuration.|
|* Device is not **UP**<br>* The event log contains entries indicating authentication error or connection timeouts|Confirm both "ip http server" and "ip http secure-server" are enabled in IOS.|
|* Device is not **UP**<br>* Device stays under the Staged tab|Check the call home URL in the web socket transport profile under the header: cgna transport-profile wst. Pay close attention to correct IoT OD cluster, PID, and serial number format as shown with no spaces.<br>* callhome-url: ws<span>s://</span>us.ciscoiot.com:443/wst/cgna/IE-3400-8P2S+FOCXXXXVXXX |
|* Device is not **UP**<br>* Device stays under the Staged tab| Check the URL registration profile to make sure it is using the correct IoT OD cluster and no typos under the header: cgna profile cg-nms-register. For example, url ht<span>tps://us.ciscoiot.com/cgna/ios/</span>registration|
|* Device is not **UP**<br>* Device stays under the Staged tab| Confirm device has functioning DNS service by pinging a public IP by name:<br>* ping cisco.com<br>&nbsp;&nbsp;&nbsp;Sending 5, 100-byte ICMP Echos to 72.163.4.161, timeout is 2 seconds:<br>&nbsp;&nbsp;&nbsp;!!!!!|
|* Device is not **UP**<br>* Device stays under the Staged tab| A web socket might be established between the device and IoT OD, but the device is still not registering. Confirm the web socket connection state is "connected" using this command:<br>* show ida transport -profile-state all \| inc IDA Status<br>&nbsp;&nbsp;&nbsp;**IDA Status: Connected**|
|* Device is not **UP**<br>* Device stays under the Staged tab|If web socket connection is not established, this low-level show command will display liveness messages between the device and IoT OD. There should be continuous ping/pong messages as follows:<br>* show logging process ida internal reverse<br>&nbsp;&nbsp;&nbsp;* 2023/05/24 18:40:29.453267143 {ida_ws_R0-0}{1}: [ida_ws] [6785]: (note): DATA: Sent PING Packet - pong Debt 1<br>&nbsp;&nbsp;&nbsp;* 2023/05/24 18:39:39.495901643 {ida_ws_R0-0}{1}: [ida_ws] [6785]: (ERR): LWS Callback:: REASON: 9 - CLIENT_RECEIVE_PONG |



<!--## Cisco IOS XE Software Web UI Privilege Escalation Vulnerability [CVE-2023-20198] -->
<h2><a name="TechNote"></a>Cisco IOS XE Software Web UI Privilege Escalation Vulnerability [CVE-2023-20198]</h2>

Cisco is providing an update for the ongoing investigation into observed exploitation of the web UI feature in Cisco IOS XE Software. IOS-XE routers and switches that are directly exposed to the internet, or an untrusted network such as a public access network, and have their HTTP or HTTPS server access enabled may be exposed to [Cisco IOS XE Software Web UI Privilege Escalation Vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z).

### Am I vulnerable? 
The  "ip http server" and "ip http secure-server" configuration lines that enable a web server on the device can be accessed externally using ports TCP 80 and TCP 443, which maybe be vulnerable to an attack. If the device is exposed to the internet or an untrusted network, and without enterprise firewall protection, it is important to control access to this web service and prevent potential security risks. See (https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software/).
One way to check is to try and access ports 80 and 443 on your device. For example, you can use "telnet <ip_address> 80" and "telnet <ip_address> 443" and check if the port is open. 

For a wider and more automated verification, tools such as nmap can be used to scan a complete network. For example:

 <pre>nmap -sT --open -p 80,443 192.168.2.0/24</pre>
 
Irrespective of any security vulnerability, the recommendation is to never leave unnecessary ports open and in particular on an untrusted network, and to always place devices behind an enterprise-grade firewall and be able to perform stateful traffic inspection.

If adding an enterprise firewall is not possible, exposed ports can be eliminated with access control lists (ACLs) configured and applied on either the Web server directly (see option 1 below), or the interface(s) pointing to the untrusted network (see option 2 below).

Modify the lists to accommodate different access modes that are required.  For example, if you need access to the device's local web server or if DNAC requires access, you can include the IPs or subnet used for access in the allowed list, and deny access to all others.

### Two ways of protection
#### Option 1: Filter Cisco IOS XE WebUI Using an Access List
Refer to the Cisco article that explains how to filter traffic going to the embedded HTTP and HTTPS server on the IOS-XE device: https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-17/221107-filter-traffic-destined-to-cisco-ios-xe.html

#### Option 2. Filter all traffic to Cisco IOS XE WebUI from untrusted network interfaces
In the following example for ACL creation, line 10 and other subsequent permit statements are used to allow access to port 443 from local enterprise IP/subnets.  For example, the client from IP address 10.10.10.10 will be allowed HTTPS access to the device webserver. Lines 15 and 16 deny such access to ports 443 and port 80 to anyone else. Line 20 permits all other IP access for normal operation.

<pre>ip access-list extended NO-HTTP-S
  10 permit tcp 10.10.10.10 0.0.0.0 any eq 443
  15 deny tcp any any eq 443
  16 deny tcp any any eq 80
  20 permit ip any any 
  </pre>
  
Apply the above access list on the interface that is used to access internet (in the below example, it is assumed that GigabitEthernet1/1  is used for internet access).

<pre>interface GigabitEthernet1/3
 ip access-group NO-HTTP-S in
 </pre>

