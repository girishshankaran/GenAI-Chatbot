# SEA: New System Admin Workflow

The guided new user workflow is designed to help a first-time SEA System Admin to set up and access a remote OT Asset in very few steps and to be able to access the asset later in the future. Unlike the Quick Wizard you must install an SEA Agent before you can install an Asset. Once you install the agent and asset, the screen changes to show the link to the newly installed network device as well as links to the asset, the type of access method used, and the ability to launch the access method.

As an SEA System Admin, when you log in and open the SEA application, the **System Management** screen opens with the setup card. This card allows you first to install the SEA Agent, then add a Remote Asset and configure the appropriate Access Method to communicate with the asset.

![New User WkFlw Cards](../graphics/sea/21123_Initial_screen_00.png)

>**IMPORTANT**: If you close the configuration flow card, it will not open again, when you access **System Management**. If you still need guidance, use the Quick **Wizard** menu option in the left navigation menu. When you log into SEA again, you can use the **Quick Wizard** to install, connect, and deploy **Network Devices**. 

>**Note**: You can add and configure SEA Agents and Network Assets using [Add Network Devices and Assets](../secure_equipment_access/add_network_devices.md).

![Add_Network_Device](../graphics/sea/21123_Initial_Scrn_00d.png)

## Install SEA Agent and Asset

**To install and configure an SEA Agent for a Network Device:**

1. Click **System Management**.
2. **Install SEA Agent**, click **Start Configuration**.

![Install SEA Agent](../graphics/sea/21123_Initial_Scrn_00a.png)

3. In the **Install SEA Agent** screen select an existing **Network Device** from the list. Click **Next**.

![Select Network Device](../graphics/sea/21123_Install_Agent_Scrn_01.png)

4. The **Advanced Configuration** screen opens.

The **Advanced Configuration** screen differs according to what **Network Device** is selected. 

>**Note**: For information on router or switch configuration, see [SEA: HTTP(S) proxy support](..//secure_equipment_access/http_proxy_support.md) or [SEA: Multi-VLAN and Static IP support](../secure_equipment_access/multi-vlan_static_ip_support.md).


**Advanced Configuration screen** 

![Adv_Config_device](../graphics/sea/21123_Adv_Config_screen_switch_03b.png)

5. When you have configured the **Network Device**, click **Deploy**. It can 3-5 minutes to enable the device.

6. Once you deploy the **Network Device**, you are returned to the **System Management** screen with a green check by **Install SEA Agent** and the **Connect to Asset** button activated.

![Successful Install](../graphics/sea/21123_Connect_Asset_Scrn_05b.png)

{%note info %}

**Note**: 
* If the installation fails, a Deployment Failed screen opens and gives a reason.
* If you return to the **Get started with Configure Access to Remote Asset** screen before the Network Device is deployed or if the deployment fails, the **Install SEA Agent** field color is Yellow and a message describing the installation status shows.
{%endnote%} 

![Install Failed](../graphics/sea/IE_QSG_Install_Device_failed_01.png)

## Connect to Remote Asset

1. After choosing **Connect to Asset**, the screen opens to the **Configure Connected Asset** section, enter the **Asset Name** and the **IP Address**.

![Connect to Asset](../graphics/sea/21123_Connect_Asset_Scrn_06a.png)

2. In the next **Connect to Asset** screen, enter the Access Method for the Connected Asset and enter the pertinent information for that **Access Method**. For information on each access method, see [Access Methods](../secure_equipment_access/access_methods.md).
/secure_equipment_access/sea_plus_access_method.md
>**Note**: All access methods are available **Except SEA Plus**. Click [here](../secure_equipment_access/sea_plus_access_method.md) for more information on using **SEA Plus** as an access method. 

![Choose Access Method](../graphics/sea/21123_Connect_Asset_Scrn_07d.png)

3. (Optional) Choose an **existing group** in the **Assign to an Access Control Group** field. 

>**Note**:  To assign an **Access Control Group** from this screen, the access group must already be created. Click [here](../secure_equipment_access/manage_schedule_access.md) to create an **Access Control Group**. Once you creat a group and test the **Access Method** described in **Step 5**. 

4. When done, click **Next** test the configuration. 
5. Click **Validate Test Method** to launch the remote session to the **Connected Asset**.
6. Click **Complete**. You are returned to the System Management screen where the Agent and Asset icons are green and links are provided that enable you view the network device and asset as well as to view and launch the access method used. 

![Completed Installation](../graphics/sea/21123_Completed_Install_Scrn_01.png)
