# Access Methods

SEA provides a variety of access methods (see Group A & B) to configure SEA connected clients.

The SEA feature incorporates two groups of access methods:

**Group A**: Is a clientless approach when a user can use a supported web-browser and these access methods to communicate with remote hosts and applications.
* SSH
* RDP
* VNC
* Web App 
* Telnet

**Group B**: Is a client-based approach where a user  installs an application on the local drive, SEA Plus App downloaded from the UI, to establish a clear communication channel with a remote system.
* SEA Plus: The SEA Plus application runs as a lightweight VPN-client and helps to establish a secure communication a channel between the user’s computer and remote system.

>**Note**: You can configure an access method for an asset using the Quick Wizard. See the [Quick Wizard](../secure_equipment_access/sea_quick_wizard.md) for configuring an access method.

## General access method for the SEA Assets

After you create a Network Device and Asset, configure the access method for that client.

You can also configure External Equipment Management to access devices, such as a Camera Management server that can be used to configure connected cameras. See the External Equipment Management section of each access method template.

1. From the **Asset Details** screen, choose the **asset name** that for the access method.
2. Click **Add Access Method**. The Add Access Method screen opens showing the **Asset Details** and **Access Method Details** sections.

![General AM Instructions](/graphics/sea/AM_Main_Screen_04_composite.png)

3. In the **Add Access Method** screen, choose an **Access Method** from the drop-down list.
4. Fill in or choose the **information appropriate to each access method** listed in the next section.

See each specific method for detailed configuration information.

## SEA Access methods

[**SSH**](ssh_access_method.md)

SSH (Secure Shell Protocol) is a remote administration protocol that allows users to access, control, and modify their remote servers over the internet.

SSH service was created as a secure replacement for the unencrypted Telnet access method and uses cryptographic techniques to ensure that all communication to and from the remote server is an encrypted manner. It provides a mechanism for authenticating a remote user, transferring inputs from the client to the host, and relaying the output back to the client. Use SSH as a secure access method to a command line interface (CLI) on a remote system.

[**RDP**](rdp_access_method.md)

RDP (Microsoft Remote Desktop Protocol) provides remote display and input capabilities over network connections for Windows-based applications running on a server.
* During your initial configuration: Enter both a username and password.
* For higher security: If you leave the credential fields blank, then IoT OD opens a popup window that requires writing credentials by the user to access the remote Windows system. 

[**VNC**](vnc_access_method.md)

VNC (Virtual Network Computing) is a cross-platform, screen-sharing system that was created to control another computer remotely. VNC works across multiple operating systems. The default port is 5900.
* During your initial configuration: Enter a password.
* For higher security: If you leave the password field blank, then IoT OD opens a popup window that requires entering the password by the user to access a remote system.

[**Web App**](web_app_access_method.md)

A web application (or web app) is an application software that runs on a web server. The user accesses web applications through a web browser with an active network connection.

A web server is computer software and the underlying hardware that accepts requests and sends responses through HTTP or its secure variant, HTTPS. HTTP/S are the network protocols created to distribute web content (web pages, etc.) to clients.

[**Telnet**](telnet_access_method.md)

A Telnet session for the device is used to virtually access a computer and provides a two-way, collaborative, and text-based communication channel between two machines. It follows a user command Transmission Control Protocol/Internet Protocol (TCP/IP) networking protocol for creating remote sessions. A username and password are not required, but you must specify the port number.

[**SEA Plus**](sea_plus_access_method.md)

{%note info %}
**IMPORTANT:**
* The current SEA Plus App release **ONLY provides support for Windows 10 and above OS SEA Plus app versions**. 
* If you have VPN clients installed on your computer, only use the SEA Plus App **without** any other VPN client in active mode.
* **Make sure that your virus scanner (antivirus) does not block the SEA Plus application.**
{%endnote%}

The SEA Plus App access method allows remote access using IP-based protocols with a TCP, UDP, or ICMP header. You can transfer files to or from a remote system through the SEA Plus channel. Access by SEA Plus App requires a particular user application (SEA Plus App) that runs on the **Microsoft Windows 10** platform and is installed on your computer. The SEA Plus application runs as a lightweight VPN-client and helps to establish a secure communication channel between the user’s computer and a remote system. 

{%note info %}
**Note**:
* To use SEA Plus features, ensure the feature is activated in your Organization on IoT OD. If you don't know the status of the feature, email [iotod-account-request@cisco.com](mailto:iotod-account-request@cisco.com) to clarify the status or activate the required feature.
* The SEA Plus features are premium features and require an Advantage license on IoT OD.
{%endnote%}
