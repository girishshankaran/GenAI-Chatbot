# Web App access method

The SEA Web App access method allows users to connect to a web server running on the asset.

## **Configure the Web App access method**

>**Note**: There can be situations where using the Web App access method has limitations. For example, if a website is implemented using redirect from the website's URL to a static IP address the redirect does not work properly or if the website uses websockets in its implementation. If there is any question in using Web App as an access method, it's recommended to use SEA Plus as an alternative access method.  

1. From the **Services** panel, choose **Secure Equipment Access** > **System Management** > **Network Devices**. 
2. Open the **Network Device Details** screen and click on a **device name** that is listed in the Assets table to open the Asset Details page. 
 
>**Note**: For detailed information on adding Assets, see [Add Network Devices and Assets to a group](add_network_devices.md).
 
3. Click **Add Access Method**. 
4. From the panel, choose **Web App** from the drop-down list.
5. Enter the **Full URL**. (For example: **https://1.1.1.1/example/path**)
>**Note**: Since the connection between the SEA Agent and the web server occurs within the secure, protected local network, the SEA Agent skips the validation of the web server’s certificate during https connection initiation. This simplifies connections to web servers using self-signed certificates, eliminating the need for additional certificate management.
6. Enter the **Session Timeout**

{%note info %}
**Note**: 
* The timeout default is **180 seconds**. The full range is **60-7200 seconds**.
* Timeout is extended based on network activity, such as, a request to the server or Websocket communication. {%endnote%}

### Advanced Settings (Optional)

* If advanced parameters are required  for this access method, enter them in the following format: **parameter 1 name**: value, **parameter 2 name**: value, etc.
   
 **Access Name**: Access Name is pre-populated based on the information above and is editable, if desired. If the name already exists, it will be automatically appended with a number. For example, Access Name (2).

 7. Type in a pre-populated or customized **name**. 
 8. (Optional) Type in a **Description**. Max character limit is 150. 
 9. When the access method is complete, click **Add Access Method**.
 10. Return to the SEA main menu and choose **Access Management** to give users access to the remote sessions where the appropriate access method(s) reside. 

![Web App Access Method](../graphics/sea/Web_App_AMa.png)
