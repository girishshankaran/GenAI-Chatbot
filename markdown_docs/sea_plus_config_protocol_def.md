# Configure SEA Plus protocol defintions

{%note info %}
**Note**: 

* The SEA Agent must be downloaded (minimum version is 0.70).
* There is an existing Network Device and Asset configured for remote access.
{%endnote%}

**To configure an SEA Plus protocol**

1. Choose **Secure Equipment Access** > **System Management**.
2. Choose the **SEA Plus Protocols** tab. The SEA Plus Protocols screen has three SEA Plus Protocol Definition setting filters.

* **All** (Default): Choose this filter to list all the definitions created (custom and predefined).
  * **Custom**: Choose this filter to list all the custom definitions created.
  * **Predefined**: This filter provides a list of "out of the box" protocol definitions that can help you to get started.

{%note info %}
**Note**:  

* The three predefined definitions: **Allow all Protocols**, **TCP All Ports+ICMP**, and **UDP All Ports+ICMP** should be used with caution. Cisco **does not recommend** using them because they offer less protection. Once you are familiar with setting up the SEA Plus Definitions, Cisco recommends configuring your own protocols and ports to fit your needs and security requirements.
* You can't add **SEA Plus Protocol Definitions** from the Predefined filter.
{%endnote%}

![SEA Plus Protocols](../graphics/sea/SEA_Plus_Prot_Initial_00.png)

The **SEA Protocols** screen shows the:

* **Name**: Protocol Definition Name.

* **Tag** (optional): Tags are used for grouping definitions.

* **Description**: Provides a relevant description of the protocol definition.

* **Last modified**: Shows when the protocol definition was last modified.

* **Actions**: Clone or Delete.

The **SEA Plus Protocols** screen also includes Search functionality to facilitate searching through long lists of protocol definitions. The search field also includes a filter icon (right side of the screen) to facilitate quick searches.

>**Note**: If you clone a protocol definition, the definition will have the same name with a number in parenthesis. For example, Protocol (1), Protocol (2), etc.

3. To add a Custom Protocol Definition, click **Add Protocol Definition**.

![Add Protocol Definition](../graphics/sea/SEA_Plus_Prot_Initial_01.png)

4. Make sure you are in the **SEA Plus Protocols** tab. Then enter:
   1. (Required) Type in a protocol definition **Name**.
   2. (Optional) Type in an identifying **Tag** (for grouping).
   3. (Optional) Type in a useful **Description**.
   4. Click **Add Protocol**.

![Add Protocol](../graphics/sea/SEA_Plus_Prot_Initial_02.png)

6. In the **Add Protocol** screen choose one of the following protocols:

* (Not recommended) TCP All Ports
* (Not recommended) UDP All Ports
* TCP
* UDP
* ICMP

7. For UDP and TCP specify a single **Port**, (or Port Range, for example 85-110) for that protocol.
8. Click **Add Protocol**. The protocol is added to the protocol list.
9. To add additional protocols, repeat **steps 6-8**.
10. Click **Save Protocol Definition**. The custom protocol definition is added to the SEA Plus Protocol Definitions list.

Once the protocol definitions are created, they can be used when you create the access methods for SEA Plus. (See [SEA Plus access method](../secure_equipment_access/sea_plus_access_method.md).)

## Operations for SEA networks devices and assets:

**Add a Network Device**

When you add an SEA Agent you must also configure a Network Device. See [Add a network device](../secure_equipment_access/add_network_devices.md).

**Add Assets**

To add an Asset (such as a switch or IR device) to a Network Device, see [Add an asset](add_assets.md).

**Configure SEA proxy support for switches**

To configure an SEA agent with proxy support on an externally-managed device (such as a IE3x00 switch), see [SEA: Proxy HTTP support](../secure_equipment_access/http_proxy_support.md).

**Configure SEA multiple VLAN support**

To configure an SEA agent with VLAN or Static IP support on an externally-managed device (such as an IR 1100 or IR1800 router), see [SEA: Multi-VLAN and Static IP support](../secure_equipment_access/multi-vlan_static_ip_support.md).

## Additional SEA funtionality

**Connect to remote asset sessions**

Use the Remote Sessions option to access your remote asset sessions. See [Connect to remote asset sessions](../secure_equipment_access/access_remote_sessions.md).

**Manage access control group asset sessions**

Use the Access Management option to create groups of users who can remotely access the network devices and assets. See [Manage access control groups asset sessions](../secure_equipment_access/manage_schedule_access.md).

**Monitor network device sessions**

This feature can be used for security as well as an educational purposes. The SEA System Admin or SEA Access Admin can login, monitor, record, and, if the situation warrants it, immediately terminate the session. See [Monitor sessions](../secure_equipment_access/monitoring_sessions.md).

**Record Inline sessions**

This Secure Equipment Access (SEA) feature allows you to record sessions for future use, such as auditing or educational purposes. Recordings are stored in your own storage space on AWS S3 using the retention policies for the recordings at this location. See [Record Inline Sessions](../secure_equipment_access/record_inline_sessions.md).

## SEA Plus functionality

**SEA Plus access method**

Using the SEA Plus access method. See [SEA Plus access method](../secure_equipment_access/sea_plus_access_method.md).

**Configuring SEA Plus protocol definitions**

Configure protocol definitions for the asset. See [Configure SEA Plus protocol definitions](../secure_equipment_access/sea_plus_config_protocol_def.md).

**Duo security checks for SEA Plus**

If using Duo security policies with SEA Plus, it is necessary to create appropriate policies on Duo for the user’s computer security posture check for remote access to OT assets. You can request a free, 30-day trial that works with IoT OD. See [Duo user security checks for SEA Plus](../secure_equipment_access/duo_posture_checks.md).