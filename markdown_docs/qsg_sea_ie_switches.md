# Quick Start Guide for Cisco SEA on IE switches

## Introduction
This document describes how, using Secure Equipment Access (SEA), to onboard an IE switch as an "externally managed device" on the Cisco Internet of Things Operations Dashboard (IoT OD).

## Before you begin

* You must have an administrator role to the IoT OD organization.
* The IE switch is functioning running at least IOS-XE 17.12.1 and has internet access.

## Add a switch of Cisco IoT OD

1. In Cisco IoT Operations Dashboard, navigate to **Application Manager** service.
2. Create a **Device Profile** by choosing **Devices** > **Staged** > **Add Devices**

![App Mgr Add Device](../graphics/app_mgr/App_Mgr_Add_Device_00.png)

3. Choose **Single Device**.

![Single Device](../graphics/app_mgr/IE_QSG_00a_single_device.png)

4. Enter a **Name**, **Product PID** (for example: IE-3400-8T2S), and **Product SN** (for example: FEC2990VZFU). They are located on the box (device?), or by using the CLI command: **show license udi**. 

![Add Device 1](../graphics/app_mgr/SEA_IE_QSG_01_add_device.png)

**Note**:  To use Latitude and Longitude for device tracking, select **I want to add my device using the Latitude, Longitude** option.

5. Click **Next**.
6. In the **Select Device Profile for Assignment** screen,choose a **Device Profile** for the Device. Click **Next**.

**Note**: If a Device Profile does not exist for the Device you are adding, you can create a new **Device Profile** by clicking the Device Profile link on the screen. If a Device Profile exists for the Device, complete step 6. Click **Next**.

![Add Device 2](../graphics/app_mgr/SEA_IE_QSG_02_assign_device_profile.png)

7. Review the **Configuration** information on the **Review** screen. 

![Add Device 3](../graphics/app_mgr/SEA_IE_QSG_03_review.png)

8. At this stage, you must format the **SD card** for the switch. 

## Format an SD CARD for the switch

To correctly function, the SD CARD is required to be in ext4 format for IOx. In enabled mode, format the SD CARD with this command:

`format sdflash: ext4`

## Configure the switch for IoT Operations Dashboard

<pre>
username <username> privilege 15 password 0 <password>`
aaa new-model
aaa authentication login default local
aaa authorization exec default local
</pre>

### Configure the IoT Operations Dashboard cluster

The cluster is in the URL where n the device was added to IoT OD
* For EU Cluster:<br>
    `event manager enviornments _cluster [eu.ciscoiot.com](http://eu.ciscoiot.com)`<br>
        
* For US Cluster:<br>
    `event manager environment _cluster [us.ciscoiot.com](http://us.ciscoiot.com)`<br>
    
### Configure IOx

The following configuration enables IOx to run on SEA.

>**Note**: The IOx interface (AppGigabilEthernet 1/1) is located in Vlan 4096 to make sure it does not conflict with any other Vlan running on the switch. The SEA Agent installed on the switch requires internet access, and, you  can configure that Vlan in this port instead of 4094.

 <pre>
 vtp mode transparent
 vlan 4094
   name app-man-native-vlan
  interface AppGigabitEthernet1/1
   switchport trunk native vlan 4094
   switchport mode trunk
iox
</pre>

 ### Configure the communication channel with IoT Operations Dashboard

 The following commands configure WebSocket communication between this switch and IoT OD and the EEM script automatically populates the cluster, serial number, and PID.
 <pre>
 event manager applet configstart
 event timer countdown time 1
 action 1.0 cli command "enable"
 action 1.1 cli command "show license udi"
 action 1.2 regexp "PID:(.*),SN:(.*)" "$_cli_result" _match _pid _serial
 action 1.3 puts "Configuring websocket for device $_match"
 action 2.0 cli command "conf t"
 action 2.1 cli command "ida transport-profile wst"
 action 2.2 cli command "callhome-url wss://$_cluster:443/wst/cgna/$_pid+$_serial"
 action 2.3 cli command "active"
 action 3.0 cli command "cgna profile cg-nms-register"
 action 3.1 cli command " url https://$_cluster/cgna/ios/registration"
 action 4.0 cli command "no event manager applet configstart"
 exit  
 </pre>
 
 <pre>
 wsma agent exec
    profile exec
 wsma profile listener exec
    transport http path /wsma/exec
 </pre>
 
<pre>
cgna gzip`
 
 cgna profile cg-nms-register
  add-command show version | format [flash:/managed/odm/cg-nms.odm](http://flash/managed/odm/cg-nms.odm)
  add-command show inventory | format [flash:/managed/odm/cg-nms.odm](flash:/managed/odm/cg-nms.odm)
  interval 3
  transport-profile wst
  gzip>
  active
 end
 </pre>

## Verify that the connection is working

Enter the following command and validate using this command: 

<pre>
show ida transport-profile-state name wst
</pre>

If the status is listed as IDA Status: Connected, then the switch status is listed as **UP** in IoT OD **Application Manager** > **Devices >Registered screen**.

![Devices Registered screen](../graphics/app_mgr/App_Mgr_Add_Device_01.png)

>**Note**: If this command does not work, check the [Troubleshooting Tips](https://developer.cisco.com/docs/iotod/troubleshooting-tips/#troubleshooting-of-externally-managed-devices).

## Add a switch to Secure Equipment Access service

1. Choose **Secure Equipment Access > System Management > Network Devices > Add Network Device**.
2. Choose the **new device** (switch). Click **Next**.
3. In the **Network Device Details** screen click the **VLAN** switch to open the **VLAN settings options**.
4. In the **Management VLAN** field, enter the **VLAN ID** (range 0-4093). This is the VLAN used for access to the internet and more specifically to Cisco IoT OD Cloud.

{%note info %}
**Note**:
  
* The SEA Agent is automatically  installed on the switch and is able to receive an IP address from a DHCP server running on that VLAN.
* If there is no DHCP running on that VLAN, you can configure one in IOS-XE. 
{%endnote%}  

5. Click **Add Network Device**. The switch is now listed in the **Secure Equipment Access** column.

>**Note**: When the device status is listed as **UP**, the switch automatically installs the SEA Agent application in IOx in the next 3-5 minutes. No other manual steps are required.

6. After all the configuration information is completed, click **Add Device**, The configured device is added to the **Device** screen as **Registered**. The device can now be added for SEA.  See [Add Network Devices and Assets](../secure_equipment_access/add_network_devices.md)
