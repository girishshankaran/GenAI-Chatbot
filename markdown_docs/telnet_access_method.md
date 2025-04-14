# Telnet access method

To configure an Telnet access method:

1. From the **Services** panel, choose **Secure Equipment Access** > **System Management** > **Network Devices**. 
2. Open the **Network Device Details** screen and click on a **device name** that is listed in the Assets table to open the Asset Details page. 
 
>**Note**: For detailed information on adding Assets, see [Add Network Devices and Assets to a group](add_network_devices.md).

3. Click **Add Access Method**. 
4. Choose **Telnet** from the Access Method list.
5. Type in **port number** of the asset device.
6.  (Optional) Type in the **session timeout** in seconds.

**Advanced Settings**: Complete the advanced setting based on the Access Method chosen.

7. **Color Scheme**: The color scheme used in the terminal session default is gray-black.
8. **Font Size**: Choose the size from the drop-down list. The default is 12 pt. (The range is: 10, 12, 14, 18, 24, 36 pts.)
9. **Scrollback**: Provides the maximum size of the limit for the terminal scrollback buffer limit. The default value is 1000.
10. **Advanced Parameters**: Provides extra information on the access method.

**Credential Details**

**Note:** Sending credentials to Cisco devices is not supported for security purposes.

11. Type in a valid **username**.
12. Type in a valid **password**. 

**Access Name**: Access Name is pre-populated based on the information above and is editable, if desired. If the name already exists,
it will be automatically appended with a number. For example, Access Name (2).

13. **Name**: The pre-populated or customized name.
14. **Description**: Maximum character limit is 150.

15. When the access method is complete, click **Add Access Method**.

16. Return to the SEA main menu and choose **Access Management** to give users access to the remote sessions where the appropriate access method(s) reside.

![Telnet Access Method](../graphics/sea/Telnet_AM.png)
