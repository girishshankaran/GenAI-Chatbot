# Device Inventory
The **Devices** page in **Application Manager** maintains the inventory of all externally-managed devices that have
initiated their onboarding process to the IoT OD. 
The **Devices** page also lists externally-managed devices that have not yet initiated the onboarding process.
>**Note**: Externally-managed devices pertains to devices that are managed through CLI, Cisco Controllers, and other third-party systems. It excludes EDM-managed devices (devices managed by the **Edge Device Manager** (EDM) service) in IoT OD. 

Through the **Devices** page, you can add/deactivate/delete the externally-managed devices. Each of these functionalities are detailed in the following sections. For details, see [Deactivate a device](..//edge_manager/device_deactivating.md) and [Delete a device](../edge_manager/device_deleting.md).

To view the details of externally-managed devices in **Application Manager**, see [Viewing Staged / Registered Device Details](#ViewingStagedDeviceDetails) on this page.

## Field Description

* **Registered**: Displays the list of all devices that are currently active and communicating with the IoT OD. This page shows the details of the devices and can be used for monitoring and managing applications on your devices. 

* **Staged**: Displays all externally-managed devices added through application manager but haven't successfully registered with the IoT OD yet. The reason for being unsuccessful could be because the IoT OD has not received any registration attempts from these devices, which may be due to either the device is not being configured to communicate with the IoT OD or experiencing connectivity issues. Through the **Staged** tab, you can add or remove the externally-managed devices to/from the IoT OD.

<a name="AddingSingleIEDevice"></a>
## Add a single externally managed device

1. From the **Sevices** pane select **Application Manager**.
2. Click **Devices > Staged** tab.
3. Click **Add Devices**.
4. Select a **Single Device** to open the **Add Device** page.
    
    ![Single Device](/graphics/app_mgr/single_device.png)
5. In the **Setup** page, provide the necessary inputs such as **Product ID (PID)**, **Serial Number**, and **Name** of the device. 

>**Note**: When entering the **Product ID (PID)**, provide the base PID without the E/A/RE/RA prefixes. These prefixes denote the license and are not required while adding the device to IoT OD.

6. Click the **checkbox** if you want to add your device using Latitude, Longitude values. It denotes the device's geographic location using it's specific latitude and longitude coordinates. 
7. In the **Assign Device Profile** page, select the device profile from the existing list and click **Next**. You have the option to create a new device profile and add your device by clicking **Device Profile** from the ![Information icon](/graphics/app_mgr/app_mgr_info_icon.png) banner and proceed. For details, see [Device Profiles](device_profiles.md)

    ![Add Device](/graphics/app_mgr/add_device.png)
8. In the **Review** page, verify the information and click **Add Device**. The device now appears in the **Staged** tab list.   

## Add multiple externally-managed devices in bulk

1. From the **Sevices** pane select **Application Manager**.
2. Click **Devices** > **Staged**. 
3. Click **Add Devices**.
4. Select **Multiple Devices**.

    ![Multiple Devices](/graphics/app_mgr/multiple_devices.png)

    **To upload using a .CSV file:**

    1. Select a **device** from the **Device Profile** list.
    2. Click **Download Sample CSV** that contains the correct column fields.
    3. Enter the **Settings** and **Variables** for your devices. Populate your .CSV file with the appropriate data.
    4. Upload the **.CSV file** that includes the settings for your network devices.
    5. Click **Claim** and wait for the success message to appear.  If the claim fails, correct your .CSV file and try again.

    ![Bulk Claim](/graphics/app_mgr/bulk_claim.png)
5. The device now is listed in the **Staged** tab.

    ![Device List](/graphics/app_mgr/app_mgr_devices_staged.png)

At this stage, adding the device to the IoT OD is complete and ready to process registration attempts from the actual device.

Device credentials for a specific device is obtained from the associated device profile and can be reviewed on the device **Summary** page. The details of the **Summary** page is explained in the following sections. 

## View Staged Device Details
1. From the **Sevices** pane select **Application Manager**.
2. Go to **Devices > Staged** to view details of the device that is yet to be onboarded
3. Click the device name to view the **Summary** and **Event Log** details.
4. In the **Summary** page, you can view the following details pertaining to the selected device:
   1. **Managed By**: Indicates if the device configuration is managed by IoT OD or other management system such as CLI, DNAC, etc.
   2. **Serial Number**: The serial number of the device. This is a unique number to help identify the individual devices which is necessary with inventory management, warranty purpose or service support.
   3. **Last Heard**: The last known timestamp indicating the time when the data exchange occurred between the device and IoT OD.
   4. **Model**: Device Model Name / Product ID of the device.
   5. **Latitude / Longitude**: The device's geographic location using it's specific latitude and longitude coordinates. This helps to pinpoint the exact geographical location to track devices.
   6. **Name**: The name provided to the device while onboarding onto IoT OD.
   7. **Firmware Version**: The current firmware version of the device.
   8. **Uptime**: The continuous operational period of the device without interruptions/downtime after a reboot.
   9. **Device Profile**: The profile to which the device is associated. For more details, see [Device Profiles](device_profiles.md).
   10. **Admin Username / Password**: The device credentials that can be obtained from the associated device profile.
5. In the **Event Log** page, you can view the device event information such as severity of an event, the event type, any relevant message and the timestamp. 

## View Registered Device Details

![Device Details](graphics/app_mgr/../../../graphics/app_mgr/app_mgr_devices_registered.png)

1. From the **Services** pane, select **Application Manager**.
2. Go to **Devices > Registered** to select devices onboarded to IoT OD.
3. Click the **device** to view the details. This page contains the device **Summary**, **Event Log**, and also provides you **Troubleshooting** options.
4. In the **Summary** page, you can view the following details of the device. 
   1. **Status**:
      1. **Device Status**: Specifies the device connection status to the IoT OD. The status can be **Up** or **Down**.
      2. **IOx Status**: Specifies the status of application management framework (IOx) on the device. The status can be **Up**, **Down**, or **Unknown**. An **Unknown** status means that the IoT OD was/is not able to connect to IOx to fetch the latest status.
   2. **Deployed Applications**:
      1. **Name**: Displays the applications deployed on the device.
      2. **App Status**: Displays the status of the applications such as **DEPLOYED**, **RUNNING**, **STOPPED** and so on. 
      3. **Version**: Displays the application version.
      4. **Transitional Status**: Indicates if the application is transitioning from one state to another.
      5. **Actions**: Navigate to App Instance - Click this link to navigate to the **Application Instances** page to view application details
   3. **IOx Resource Allocation**: Displays the details such as the CPU usage, available Memory and total/available Disk space allotted for the applications in a device.
5. Click **Event Log** to view the device events such as severity of an event, any relevant message and the timestamp.
6. Click **Troubleshooting** to find options to diagnose any device issues, reboot the device or refresh device metrics. For details, see <a href="#TroubleshootingOptions">Troubleshooting Options</a> in the following section.

<!--## Troubleshooting Options-->
<h2><a name="TroubleshootingOptions"></a>Troubleshooting Options</h2>

To use **Troubleshooting** tools, the device should register successfully on IoT OD and establish websocket tunnel. The **Troubleshooting** page allows **Ping IP**, **Traceroute IP**, and **IOS Show Commands** initiation on the device. 

1. From the **Services** pane, select **Application Manager**.
2. Go to **Devices > Registered**.
3. Click on the **device** you want to troubleshoot.
4. Click **Troubleshooting**. This page contains the **Troubleshooting Options**.
5. To diagnose the issue. choose the required option, enter the necessary details and click **Execute**. Once the process is triggered, click on **Show Result** to view the result of the operation:
   1. Select **Ping IP address from the device**: 
      1. **Specify the IPv4 / Hostname**: The destination IPv4 address or a hostname associated with the device.
      2. **Source and the Datagram Size**: Specify the source from where the data originated and the data size.
      3. **Set DF Bit in IP Header**:  The "do not fragment" (DF) bit determines whether or not a packet is allowed to be fragmented. This instructs the device not to fragment or break the data packet into smaller segments and ensure seamless transmission. You can enable this field using the toggle switch.
   2. Select **Traceroute IP address from the device**:
      1. **Specify the IPv4 / Hostname**: The destination IPv4 address or a hostname associated with the device.
      2. **TTL Minimum/Maximum**: Specify the minimum/maximum "Time to Live" (TTL) value for packets within the specified range.  This indicates that packets with TTL value below the minimum or exceeding the maximum will be discarded.
   3. **Select IOS Show Commands**: Type the required IOS show command that you want to initiate.
6. You can click **Show Result** after every execution to view the result of your above operations.

## Deactivate an Externally Managed Device

An externally managed device can be deactivated if you no longer want the device to connect to IoT OD. This operation does not remove the device from the IoT OD inventory, but only disconnects the device and moves it to **Staged** inventory.

>**Note**: Before deactivating a device, remove the IoT OD specific configuration settings such as transport and registration profiles configured on the device, or the device will trigger registration requests to the IoT OD periodically and the deactivated device will show up again as **Registered**.

1. From the **Services** pane, select **Application Manager**.
2. Click **Devices > Registered**. 
3. **To Deactivate**: Click the **checkbox(s)** to select the device(s) and click **Deactivate Device**. The selected device(s) is deactivated and moved to **Staged**.
   
## Delete an Externally Managed Device

To delete an externally-managed device from the IoT OD Inventory and stop managing applications on the device, complete the following steps: 

1. From the **Services** pane, select **Application Manager**.
2. Click **Devices > Registered**.
3. To Delete: Click **Staged**. Click the **checkbox(s)** to select the device(s) and click **Delete Device**. This operation deletes the device from the IoT OD device inventory.
