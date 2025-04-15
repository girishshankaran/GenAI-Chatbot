# Onboarding Externally-Managed IE3x00 Switches
This section guides you through the process of onboarding an externally-managed device to the IoT OD Application Manager's Inventory and deploying Operational Technology (OT) services on the device.  It also includes the device configuration process and initiating connection to the dashboard. For details, see [IE Device Configuration and Initiating Connection to OD](ie_device_config_initiate_conn_iotod_17_13.md).
>**Note**: Externally-managed devices refers to devices that are managed through CLI, Cisco Controllers, or other third-party systems. It excludes devices managed by the Edge Device Manager (EDM) service in IoT OD. 

The IoT OD System Administrator can onboard externally-managed devices on the OD. For details on roles and permissions, refer [Role-Based Access Control](role_based_access_control.md).

## Prerequisites
Ensure the following for successful onboarding of the devices and deploying the Application Manager service:
1. IoT OD (Customer Organization): Create your Organization (with active support for externally-managed devices) and onboard a target IE3x00 device as externally-managed. See Step 3 below.
2. IE3x00 Device: Ensure IE3x00 has an SD card and runs a minimum IOS-XE version 17.13.1 or higher. Apply the required configuration commands via CLI, Local Manager, or Catalyst Center template. See Step 4 below.
3. Service Deployment: Configure a required service on IoT OD. For example, to configure SEA service, go to the **SEA** service in your Organization. See Step 5 below.

## IoT OD Service Activation on an Externally-Managed IE3x00 Device
This section details the process and workflow required to have a **Service** supported by IoT OD up and running on an externally-managed IE3x00. The information is organized into the following steps:
* Step 1: Device Readiness
* Step 2: Customer Site Readiness
* Step 3: Cloud Infrastructure and Operations Dashboard Readiness
* Step 4: Device Configuration and Initiating Connection to OD
* Step 5: IOx Application Deployment, **Service** Configuration, and Activation
* Step 6: IoT OD Service Deactivation and Device removal on an Externally-Managed IE3x00

### Step 1: Device Readiness
**To ready your device**:
1. Ensure IoT OD supports your device.
   IoT OD supports externally-managed IE3x00 - IE3400 (all models) and IE3300 (4GB/RAM models).
2. Make sure the IE3x00 device has an SD card installed and is configured. For more information, see **Configure and Enable IOx** section in [IE Device Configuration and Initiating Connection to OD](ie_device_config_initiate_conn_iotod_17_13.md).
3. Cable the device securely. Use the power cable and uplink connection cables.
4. Ensure that the device is configured such that it has an IP address and internet access (to connect to IoT OD). Device configuration might include interfaces and networking.
5. Record the serial number and base product ID of the device for later use.
6. For externally-managed IE3x00 switches, apply configuration command shown below to establish websocket tunnel between the device and IoT OD.

<pre>
Use the following command to show the product ID and serial# for your device:
Switch#show license udi
UDI: PID:IE-3300-8T2X,SN:FTX2000000N

In this example, the product ID (PID) is IE-3300-8T2X and serial number (SN) is FTX2000000N. 
This data will be used to add the device to IoT OD.
</pre>

### Step 2: Customer Site Readiness
**For site security** 
1. Refer to [Firewall Rules: Device and network requirements](firewall_rules_device_network_reqs.md) and verify if you are using the available IP addresses and network ports for your region (EU or US).
2. Please ensure the site is ready for communication with IoT OD by allowing dashboard's public IP addresses through ACLs, etc.
   >**Note**: To simplify and start faster, open 9 IPs to communicate with the US or EU IoT OD clusters and port 443.  At every given moment, only 3 IPs are used to communicate from each pool, but they can swap over time within the pool of 9.

   For a complete list of IP addresses for each cluster, see the following links:

  * [US Cluster](https://us.ciscoiot.com)

  * [EU Cluster](https://eu.ciscoiot.com)

    For more specific use cases, please refer to the [Firewall Rules: Device and network requirements](firewall_rules_device_network_reqs.md).

### Step 3: Cloud Infrastructure and Operations Dashboard Readiness
**To begin onboarding an existing IE3x00 device into IoT OD**:
1. If the customer organization is not created on IoT OD, create the organization. Use the online instructions at [us.ciscoiot.com] or [eu.ciscoiot.com] based on the geographical location. In case of issues, use ask-sea-pm@cisco.com to contact support.
2. Log in to the organization with a user who has appropriate permissions/roles to add devices or ask the Tenant Admin to create one.

>**Note**: When a new user is created on IoT OD, the target user will receive a personal invitation to access the cloud platform. Only a Tenant Admin can pre-define or assign a custom role to the user.

3. Create a new Device Profile or select an existing Device Profile for the device as applicable. For details on creating, editing or deleting a device profile, see [Device Profiles](device_profiles.md).
4. Add the device in IoT OD as an externally-managed device. For details, see [Device Inventory](device_inventory.md).

### Step 4: Device Configuration and Initiating Connection to OD
For details, see sections on **Configuring devices managed by CLI/Local Manager** and **Configuring Devices managed by Catalyst Center** in [[IE Device Configuration and Initiating Connection to OD](ie_device_config_initiate_conn_iotod_17_13.md).

### Step 5: IOx Application Deployment, Service Configuration, and Activation
See the following documentation for additional reference on Application Management in IoT OD:
* [Application Management](../edge_manager/app_mgmt.md)

{%note info %}
**Note**:
* In most cases, you don't need **Application Management** to deploy **SEA** **Service** on IoT OD. You can make all necessary service-specific configurations for those **Services**, including software installation onto IE3x00 devices, in the corresponding services on IoT OD.
* To deploy **EI**, you will need **Application Management** for installing **EI** software onto the IE3x00 device. Afterward, you can use the EI service on IoT OD to configure it. {%endnote%}

#### Secure Equipment Access (SEA)
For installing, configuring, and activating SEA on a device, see the following topics:
* [Secure Equipment Access–Overview](../secure_equipment_access/sea_overview.md)
* [Cisco SEA on IE swicthes - Quick Start Guide](../overview_iot/config_catalyst_sea_qkst.md)
* [Add network devices and connected clients](../secure_equipment_access/add_network_devices.md)
 
#### Edge Intelligence (EI)
For installing, configuring, and activating Edge Intelligence on a device, see the following topic:
* <a href="../edge_intelligence/ei_agents.md#InstallIOTOD">Install EI agent on unmanaged devices using IoT OD</a>

### Step 6: IoT OD Service Deactivation and Device Removal on an Externally-Managed IE3x00
**To deactivate IoT OD Services on an Externally-Managed IE3x00**:
1. Remove the OD-specific configuration from the device. 
   <pre>
   // Remove the IoT OD connection profiles
   no cgna transport-profile wst
   no cgna profile cg-nms-register

   // Remove the user that was used by IoTOD (if this user is not used for any other purposes on the device)
   no username odserviceuser
 
   // Remove the trustpoint created for IoT OD connection (use the same name that was given while configuring the trust point)
   no crypto pki trustpoint iotod-cert

   // Remove WSMA & CGNA related configuration (if WSMA is not needed)
   no wsma agent exec
   no wsma agent config
   no wsma profile listener exec
   no wsma profile listener config
   no cgna gzip

   // Stop IOx and remove configuration of AppGigabitEthernet1/1 (if IOx is not needed)
   no iox
   interface AppGigabitEthernet1/1
   no switchport mode trunk
   </pre>

2. Deactivate the device in IoT OD.
   1. From the **Sevices** select **Application Manager**.
   2. Click **Devices > Registered**.
   3. Use the checkbox to select the device(s) to be deactivated.
   4. Select the **Deactivate Device** action on the top of the table.
   5. Confirm the operation, when prompted.
3. Remove the device from IoT OD.
   1. From the **Sevices** select **Application Manager**.
   2. Click **Devices > Staged**.
   3. Use the checkbox to select the device(s) to be removed.
   4. Select the **Delete Device** action on the top of the table.
   5. Confirm the operation when prompted.

For more details on possible errors and corresponding solutions see [Troubleshooting Tips](troubleshooting_tips.md).
