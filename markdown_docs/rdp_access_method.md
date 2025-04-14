# RDP access method

**To configure an RDP access method**:

1. From the **Services** panel, choose **Secure Equipment Access** > **System Management** > **Network Devices**. 
2. Open the **Network Device Details** screen and click a **device name** that is listed in the Assets table to open the Asset Details screen. 
  
>**Note**: For detailed information on adding Assets, see [Add Network Devices and Assets to a group](add_network_devices.md).
 
3. Click **Add Access Method**. 
4. Choose **RDP** from the Access Method list.
5. (Optional) Enter a **Port number** of the client device.
6. (Optional) Enter a **Session Timeout** (in seconds).
7. Choose a **Security Mode**. Choose one of the three options, **Any**, **NLA**, or **RDP** to set up your authorization.

**Advanced Settings**: Complete the advanced setting based on the Access Method choose.

1. Choose a **Domain** associated with the device.
2.  Choose a **Color Depth**. Choose either:  8, 16, 24, or 32 bits per pixel.
3.  Choose a **Resize Method**: There are two options:
* **Display-update**: This option uses the channel added with RDP 8.1 to signal the server when the client display size has changed.
* **Reconnect**: Use this option if the client display size changes and you want the RDP session to automatically disconnect and then reconnect with the new display size.
1.  **Advanced Parameters**: You can enter Advance Parameters  that provides specific information for configuring parameters.  This table describes the parameters that can be used with the RDP access method.

  |Parameter Name | Description |
  |-------------- | ----------- |
  | width  | This optional parameter lists the width of the display in pixels.  If this value is not specified, the width of the connecting client display is used, for example 1000 pixels.|
  | height | This optional parameter lists the height of the display in pixels. If this value is not specified, the height of the connecting client display is used, for example 800 pixels. |
  | server<br>layout | This parameter only covers the RDP server-side keyboard layout. <br><br> **Note**: The RDP protocol is not independent of keyboard layout, and needs to "know" the keyboard layout of the server to send the proper keys when a user is typing.<br><br>Possible values are:<br>* en-us-qwerty<br>English (US) keyboard<br>* de-de-qwertz<br>German keyboard (qwertz)<br>* fr-fr-azerty<br>French keyboard azerty<br>failsafe<br>* Unknown keyboard - this option sends only Unicode events and should work for any keyboard, though not necessarily all RDP servers or applications.<br><br> **Note**: If your server's keyboard layout is not yet supported, this option should work in the meantime. 
  | ignore-cert | Setting this parameter to true, enables server to ignore the returned certificate even if that certificate cannot be validated. This parameter is useful if you trust the server and your connection to the server, and the server's certificate cannot be validated.|
  | disable-auth | Setting this parameter to true disables authentication while connecting to the server.<br><br>Any authentication enforced by the server over the remote desktop session (such as a login dialog) will still takes place. By default, authentication is enabled and only used when requested by the server.<br><br> **Note**: If you are using NLA, authentication must be enabled by definition.|


**Credential Details**

13.  Type in a valid **Username**.
14.  Type in a valid **Password**.

{%note info %}
**Note**:
* During your initial configuration: Enter both a username and password.
* For higher security: If you leave the credential fields blank, then IoT OD opens a popup window that requires writing credentials by the user to access the remote windows system.{%endnote%}

**Access Name**: Access Name is pre-populated based on the information above, and is editable if desired. If the name already exists, it will be automatically appended with a number, for example, Access Name (2).

15.  Type in a pre-populated or customized **Name**.
16. (Optional) Type in a **Description**. Maximum length is 150 characters.
17. When the access method is complete, click **Add Access Method**.
18. Return to the SEA main menu and choose **Access Management** to give users access to the remote sessions where the appropriate access method(s) reside. 

![RDP Access Method](../graphics/sea/RDP_AM.png)
