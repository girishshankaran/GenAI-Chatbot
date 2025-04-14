# Add Network Devices and Assets

>**Note**: Only SEA System Admin role can access this menu on IoT OD. 

Use **System Management** to provide secure remote communication with IoT network devices and assets. The asset can either be a network device or the subtended devices attached to that network device.

>**Note**: Cisco also provides a guided, new user workflow and quick wizard designed to help a first-time SEA System Admin to access a remote OT Asset in a few steps. For more information, see [SEA: New User Workflow](../secure_equipment_access/sea_new_user_wrkfw.md). For a more efficient means of installing and updating network devices or assets see [SEA Quick Wizard](../secure_equipment_access/sea_quick_wizard.md).

## Summary steps

1. Add **Network Devices** that were previously onboarded and configured.
2. SEA installs and activates SEA Agent on the network device in the background.
3. Add the **Asset** attached to the network devices that users can access.
4. Configure **SEA Plus protocols** for network devices and Assets.

>**Note**: On Cisco IR devices running IOS or IOS-XE, the SEA Agent is automatically installed and configured on the network device.

## Add Network Devices

1. From the Services pane, choose **Secure Equipment Access > System Management**.
2. From the **Network Devices** tab, click **Add Network Device**. A list of possible network devices opens. 

![System Management](../graphics/sea/21121_Sys_Mgmt_Initial_Scrn_00a.png)


3. Choose a **network device** from the list or search for it in the **Search** field. Click **Next**.
4. Enter a **network device description**, if needed, and click **Add Network Device**.
   SEA service starts the installation of the SEA Agent on the device in the background.
   
>**Note**: At this step, if you are installing a switch, you can configure the switch for HTTP(S) proxy support. Click [here](../secure_equipment_access/http_proxy_support.md) for directions on configuring for HTTP(S) proxy support. To configure switch with multi-VLAN configuration, see click [here](../secure_equipment_access/multi-vlan_static_ip_support.md). 

1. Click **Next**. A confirmation box opens.
2. Check the SEA Agent state of deployment associated with the network device.
    * The **SEA Agent** deployment state changes to **Installed**, and this can take up to 5 minutes. If the status doesn't change to Installed, go to the network device listing and hover over the **3 dots** in the **Actions column** and choose **Install SEA Agent**. 

   ![Install SEA Agent](../graphics/sea/SEA_Install_SEA_Agent_00a.png)

## Manually Add Assets

To manually add an Asset for a device: 

>**Note**: These devices can be subtended devices, or the network device itself.

![Add IoT devices](/graphics/sea/Add_Asset_03_composite.png)

1. From the **System Management** page, choose a **Network Device**.
2. From the **Network Device details** page, click **Add Asset**.
3. On the **Add Asset** page, choose one of the following options:
   * **Select from list (Recommended)**
   * **Manual entry**
4. After you choose the option, click **Add**. The asset is associated with the network device.

### Using the Network Device as an Asset for Configuration or Troubleshooting

Use the network device itself as an asset to configure or troubleshoot the device. For IR devices, use the VirtualPortGroup0 IP address and for IE devices, use the VLAN IP address that SEA Agent is configured to run on, to add access methods for accessing the device itself. 


## Configure SEA Plus Protocol Definitions

{%note info %}
**Note**:
* The SEA Plus App must be running (minimum version is 0.70). 
* There is an existing Network Device and Asset configured for remote access. 
{%endnote%}

**To configure an SEA Plus protocol:**

1. From the **Services** panel, choose **Secure Equipment Access > System Management**.
2. Choose the **SEA Plus Protocols** tab. This screen has three SEA Plus Protocol Definition setting filters.

    * **All** (Default): Choose this filter to list all the definitions created (custom and predefined).
    * **Custom**: Choose this filter to list all the custom definitions created.
    * **Predefined**: Choose this filter for a list of "out of the box" protocol definitions that can help you get started. 

{%note info %}
**Note**:

* The three predefined definitions: **Allow all Protocols**, **TCP All Ports+ICMP**, and **UDP All Ports+ICMP** should be used with caution. Once you are familiar with setting up the SEA Plus Definitions, we recommend configuring your own protocols and ports to fit your needs and security requirements. 
* You cannot add **SEA Plus Protocol Definitions** from the Predefined filter.
{%endnote%}

![SEA Plus Protocols](../graphics/sea/SEA_Plus_Prot_Initial_00.png)

The SEA Protocols screen lists the following:
* **Name**: Protocol Definition Name.
* **Tag** (optional): Used for grouping definitions.
* **Description**: Description of the protocol definition.
* **Last modified**: Protocol definition was last modified.
* **Actions**: Clone or Delete. 

The SEA Plus Protocols screen also includes a **Search Table** field and a **filter icon** (right side of the screen) for searching through long lists of protocol definitions. 

>**Note**: If you clone a protocol definition, the definition has the same name with a number in parenthesis. For example, Protocol (1), Protocol (2), etc. 

1. To add a Custom Protocol Definition, click **Add Protocol Definition**.

![Protocol Definition](../graphics/sea/SEA_Plus_Prot_Initial_01.png)

1. Make sure you are in the **SEA Plus Protocols** tab. Then enter:
   
   a. (Required) Type in a protocol definition **name**. 
   
   b. (Optional) Type in an identifying **tag** (for grouping).
   
   c. (Optional) Type in a useful **description**.

2. Click **Add Protocol**.

![Add Protocol](../graphics/sea/SEA_Plus_Prot_Initial_02.png)

7. In the **Add Protocol** screen choose one of the following protocols:

  * TCP All Ports
  * UDP All Ports
  * TCP
  * UDP
  * ICMP

8. For UDP and TCP, specify a single **Port** (or Port Range, for example 85-110) for that protocol.
9. Click **Add Protocol**. The protocol is added to the protocol list.
10. To add additional protocols, repeat **step 6-9**.
11. Click **Save Protocol Definition**. The custom protocol definition is added to the **SEA Plus Protocol Definitions** list.

Once the definitions are created they can be used when you create the access methods for SEA Plus. (See [SEA Plus Access Method](/secure_equipment_access/sea_plus_access_method.md).)

>**Note**: To configure an IE3x00 switch or IR18xx router in SEA, refer to the appropriate section below.

### SEA: Proxy Support for Switches
To configure an SEA agent with proxy support on an externally managed device (such as a IE3x00 switch), see [SEA: HTTP(S) proxy support](..//secure_equipment_access/http_proxy_support.md)

### SEA: Muli-VLAN Support

To configure an SEA agent with VLAN or Static IP support on an externally managed device (such as an IR1101 or IR1800 router), see [SEA: Muli-VLAN and Static IP support](../secure_equipment_access/multi-vlan_static_ip_support.md).
