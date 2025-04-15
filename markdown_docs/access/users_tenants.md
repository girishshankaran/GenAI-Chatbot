# Add and manage user access

## Introduction

Add users to provide access to your organization's network devices, configuration, and monitoring (events and alerts). Access roles are assigned to each user to define the features and functions they can access.

Built-in roles provide default sets of functionality, but you can also create custom roles that define different sets of access permissions or privileges. For example, you can create an "EI Management" role with permissions to manage data and assets. Users assigned to that role will gain those permissions. Create another "Operator" role for users that can only monitor the health of data policies and EI agents.

IoT Operations Dashboard (OD) provides Roles and Permissions for users.  A Role is defined as a collection of one or more Permissions. We provide two default Roles with a specific set of pre-determined Permissions. The default Roles and accompanying Permissions cannot be changed. The built-in Roles have the following capabilities and privileges:

* __Tenant Admin:__
    * Manage users. Add, delete, grant, and remove roles.
    * Manage sub-tenants (sub-organizations) and control who has access to them. Sub-tenant access extends a user's access privileges to sub-organizations.
    * Create custom roles.

* __Device Operator:__
    * Manage and troubleshoot devices. Add, delete, and edit groups and templates.
    * Manage firmware upgrades, other services, and connected client access.
    * View passwords.

You can create Custom Roles. Using a custom role, you can add one or more permissions. 

## Requirements

You must have __Tenant Admin__ permissions to manage users and organizations.

<!---## Add users --->
<h2><a name="AddUsers"></a>Add Users</h2>

1.  Click the "people icon"  on the far right of the header. Click __Access Control__.

2.  Click **Users \> Add user**.

3.  Enter a valid email address.

    * A welcome email with login and password instructions will be sent to this address.
    * If your organization uses SSO, users receive an email but are not prompted to enter a password. They will use their corporate credentials to log in instead.
4.  Select one or more Roles to define the user's access permissions. The list includes pre-defined roles and your organization's custom roles.

5.  Select **Extend Roles to Sub-tenants** to apply the same roles to any sub-organizations the user can access.

6.  Click **Add**.
7.  If the user is not present in [Cisco identity platform](https://id.cisco.com/app/bookmark/0oadg3z433OHTcCqL5d6/login), you will be required to enter additional parameters for the user, such as **First Name**, **Last Name** and **Country** / **Region**. Click **Add**.  The user will receive two emails: one to activate the Cisco identity platform account and change the password, and another to welcome and log in to IOT OD. For details on Cisco identity platform, see [Cisco SSO Login Experience](../access/sso.md)
   
      ![Authorization Process ](../graphics/intro/cs_add_new_user.png)
      
      ![Authorization Process ](../graphics/intro/cs_new_user_success.png)

>**Note**: When the user is a member of both the parent and one of the child organizations with different permissions in each, the user has access that is inclusive to both the parent and child organizations.

## Create custom roles

1.  Click the "people icon" on the far right of the header. Click __Access Control__.

2.  Click **Roles > Create Custom Role**.

3.  Enter a meaningful name, such as "EI Operator".

4.  Select a service, such as **Edge Intelligence**.

5.  Select one or more permissions available for the selected IoT OD service.

6.  Click **Save**.

## Built-in roles
Cisco IoT OD includes the following built-in roles.


### Edge Intelligence roles

* __EI Admin__ – Full access to all EI functions, including the ability to deploy or undeploy data-policies.
* __Operator__ – Can add or remove new EI Agents to the system, including:
    * Create tokens used to connect a new EI Agent to the cloud.
    * Remove an EI Agent that is disconnected from the cloud.
* __Asset Expert__ – Can manage the inbound data, including:
    * Source Data Model Definitions. For example: tell the system to fetch the upper and lower temperature data from a modbus tcp speaking fridge over 2 modbus registers.
    * Source Asset Instance Definitions. For example, define how many fridges of that type are available to fetch data from and what are their IP addresses.
    * Mapping of Source Asset Instances to EI Agents. For example, which gateways should contact which fridge (the gateway needs to be on the same floor/in the same building as the fridge to be able to reach it over the network).
* __Data Logic Developer__ – Can develop Data Logics in Visual Studio Code.

### Edge Device Manager roles

* Tenant Admin
* Device Operator

### Edge Device Manager permissions

Permissions and what actions a user can perform using those permissions are defined in the following table. You cannot create custom permissions.

|  **Permission**  |  **Description**  |
|--|--|
| Access Connected Clients | * Access any access methods within the organization in SEA<br>* Open a session in SEA or cross-launch a session to a connected client in EDM without needing to be added to a group|
|  Add Devices  | * Add devices to the inventory<br> * View list of configuration groups and templates<br> * Cannot view device inventory, hence should be used along with View Devices/Manage Devices permission<br> * Cannot view CSV upload history  |
| Configure Unused Devices  |  * View Dashboard and Device Inventory<br> * Assign or modify the configuration group for a set of devices in the Unused Inventory<br> * Edit device details (name, latitude, longitude), per device configuration parameters for one or more devices in the Unused Inventory |
| Deactivate Devices  |  * View Dashboard and Device Inventory<br> * Deactivate devices from the Inventory |
|  Delete Devices | * View Dashboard and Device Inventory<br> * Delete devices from the Inventory |
|  Manage Applications | * Applications module - view and perform all actions<br> * Cannot view EDM menu if used alone; use with another suitable permission<br> * Use with View Devices/Manage Devices permission to install applications on a list of devices<br> * Use with Manage Groups permission to install applications on a group of devices|
|  Manage Devices | * View Dashboard and Device Inventory<br> * Add devices, troubleshoot devices, and manage groups<br> * Deactivate devices, delete devices, and view CSV upload history<br> * Edit device details (name, latitude, longitude), per device configuration, and push configuration to a single device<br> * Manage connected clients for a device <br> *  Operations module - view alerts and events,  close active alerts, and view/manage alert rules<br> * Cannot view device admin password or manage notification settings  |
|  Manage Firmware Upgrades  | * View Dashboard and Device Inventory<br> *  Software module - view and perform all actions such as scheduling software update jobs, cancelling jobs, etc. |
| Manage Groups |  * View Dashboard and Device Inventory<br> * Manage templates<br> *  View, create, update, delete and manage configuration groups<br> * Push configuration to a group of devices |
|  Manage Templates |  * View Dashboard and Device Inventory<br> * View, create, update, delete and manage configuration templates |
|  Request Device Deactivation | * Request for device deactivation/deletion from the inventory<br> *  Cannot view Device Inventory; use with View Devices/Manage Devices permission |
|  Troubleshoot Devices | * View Dashboard and Device Inventory<br> * Run troubleshooting jobs on a device like ping, traceroute, show commands, reboot device, and refresh device metrics |
|  View Devices | * View Dashboard, Device Inventory, Device Summary, Monitoring, Event Log, Interfaces, Connected Clients<br> * Operations module - view alerts (active and closed) and events<br> * Operations module - close active alerts<br> * Cannot view device admin password or run device troubleshooting |
|  View Password |  * View device admin password<br> * Cannot view Device Inventory or device summary; use with View Devices/Manage Devices permission |

>**IMPORTANT**: When changing/updating the permissions, you must log out and log back in to IoT OD for the new permissions to work.

{%note info %}
**Note**: 
* When setting the **Configure Unused Devices** permission to a user, the user can assign only unused devices to a group. 
* If a device is in the **Unused** Device inventory and the user has the **Configure Unused Devices** permission set, then the user can edit the device configuration. A user with the **Configure Unused Devices** permission cannot edit a device configuration on a device in the **In Use** inventory.
{%endnote%}

### Application Manager

IoT OD's Role-based access control (RBAC), offers the following system-provided (predefined) roles for the Application Manager service:

* __Application Manager Admin(read-write)__ 
* __Application Manager User(read-only)__ 

>**Note**: For detailed information on the above roles, see [Role-based Access Control](../application_manager/role_based_access_control.md).

### Secure Equipment Access (SEA) roles

* __SEA System Admin__ – View and manage Network Devices, Connected Clients, and Access Methods.
* __SEA Access Admin__ – Launch remote sessions and manage access groups.
* __SEA User__ – Launch remote sessions.

### Industrial Asset Vision
* __Asset Vision User__ – View the dashboard, sensor catalog;  Create, edit, and delete assets; View the sensor and the network devices details; Create alert rules and view alerts; Generate and view reports; Create, update, and delete asset types.
* __IT Admin__ – View the dashboard, sensor catalog; Create, update, and delete assets; View the sensor details; View and delete network devices;  Create alert rules and view alerts; Generate and view reports; View sensor health; Add, edit, and delete integrations; View asset types details.
* __Asset Vision Installer__ – View sensor health; Add, edit, and delete assets; Onboard, view, and delete sensors; Onboard, view, and delete network devices;  View asset types details.
* __Contact Tracing User__ – View network devices details; Create alert rules and view alerts; Generate and view reports; View sensor catalog; Add, edit, and delete aliases; Add, edit, and delete badges; View collisions records.

### Industrial Wireless 
* __IW viewmode__ – View the **Inventory** and device **Summary** pages; read the configuration of each device of the selected organization.
* __IW Admin__ – View the **Inventory** and device **Summary** pages; read and edit the configuration of each device of the selected organization, push configurations updates; manage firmware upgrades of the connected devices (online mode); add devices to an organization with the list of serial numbers / MAC addresses; and download configuration file for offline mode configuration.
