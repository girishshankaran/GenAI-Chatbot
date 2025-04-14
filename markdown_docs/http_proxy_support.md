# SEA: HTTP(S) proxy support

This feature allows for customer-controlled proxy sessions that provides more flexibility while maintaining the strict security capabilities used by SEA. 

{%note info %}
**Note**:
* The HTTP(S) proxy feature is specifically for customers installing IE3x00 switches.
* The proxy configuration is specifically for the SEA application.
* IDA version 17.14.1 or above is required for device communication through the proxy.{%endnote%}

## Configure SEA Agent for proxy support

1. In **Secure Equipment Access**, choose **System Management > Network Devices**.

2. Click **Add Network Device**. 

3. Use the **Select from list (recommended)** option and choose the **Network Device** that you want to add.

![Add Network Device](graphics/sea/../../../graphics/sea/SEA_New_Proxy_Connect_00a.png)

4. Click **Next** to open the **Network Device Details** screen.

![Add_Device_1](../graphics/sea/SEA_New_Proxy_Connect_02.png)

5. Enable the **HTTP Connect Proxy switch** to open proxy settings.
6. Choose either **Proxy URL** (default setting) or **Proxy Form** and enter the proxy configuration. Choose the **option** and enter the information that fits your needs. 

>**Note**: Proxy Form and Proxy URL have the exact same purpose, they provide different ways of the entering the same information and you can pick the one that is most convenient for you.

![Add_Device_2](../graphics/sea/SEA_New_Proxy_Connect_03.png)

## Configure a network device for proxy URL
1. Enter the **URL** for the device using this format: **http(s)://username:password@server:port**.

![Proxy URL](../graphics/sea/Proxy_Connect_URL_01.png)

2. Click **Add Network Device** located in the bottom right corner of the screen. You are notified that the device is successfully added.

>**Note**: If the configuration fails, the reason is posted on a banner at the top of the screen.

## Configure a network device for Proxy Form (HTTP Proxy support)
1. Depending on your requirements, choose either **http://** or **https://** from the drop-down list.
2. Enter the **Server IP address**.
3. Enter the **Port number**.
4. (Optional) Enter the **Username** and **Password**.
5. Click **Add Network Device** located in the bottom right corner of the screen. You are notified that the device is successfully added.

>**Note**: If the configuration fails, the reason is posted on a banner at the top of the screen.

![Proxy Form](../graphics/sea/Proxy_Connect_Proxy_form_02b.png)

## Modify an existing network device proxy setting
1. In **Secure Equipment Access**, choose **System Management**.
2. Click **Network Devices**. 
3. Choose the **Device name** to be modified.

![Modify_Proxy](../graphics/sea/SEA_New_Proxy_Connect_04a_update.png)

4. In the **Network Device Details** screen, click **View Details** to modify the proxy information.

![Edit Configuration](../graphics/sea/SEA_New_Proxy_Connect_05a_update_details.png)

5. In the **Additional Configuration** panel, click **Edit Configuration**.

>**Note**: Clicking **SHOW**, shows the configuration information as text, clicking **HIDE** masks the information behind asterisks.

6. Edit the **appropriate information** for the network device.

>**Note**: To disable a HTTP proxy configuration, click the **HTTP Connect Proxy switch**. Then continue to **Step 7**. 

7. Click **Apply and Reinstall**.
8. Click **Reinstall** in the reinstall app confirmation prompt. Depending on the network, the reinstallation process can take several minutes.

## Modify an existing network device with no proxy configuration
1. In **SEA Service**, choose **Secure Equipment Access** > **System Management > Network Devices**. 
2. Choose the **Device name** that does not have a configured proxy setting. 

![Modify Existing Device](../graphics/sea/SEA_New_Proxy_Connect_09b_update_proxy_settings.png)

3. In the **Additional Configuration** section of the **Network Device details** screen, click **Edit**.

>**Note**: If the network device does have an existing proxy, follow the steps in: To modify an existing network device proxy setting.

![Edit to Configure](../graphics/sea/SEA_New_Proxy_Connect_010b_update_proxy_settings.png)

4. Click the **HTTP Connect Proxy switch**.
5. Depending on your network requirements, enter either the information for configuring a **Proxy URL** or **Proxy Form**. 
6. After you have entered all the information, click **Apply and Reinstall**.
7. Click **Reinstall** in the reinstall app confirmation prompt. Depending on the network, the reinstallation process can take several minutes.
