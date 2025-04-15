# Role-Based Access Control

## Prerequisite  
For details on procuring access or adding users to gain access on IoT OD, refer to [Add and Manage User Access](../access/users_tenants.md).

## Overview
Role-based access control (RBAC) is a security control intended to segregate the ability for users to access and interact at different levels with various resources in a system. RBAC enables an administrator (admin) to efficiently manage system-provided (predefined) roles or create customized (custom) roles. By combining read-only and/or read-write permissions, the admin can tailor these roles to match the user's requirements in IoT OD's Application Manager. 

IoT OD's Role-based access control, offers the following system-provided (predefined) roles for the Application Manager:
* **App Manager Admin** (read-write)
* **App Manager User** (read-only)

The system-provided roles can simplify the initial stage of using the App Manager and help manage the service's basic security posture.

Besides the system-provided roles, IoT OD's RBAC has extensive capabilities to create custom roles. The following tables provide available read-only and read-write permissions that can be used for custom role creation. The permissions are aggregated into buckets that reflect the structure of the App Manager to help with the process of custom role creation.

## Permissions for Applications management (App Manager only)

| User Interface                     | Permissions type       |Permissions|
| ---------------------------------- | ---------------------- |-----|
| Application Manager > Applications | Read-only permissions  |* View list of applications<br>* View application Instances<br>* View Application details<br>* View App Instance details and additional information such as viewing App Logs, IP Configuration, and Resource usage<br>* Perform device-level actions such as Device refresh, Download Tech support logs|
| Application Manager > Applications | Read-write permissions |* View list of Applications<br>* View Application Instances<br>* View Application details<br>* View App Instance details and additional information (View App Logs, View IP Configuration, View Resource Usage)<br>* Perform Device level actions (Device Refresh, Download Tech support logs)<br>* Add Application<br>* Install Application<br>* Delete Application<br>* Change Application configuration<br>* Perform App level actions (Start/Stop/Uninstall/Change version)|

## Permissions for Device Inventory (App Manager only)

| User Interface   |   Devices        | Permissions type       |Permissions|
| -----------------|----------------- | ---------------------- |-----|
|Application Manager > Devices|Registered|Read-only permissions|* View list of externally-managed devices in **Registered** table<br>* View device details, Event Log, Troubleshooting or Health Check tabs |
|Application Manager > Devices|Registered|Read-write permissions|* View list of externally-managed devices in **Registered** table<br>* View device details, Event Log, Troubleshooting or Health Check tabs<br>* Deactivate externally-managed devices<br>* Edit device details<br>* Run troubleshooting commands |
|Application Manager > Devices|Staged|Read-only permissions|* View externally-managed devices in **Staged** tab<br>* View device details and Event Log tabs<br>* View CSV upload history |
|Application Manager > Devices|Staged|Read-write permissions|* View externally-managed devices in **Staged** tab<br>* View device details and Event Log tabs<br>* View CSV upload history<br>* Download CSV template for bulk device onboarding<br>* Add externally-managed devices (through single or multiple flows)<br>* Edit device details<br>* Delete devices |

## Permissions for Device Profiles (App Manager only)

| User Interface                     | Permissions type       |Permissions|
| ---------------------------------- | ---------------------- |-----|
| Application Manager > Device Profiles|Read-only permissions|* View list of all Device Profiles<br>* View Device Profile details|
| Application Manager > Device Profiles|Read-write permissions|* View list of all Device Profiles<br>* View Device Profile details<br>* Create Device Profiles<br>* Edit Device Profiles<br>* Delete Device Profiles|
