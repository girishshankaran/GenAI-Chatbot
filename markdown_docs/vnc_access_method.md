# VNC access method

{%note info %}
**IMPORTANT**:

* Please check virtual network computing (VNC) vendor-specific documentation for VNC server configuration to allow non-vendor specific VNC Viewer access.
* VNC access method  is implemented using RFC6143 that supports only VNC password authentication. VNC servers must be configured to use VNC password authentication to work with the VNC access method. If you choose to use an alternative security configuration (such as username/password), you can use SEA Plus in combination with a local VNC client.{%endnote%}

**To configure the VNC access method**:

1. From the **Services** panel, choose **Secure Equipment Access > System Management > Network Devices**. 
2. Open the **Network Device Details** screen and click a **device name** that is listed in the Assetss table to open the **Asset Details** screen. 
 
>**Note**: For detailed information on adding Assets, see [Add Network Devices and Assets to a group](add_network_devices.md).

3. Click **Add Access Method**. 
4. Choose **VNC** from the Access Method list.
5. (Optional) Enter a **Port**. Enter the port number of the client device. If no value is entered, the default VNC port is 5900.
6. (Optional) Enter a **Session Timeout** in seconds. If no value is entered, the default session timeout is 180 seconds.

**Advanced Settings**: If this setting is enabled, complete the following parameters.

7. (Optional) **Read Only Access**: If this setting is enabled, the user cannot make any modifications to the access method.
8. **Color Depth**: Choose either  8, 16, 24, or 32 bits per pixel. Default is 32.
9. **Clipboard Encoding**: Choose one of the four options, ISO0508859-1, UTF-8, UTF-16, or CP1252.

**Credential Details**

10. (Optional)**Password**: Enter a valid password.

{%note info %}
**Note**:
* **During your initial configuration**: Enter a password.
* **For higher security**: If you leave the password field blank, then IoT OD opens a popup window that requires entering the password by the user to access a remote system.{%endnote%}

**Access Name**: Access Name is pre-populated based on the information above and is editable, if desired. If the name already exists, it will be automatically appended with a number. For example, Access Name (2).

11. Type in a **Name**: The pre-populated or customized name.
12. (Optional) Type in a **Description**: Maximum length is 150 characters. 

13. When the access method is complete, click **Add Access Method**. 

14. Return to the SEA main menu and choose **Access Management** to give users access to the remote sessions where the appropriate access method(s) reside.  

![VCN](../graphics/sea/VNC_AM.png)
