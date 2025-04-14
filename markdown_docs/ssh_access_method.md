# SSH access method

**To configure an SSH access method**:

1. From the **Services** panel, choose **Secure Equipment Access** > **System Management** > **Network Devices**. 
2. Open the **Network Device Details** screen and click on a **device name** that is listed in the Assets table to open the Asset Details page.

>**Note**: For detailed information on adding assets, see [Add Network Devices and Assets to a group](add_network_devices.md).
3. Click **Add Access Method**. 
4. Choose **SSH** from the Access Method list.
5. (Optional) Type in the **Port number** of the asset device.
6. Type in the S**ession Timeout** (In seconds). 

**Advanced Settings**: If you have enabled Advanced Settings, set these parameters

7. Select the **color scheme** used in the terminal session default is gray-black.
8. Choose the **Font Size** from the drop-down list Default: 12 pt. (Range is 10, 12, 14, 18, 24, 36 pts)
9. Set the **Scrollback**. This provides the maximum size of the terminal scrollback buffer which is limited to 1000.
10. Advanced Parameters: Provides specific information for configuring parameters. 

**Credential Details**

11. Type in a valid **username**. 
12. Type in a valid **password**.

**Access Name**: Access Name is pre-populated based on the information above, and is editable if desired. If the name already exists, it will be automatically appended with a number. for example, Access Name (2).

13. Type in the pre-populated or customized **name**.
14. (Optional) Type in a **Description**: Maximum length is 150 characters. 
15. When the access method is complete, click **Add Access Method**.
16. Return to the SEA main menu and choose **Access Management** to give users access to the remote sessions where the appropriate access method(s) reside.

![SSH Access Method](../graphics/sea/SSH_AM.png)
