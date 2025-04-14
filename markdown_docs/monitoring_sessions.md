# Monitor sessions

>**Note**: You must have either an SEA System Admin or SEA Access Admin role to use this feature. 

This feature is a security measure that allows the SEA System Admin or SEA Access Admin to login, monitor, and immediately terminate remote sessions. 

From the **SEA Service** panel, choose **Access Management > Active Sessions** tab. The active sessions screen lists all sessions that are currently in use (active). 

![Active Sessions tab](../graphics/sea/SEA_monitor_00b-active%20sessions.png)

The Active Sessions screen lists the following information:

* **Connected Client**: Shows what session is currently open (from the **Remote Sessions** screen). 
* **Access Method**: Shows what SEA method is used to access the session. See [Access Methods](access_methods.md).
* **User**: Shows who is currently in the session.
* **Session Start**: Shows when the session was opened.
* **Duration**: Shows how long the session was open. If the session is currently open, the Duration parameter lists it as Unscheduled. 
* **Monitor**: Shows the **Join Session** option for the supported access methods.
* **Security**: Shows the **Terminate** option. 

## Launch a remote session from the Active Sessions screen

Once a remote session is created and configured with and asset(s) and users, you are then able to launch the session.

1. Navigate to the **Active Sessions** tab. 
2. Select the **Active Session** from the list and in the **Monitor** column, click **Join Session**.

## Monitor a session
Joining a session allows a user (for example, an OT Manager) to supervise supported session types and view what happens during the session. For example, when an external technician delivers remote support for an asset, an OT person can control the technician's actions and terminate the active session at any moment. The monitoring functionality can also be used for training purposes.

**To join a session:**

>**Note**: This feature only allows the following access methods: SSH, VNC, RDP, and Telnet.

1. From the **Access Management** screen, click **Active Sessions**.
2. Choose the **Session** you want to monitor.
3. Click **Join Session**. That session opens. You can monitor all the actions in the session through session screen.

>**Note**: You can only monitor a session. You cannot interact with it in any way except to terminate the session by clicking **Terminate** in the **Active Sessions** screen.

![SEA_Monitor_Screen](../graphics/sea/SEA_monitor_full_screen_join_session_02.png)

>**Note**: 
You can only monitor a session, you cannot interact with it in any way except to Terminate the session by clicking **Terminate** in the **Active Sessions** screen.

![Full Screen Monitor](../graphics/sea/SEA_monitor_full_screen_01.png)
## Export (download) SEA session history in CSV format

As an SEA Admin, you can download SEA sessions using the Download Session History. This feature allows you to select a date range and download any active session in that range as a **.csv file**. You can filter the download by specific parameters such as: Session Start, Session End, Access Method, User, and Total Bytes. You can also filter downloads to only recorded sessions by clicking the **Show Recorded Sessions** checkbox.  

**To download SEA session history**:

1. From the **Secure Equipment Access** panel, choose **Access Management > Session History**.

![Session History](../graphics/sea/SEA_monitor_00b-session_history_menu.png)

1. Select the **date range** for the sessions using the **calendar pop-up windows**.

**Note**: The time and date the sessions are exported is in UTC.

3. (Optional) Click the **Only Show Recorded Sessions** checkbox to limit the download to only recorded sessions.

**Note**: The session data is exported based on the sort order of the table column selected. 

4. Click **Download Session History** a prompt opens showing that the download was successful.

![Download History](../graphics/sea/SEA_monitor_00b_download_history.png)

5. The **.csv** file is listed in your **Downloads** directory with the date it was downloaded.

## Terminate a session

When you are monitoring a session and you note that there appears to be an action that can damage the system, you can click the **Terminate** option in the **Security** column.

When you click **Terminate**, a Terminate Session prompt opens notifying you that, "Terminating the current session will end the session for the User that initiated it, preventing further action." You can either:

* **Cancel**: To cancel the terminate action and let the session continue.
* **Terminate**: Confirms the terminate command and the session is terminated.

A **Session Timed Out** notice opens in the user's session preventing the user from taking any other actions. The active session is no longer visible from the Admin's Active Sessions screen.
Open the Session History screen by choosing the **Session History** tab and the terminated session is listed showing all the pertinent information and **Yes** in the **Terminated** column.

![Session History](../graphics/sea/SEA_monitor_01b-session_history-teminated.png)

## Operations for SEA networks devices and assets:

**Add a Network Device**

When you add an SEA Agent you must also configure a Network Device. See [Add a network device](../secure_equipment_access/add_network_devices.md)

**Add Assets**

To add an Asset (such as a switch or IR device) to a Network Device, see [Add an asset](add_assets.md).

**Configure SEA proxy support for switches**

To configure an SEA agent with proxy support on an externally-managed device (such as a IE3x00 switch), see [SEA: Proxy HTTP support](../secure_equipment_access/http_proxy_support.md).

**Configure SEA multiple VLAN support**

To configure an SEA agent with VLAN or Static IP support on an externally-managed device (such as an IR 1100 or IR1800 router), see [SEA: Multi-VLAN and Static IP support](../secure_equipment_access/multi-vlan_static_ip_support.md).

## Additional SEA funtionality

**Manage access control group asset sessions**

Use the Access Management option to create groups of users who can remotely access the network devices and assets. See [Manage access control groups asset sessions](../secure_equipment_access/manage_schedule_access.md).

**Record Inline sessions**

This Secure Equipment Access (SEA) feature allows you to record sessions for future use, such as auditing or educational purposes. Recordings are stored in your own storage space on AWS S3 using the retention policies for the recordings at this location. See [Record Inline Sessions](../secure_equipment_access/record_inline_sessions.md).

## SEA Plus functionality

**SEA Plus access method**

Using the SEA Plus access method. See [SEA Plus access method](../secure_equipment_access/sea_plus_access_method.md).

**Configuring SEA Plus protocol defintions**

Configure protocol definitions for the asset. See [Configure SEA Plus protocol definitions](../secure_equipment_access/sea_plus_config_protocol_def.md).

**Duo security checks for SEA Plus**

If using Duo security policies with SEA Plus, it is necessary to create appropriate policies on Duo for the user’s computer security posture check for remote access to OT assets. You can request a free, 30-day trial that works with IoT OD. See [Duo user security checks for SEA Plus](../secure_equipment_access/duo_posture_checks.md).