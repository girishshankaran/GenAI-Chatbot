# Introduction

Remote access is key for operations teams to manage and troubleshoot operational technology (OT) assets without time-consuming and costly site visits. In many organizations, machine builders, maintenance contractors, or the operations teams themselves have installed their own solutions: cellular gateways that nobody knows about or remote access software that IT is not controlling. 

With Secure Equipment Access (SEA), Cisco is solving the challenges of deploying secure remote access to operational assets at scale. It embeds the Zero Trust Network Access (ZTNA) gateway function into Cisco industrial switches and routers, making secure remote access capabilities very simple to deploy at scale. There is no point hardware solution to source, install, and manage. No complex iDMZ firewall rules to configure. Enabling remote access is just a software feature to activate in your Cisco industrial network equipment.

Managing a large number of ZTNA gateways across your operational environment is simple. Cisco Secure Equipment Access comes with a cloud portal that centralizes gateway management and configuration of remote access policies. It acts as a ZTNA trust broker, verifying users and granting access only to specific resources based on identities and contexts.

![SEA_Overview](..graphics/sea/../../../graphics/sea/SEA_Overview_00.png)

Remote personnel (employees, vendors, and contractors) connect to the Secure Equipment Access cloud portal where they are authenticated and offered access only to the devices, protocols, and time you choose.

Remote Sessions start with a default deny posture and SEA adaptively offers the appropriate trust required at the specified time. Assets are hidden from discovery making lateral movements impossible. IP addresses are never exposed in the iDMZ, which further reduces your attack surface.

Operations Administrators can easily create credentials to meet their business needs and grant access to OT assets in two different ways:

* **Clientless ZTNA**: Users need a web browser to access remote OT assets using RDP, VNC, HTTP/S, SSH, or Telnet.
* **Agent-based ZTNA (also called SEA Plus)**: SEA establishes a secure IP communication channel between the user’s computer and the OT asset, so that any desktop application can be used for advanced tasks, such as file transfer or PLC programming using native applications.

**IMPORTANT**: The SEA Service no longer recognizes the Device Operator role. To utilize SEA functionality, you must have one of the following designated SEA roles with the associated privileges:

* SEA System Admin
* SEA Access Admin
* SEA User
  

## Clientless ZTNA (SEA) solution architecture 

{%note info %}
**Note**:
* To use Clientless SEA access features, ensure the feature is activated in your Organization on IoT OD. If you don't know the status of the feature, please contact Cisco to clarify the status or activate the required feature.
* Clientless SEA requires at least SEA-E licenses. See the [SEA Ordering guide](https://salesconnect.cisco.com/IoT/s/secure-equipment-access?tabset-cadac=1) on the Cisco Sales Connect portal. {%endnote%}

![SEA_Overview](/graphics/sea/SEA_Overview.png)

## Agent-based ZTNA (SEA Plus) solution architecture

**Note**:
* To use Agent-based SEA (SEA Plus) features, ensure the feature is activated in your Organization on IoT OD. If you don't know the status of the feature, please contact Cisco to clarify the status or activate the required feature.
* Agent-based SEA requires at least SEA-E licenses. See the [SEA Ordering guide](https://salesconnect.cisco.com/IoT/s/secure-equipment-access?tabset-cadac=1) on the Cisco Sales Connect portal. {%endnote%}

Use the Secure Equipment Access Plus (SEA Plus) feature to establish a secure clear channel between your computer and a remote system through SEA cloud.

* When using the SEA Plus User App to access remote systems, you can employ TCP, UDP, and ICMP protocols for data transfer and to configure any particular port for enhanced security.
* For remote access that requires SEA Plus connectivity you must download and then launch the SEA Plus App to your local computer. See [supported access methods](/secure_equipment_access/access_methods.md) and [SEA Plus access method](/secure_equipment_access/sea_plus_access_method.md).

![SEA Plus](/graphics/sea/SEA_Plus_App_Diagram_wo_caption.PNG)

## SEA Agent

SEA is a hybrid-cloud solution that integrates cloud-based control and management (SaaS) with on-premises industrial devices. To provide remote access, an SEA Agent should be installed to a compatible industrial device. The SEA Agent is an IOx application that enables the ZTNA gateway functionality while industrial devices run as a hosting platform for the IOx applications.

Both external and internal customers can use SEA to remotely manage access and interact with both network devices and connected clients. Remote access, using the SEA agent, is used to directly access, troubleshoot, or monitor the connected clients in your deployment.

>**Note**: SEA requires SEA-E or SEA-A licenses. See [SEA Ordering guide](https://salesconnect.cisco.com/IoT/s/secure-equipment-access?tabset-cadac=1) on the Cisco Sales Connect portal.

## SEA Agent Connection States

When you open the SEA System Management page, the state of the SEA Agent Connection column is displayed. 

![SEA Deployment States](/graphics/sea/SEA_application_menu_05.png)

The table below describes the various deployment states that the SEA Agent can show.

| State  | Description |
|----------|----------------------------------|
| **Unknown**  | The connection state is unknown.    |
| **Down** | The connection state for the device is down.|
|**Up** | The connection state for the device is up. |

# Prerequisites

| Requirement  | Additional requirements |
|----------|----------------------------------|
| A supported network device (edge device)      | 1. If an IR1101 or IR1800 network device is managed by Cisco Edge Device Manager, then the network device must be onboarded in IoT OD Edge Manager Service using an eCVD template. <br>2. If a network device is managed by a customer using existing tools (CLI, scripts, Cisco Controllers), then the network device (IE3400, IE3300 (4GB RAM), IE 3100) must be onboarded in Application Manager.    |
|Network requirements for the SEA agent (application)| The SEA Agent enables SEA service and is automatically installed when a new network device is added through "Add Network Device" flow in SEA's Systems Management tab.  <br>The SEA Agent must be able to communicate with IoT OD through the uplink interface.<br>For an EDM-managed device, include the eCVD template available in EDM. <br>If the eCVD template is not used, then apply an EDM template that includes a NAT configuration to the uplink interface. In the following example, the uplink interface is at Cellular 0/1/0:<br><code>int Cellular 0/1/0</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;ip nat outside</code><br><code>&nbsp;&nbsp;ip nat inside source list NAT_ACL interface Cellular 0/1/0 overload</code>|
| Assets connected to the network device | Assets (OT Assets, such as a Robot Arm or PLC ) must have IP connectivity from the network device. 
| No prior application installed manually or in any other organization  | Currently, if there is a pre-existing SEA application when a device is onboarded to an organization, the application is listed as "Unmanaged." To allow the application to be managed by IoT Operations Dashboard, you must uninstall the unmanaged app and create a new device SEA session in this current organization. To uninstall the unmanaged application, use the **Applications** interface.  |

## Role name and permission descriptions

There are three principal roles used in SEA. Each role has permissions specific to that role. The roles with accompanying permissions and available menu options are listed here. 

| Role Name  | Permission | SEA Menu Options |
|----------|--------------|------------------|
| SEA System Admin  | * Remote System Management<br>* Remote Access Management<br>* Remote Access | * Remote Sessions: Launch remote sessions<br>* Access Management: Launch remote sessions and manage access groups<br>* System Management View and manage network devices, connected clients, and access methods |
| SEA Access Admin | * Access Management<br>* Remote Access |* Remote Access Management: Manage access groups<br>* Remote sessions: Launch remote sessions |
| SEA Access Manager  | * Access Approver<br>* Remote Access | * Approve access requests for access methods within a group<br>* Launch remote sessions |
| SEA User | * Remote Access | * Remote Sessions: Launch remote sessions |

>**Note**: Roles and permissions are the same for SEA and SEA Plus.


