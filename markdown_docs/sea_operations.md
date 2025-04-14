# SEA operations

For application managed devices, there are two methods by which you can configure SEA Network Devices (Devices) and their Assets.

* Follow the sequence in the [SEA Quick Wizard](../secure_equipment_access/sea_quick_wizard.md) for either SEA Agent, Asset, or both.
* Manually add Devices and Assets along with access method(s) to connect with [Open SEA remote asset sessions](../secure_equipment_access/access_remote_sessions.md).

>**Note**: For **SEA System Admin** new to SEA, there is a [New User Workflow](../secure_equipment_access/sea_new_user_wrkfw.md) that can be used as a temporary quick wizard. Otherwise, you can use the [SEA Quick Wizard](../secure_equipment_access/sea_quick_wizard.md) as a starting point for configuring Devices and Assets.

## Operations for SEA networks devices and assets:

**Add a Network Device**

When you add an SEA Agent you must also configure a Network Device. See [Add a network device](../secure_equipment_access/add_network_devices.md)

**Add Assets**

To add an Asset (such as a switch or IR device) to a Network Device, see [Add an asset](./add_assets.md).

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

**Configuring SEA Plus protocol defintions**

Configure protocol definitions for the asset. See [Configure SEA Plus protocol definitions](../secure_equipment_access/sea_plus_config_protocol_def.md).

**Duo security checks for SEA Plus**

If using Duo security policies with SEA Plus, it is necessary to create appropriate policies on Duo for the user’s computer security posture check for remote access to OT assets. You can request a free, 30-day trial that works with IoT OD. See [Duo user security checks for SEA Plus](../secure_equipment_access/duo_posture_checks.md).