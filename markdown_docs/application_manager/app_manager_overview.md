# Application Manager

## Overview
The Cisco IoT Application Manager operates as a service in Cisco IoT Operations Dashboard to install and manage Cisco IOx applications on network devices. These devices comprise externally-managed devices such as IE3x00 switches and IR routers that include IR1101, IR1800. Externally-managed devices refers to devices that are managed through CLI, Cisco Controllers, and other third-party systems. It excludes devices managed by the Edge Device Manager (EDM) service in IoT OD.

The Application Manager is a service that lets you onboard and monitor externally-managed devices. It displays the status of the devices’ network connection and the applications installed on them.

The Application Manager in IoT OD enables you to manage the IOx application life cycle. The lifecycle involves tasks such as uploading, installing and managing application(s) on a specific network device(s). This functionality is intended for Cisco branded applications only. Within the IoT OD, you can also perform tasks such as upgrading the applications, viewing event logs, uninstalling applications, and much more using the Application Manager user interface. 

![Application Manager Overview](../graphics/app_mgr/app_mgr_overview_01.PNG)

## Prerequisites

Ensure the following criteria are met before you proceed to upload applications in the IoT Application Manager. 
* The application meets the Cisco IOx requirements. See [Develop IOx applications](https://developer.cisco.com/docs/iox/#!application-development-concepts) for more information.
* Cisco IoT OD network device and its software supports Cisco IOx applications, has an activated IOx framework, the device has been onboarded, and is ready for use.
* Cisco IoT OD organization has an active Application Management feature which requires an Advantage IoT OD license.
* By default, the device operator role includes application management permissions to kick start the process.
>**Note**: You will need permission to view the **Application Management** service on the IoT OD. For details on roles and permissions, see [Role-Based Access Control](../application_manager/role_based_access_control.md).

* SD Card and its set up on the IE3x00 switch. For details, see **Prepare the Device** section, in [Device Configuration and Initiating Connection to OD](../application_manager/device_config_initiate_conn_iotod.md)
>**Note**: SD Card and it's setup procedure is not applicable for IR devices.

## Supported IE switch models and IOS-XE firmware on IoT OD
![Supported switch models](/graphics/app_mgr/am_combined_ie_switches.jpg)

>**IMPORTANT**: This feature applies to both greenfield and brownfield devices. Brownfield is defined as devices that have previously been operational in the field and greenfield devices refer to new devices added for new organizations.

## Supported IR router models and IOS-XE firmware on IoT OD
![Supported router models](/graphics/app_mgr/IR1100_1800.png)

Here are the supported IE switch models and IR router models that can enable IoT OD services on them.

| Base Product ID | Model Series Product ID (based on license)                                             | Minimum IOS XE version |
| --------------- | -------------------------------------------------------------------------------------- | ---------------------- |
| IE-3400H-8FT    | IE-3400H-8FT-E, IE-3400H-8FT-A                                                         | 17.14.1                |
| IE-3400H-16FT   | IE-3400H-16FT-E, IE-3400H-16FT-A                                                       | 17.14.1                |
| IE-3400H-24FT   | IE-3400H-24FT-E, IE-3400H-24FT-A                                                       | 17.14.1                |
| IE-3400H-8T     | IE-3400H-8FT-E, IE-3400H-8FT-A                                                         | 17.14.1                |
| IE-3400H-16T    | IE-3400H-16FT-E, IE-3400H-16FT-A                                                       | 17.14.1                |
| IE-3400H-24T    | IE-3400H-24FT-E, IE-3400H-24FT-A                                                       | 17.14.1                |
| IE-3400-8T2S    | IE-3400-8T2S-E, IE-3400-8T2S-E-RF, IE-3400-8T2S-A, IE-3400-8T2S-A-RF                   | 17.14.1                |
| IE-3400-8P2S    | IE-3400-8P2S-E, IE-3400-8P2S-E++, IE-3400-8P2S-E-RF, IE-3400-8P2S-A, IE-3400-8P2S-A-RF | 17.14.1                |
| IE-3300-8T2S    | IE-3300-8T2S-E, IE-3300-8T2S-E-RF, IE-3300-8T2S-A, IE-3300-8T2S-A-RF                   | 17.14.1                |
| IE-3300-8P2S    | IE-3300-8P2S-E, IE-3300-8P2S-E-RF, IE-3300-8P2S-A                                      | 17.14.1                |
| IE-3300-8T2X    | IE-3300-8T2X-E, IE-3300-8T2X-A                                                         | 17.14.1                |
| IE-3300-8U2X    | IE-3300-8U2X-E, IE-3300-8U2X-A                                                         | 17.14.1                |
| IE-3100-4T2S    | IE-3100-4T2S-E                                                                         | 17.14.1                |
| IE-3100-8T4S    | IE-3100-8T4S-E                                                                         | 17.14.1                |
| IE-3100-8T2C    | IE-3100-8T2C-E                                                                         | 17.14.1                |
| IE-3100-18T2C   | IE-3100-18T2C-E                                                                        | 17.14.1                |
| IE-3105-8T2C    | IE-3105-8T2C-E                                                                         | 17.14.1                |
| IE-9310-26S2C   | IE-9310-26S2C-E, IE-9310-26S2C-A, IE-9310-26S2C-E++                                    | 17.16.1                |
| IE-9320-26S2C   | IE-9320-26S2C-E, IE-9320-26S2C-A, IE-9320-26S2C-E++                                    | 17.16.1                |
| IE-9320-22S2C4X | IE-9320-22S2C4X-E, IE-9320-22S2C4X-A, IE-9320-22S2C4X++                                | 17.16.1                |
| IE-9310-16P8S4X | IE-9310-16P8S4X-E, IE-9310-16P8S4X-A, IE-9310-16P8S4XE++                               | 17.16.1                |
| IE-9320-24T4X   | IE-9320-24T4X-E, IE-9320-24T4X-A, IE-9320-24T4X-E++                                    | 17.16.1                |
| IE-9320-24P4X   | IE-9320-24P4X-E, IE-9320-24P4X-A, IE-9320-24P4X-E++                                    | 17.16.1                |
| IE-9320-16P8U4X | IE-9320-16P8U4X-E, IE-9320-16P8U4X-A, IE-9320-16P8U4XE++                               | 17.16.1                |
| IE-9320-24P4S   | IE-9320-24P4S-E, IE-9320-24P4S-A, IE-9320-24P4S-E++                                    | 17.16.1                |
| IR1100          | IR1101-K9, IR1101-A-K9                                                                 | 17.14.1                |
| IR1800          | IR1821-K9, IR1831-K9, IR1833-K9, IR1835-K9                                             | 17.14.1                |


{%note info %}
**Note**
* Only the switch models with 4 GB RAM and an SD card are supported. You can check if the switch has a 4GB RAM using the "RAM: show mem platform" command. 
* These IR routers and IE switches support the IOx framework and have the ability to host IOx applications for IoT OD **Services** (**SEA**, **EI**) and third-party IOx applications. An IoT OD user with Application Management privileges can load, deploy, troubleshoot, and remove both Cisco and third-party applications using IoT OD. IoT OD Services require service-specific privileges. For example, a user should have one of the SEA roles to use **SEA**. For details on roles and permissions, see [Role-Based Access Control](../application_manager/role_based_access_control.md).
* For complete information on each supported IE3x00 switch on IoT OD, see the suite of Cisco IE switch Data Sheets here: [IE3000 rugged switches](https://www.cisco.com/c/en/us/products/switches/industrial-ethernet-switches/catalyst-IE3000-rugged-switches.html). For Cisco IR routers, see [IR1101](https://www.cisco.com/c/en/us/products/collateral/routers/1101-industrial-integrated-services-router/datasheet-c78-741709.html) and [IR1800](https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-ir1800-rugged-series-routers/nb-06-cat-ir1800-rugged-ser-rout-ds-cte-en.html) Data sheets. 
* Check the table above for minimum IOS-XE version supported for IoT OD services. Please refer to the [Cisco Software Download page](https://software.cisco.com/download/home), search for the hardware type (for example, IE3400), download the latest IOS XE Software and apply it to the device.
{%endnote%}

**SEA**: SEA can run on supported IE3x00 or IR platforms.  SEA agent has a low demand for platform resources. SEA Plus user app is available for Windows OS only. 

**EI**:  Available on both IR routers and IE34xx switches.
