# SEA: Quick Wizard

>**Note**: **Quick Wizard** is only available to **SEA System Admin** users.

The Secure Equipment Access (SEA) **Quick Wizard** provides a simplified process to configure remote client access. **Quick Wizard** includes the following two process options:

* Install an **SEA Agent** 
* Connect to an **Asset**

Each procedure can be used independently. 

**Note**: You can access the SEA documentation by clicking the link at the top left corner of the screen.
![QW_Blank](../graphics/sea/22431_QW_blank_00c.png)

## Install and configure an SEA Agent for a device

1. Click **Quick Wizard**.
2. Select **Install SEA Agent**, click **Start Configuration**. 

![QW_SEA_Agent](../graphics/sea/22431_QW_00c.png)

3. In the **Install SEA Agent** screen, select an existing **Network Device** from the list. Click **Next**. The **Advanced Configuration** screen opens.

![QW_Install Agent](../graphics/sea/21123_Install_Agent_Scrn_01.png)

4. The **Advanced Configuration** screen opens.
The Advanced Configuration screen differs according to the device that is selected (router or switch). 

>**Note**: For information on router or switch configuration, see [SEA: HTTP(S) proxy support](..//secure_equipment_access/http_proxy_support.md) or [SEA: Multi-VLAN and Static IP support](../secure_equipment_access/multi-vlan_static_ip_support.md).   

**Advanced Configuration Screen**

![Adv_Config_device](../graphics/sea/21123_Adv_Config_screen_switch_03b.png)


5. When you have configured the network device, click **Deploy**. It can take 3-5 minutes to enable the device.

>**Note**: If the installation fails, a Deployment Failed screen opens with the reason.

## Connect to a remote asset

1. From the **Quick Wizard**, click **Connect to Asset**.

![Connect to Agent](../graphics/sea/22431_QW_remote_asset_00a.png)

2. Select the **Network Device**.

![Connect_to Asset_2](../graphics/sea/22431_QW_remote_asset_01.png)

3. In the **Connect to Asset** screen, enter the **Asset Name** and the **IP Address**.

![Connect to Asset](../graphics/sea/21123_Connect_Asset_Scrn_06.png)

4. In the **Configure Access Method** screen, enter the **Access Method** for the Connected Asset.

>**Note**: All access methods are available **Except** SEA Plus. Click [here](../secure_equipment_access/sea_plus_access_method.md) for more information on using **SEA Plus** as an access method. 

![Connect to Asset_01](../graphics/sea/21123_Connect_Asset_Scrn_07b.png)

5. Enter the information for that **Access Method**. For information on each access method, see [Access Methods](../secure_equipment_access/access_methods.md).
6. (Optional) Choose an **existing group** in the **Assign to an Access Control Group** field.

>**Note**:  To assign an Access Control Group from this screen, the access group must already be created. Click [here](../secure_equipment_access/manage_schedule_access.md) to manage and schedule groups.

7. When finished, click **Next** test the configuration.
8. Click **Validate Test Method** to launch the remote session to the **Connected Asset**.

![Test_Connection](../graphics/sea/21123_Connect_Asset_Test_Scrn_09.png)

9. Click **Complete**. The newly added network device a listed in the network device table in **System Management**. 
