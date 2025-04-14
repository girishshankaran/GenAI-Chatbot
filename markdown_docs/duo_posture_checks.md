# Duo user security posture checks
In regular day-to-day activities, any user's PC can be used for multiple purposes, such as storing and accessing files, folders, programs, etc. Without strong security management, malicious external parties can access confidential or process-sensitive information on that user's computer, furthermore, a low-security posture can allow third parties access through that computer and a remote access solution to assets on remote sites can be jeopardized. Additionally, Operational Technology (OT) programs (for PLC, HMI, robots, etc.) can be accessed and copied without authorization. Utilizing Duo integration allows you to conduct a system posture check on a user's device before allowing access from the device to a remote OT Asset using the SEA Plus access method. 

## Duo integration with SEA Plus

{%note info %}
**Prerequisite**: The SEA System Admin, who sets up the external integration, must have a Duo Admin account with a unique URL. Or, the SEA System Admin can work with a dedicated Duo administrator to capture Duo credentials for integration with IoT OD. It is necessary to create appropriate policies on Duo for the user’s computer security posture check for remote access to OT assets. You can request a free, 30-day trial that works with IoT OD. Click [Duo.com](https://duo.com/trial) to request a 30-day trial.{%endnote%} 

## Introduction

The integration between Duo and SEA Plus has two steps:

1. Creating the SEA Plus application in Duo
2. Adding the Duo client ID and secret to SEA 

From the **Remote Sessions** screen, click the **SEA Plus** toggle switch to activate SEA Plus. If you have an active Duo integration configured when you launch SEA Plus, Duo performs a system posture check to ensure that the system complies with Duo's security policies defined for this use case by the Duo Administrator. If the user's computer passes Duo's posture check criteria, then the Duo logo turns green and activates SEA Plus connectivity. For more information on using the SEA Plus access method, refer to [SEA Plus access method](/secure_equipment_access/sea_plus_access_method.md) documentation.

![Successful Activation](../graphics/sea/SEA_monitor_00b.png)

>**Note**: If the security posture check fails, you receive an error message. 

![DUO Error Notice](../graphics/sea/SEA_monitor_duo_online_01.png)

To view **Details** of the Duo session, click **SEA Plus Details**. The **details panel** opens on the right side of the screen.

![Duo_Details](../graphics/sea/SEA_monitor_duo_online_details_02.png)

>**Note**: If Duo integration is not enabled on your system then Duo logo remains grayed out. You can still enable **SEA Plus** and access **SEA Plus sessions**. However, your computer security posture check won't be initiated.

## Configure Duo external integration for SEA Plus

{%note info %}
**Note**:
* To configure Duo external integrations, you must have an SEA System Admin role.
* This Duo integration only applies to the SEA Plus access method. The Duo integration does not apply to user login. If you need to use Duo during IoT OD login, a separate integration must be configured with an Identity provider and Single Sign On (SSO) must be enabled. {%endnote%}

## Create the SEA Plus (Web SDK) application in Duo

1. From the left menu of your Duo Admin account (Duo Admin Login), navigate to **Applications > Protect an Application**.
2. In the Protect an Application screen, choose **Web SDK** option and click **Protect**.

![Application Protect](/graphics/sea/SEA_Duo_03.png)

3. We recommend you change the name from **Web SDK** to something more meaningful like **SEA Plus**.
    1. In the Duo Admin Dashboard navigate to **Applications > Web SDK**.
    2. Scroll down to **Settings** section, change the **Name**.
    3. Scroll to the bottom of the page to **Save**.
      
![Settings](/graphics/sea/SEA_Duo_04.png)

## Configure SEA Plus policy in Duo

>**Note**: The example is used to understand available options and simplify the initial stage of Duo configuration. We highly recommend you become familiar with Duo policy documentation to fit to your requirements. For more information, see [Duo Administration: Policy & Control](https://duo.com/docs/policy).

1. In Duo, from the menu, choose **Policies**.

![Policies screen](/graphics/sea/SEA_Duo_08a.png)

2. Scroll down to the **Custom Policies** section at the bottom of the section and click **New Policy**.

![New Policy](/graphics/sea/SEA_Duo_010a.png)

3.  Type in an appropriate policy **Name**.
4.  Remaining in the Policy section, configure the policy elements located at the left of the Policy section, that apply to SEA Plus users. For example:
    1. Click **Authentication Policy** and choose **Enforce 2FA**.
    >**Note**: Although we choose **Enforce 2FA**, we will disable it later in the policy. This setting is enabled to force a user to undergo device posture checks.
    ![Enforce 2FA](/graphics/sea/SEA_Duo_09a.png)
    2. Click **User location** and choose the countries to which remote access should be enabled and choose **No action** from the dropdown for the chosen countries. For All other countries, choose **Deny Access**.      
![User Location](/graphics/sea/SEA_Duo_09.png)
    3. Click **Device Health Application**.    
{%note info %}
    **Note**:
    * The default screen lists both macOS and Windows in reporting status. Under **Windows**, click **Require users to have the app** and at a minimum require a **firewall** and a **system password**.
    * We highly recommended you **block access if an endpoint security agent is not running** (not shown in the screen).{%endnote%}
    ![Device Health application](/graphics/sea/SEA_Duo_010d.png)  
    4. Click **Operating Systems** and uncheck all boxes except for **Allow Windows devices** located at the bottom of the screen.
    >**Note**: SEA Plus is only supported on Windows. Any authentication attempts that are not Windows is suspicious behavior.
    ![Allow Windows](/graphics/sea/SEA_Duo_011.png)
    5. Scroll down in the Policy section and choose **Networks > Authorized networks**. In the **Allow access without 2FA from these networks field** enter **0.0.0.0-255.255.255.255**. This addresss covers every possible network and ensures that nobody undergoes additional 2FA checks. 
    >**Note**: Choosing this option disables 2FA for SEA Plus. We disable 2FA for SEA Plus because you have already undergone the identify verification when you logged into IoT OD. This action eliminates unnecessary 2FA checks.
    ![Authorized Networks](/graphics/sea/SEA_Duo_012.png)
    6. Click **Save Policy**.
5. In Duo, navigate to **Applications** menu and scroll down to choose the **Web SDK application** you created to protect SEA Plus.
6. Navigate to the Policy section and click **Apply a policy to all users**.
![Apply Users](/graphics/sea/SEA_Duo_013.png)
7. Choose the newly created **Policy** (SEA Plus) from the drop-down menu.

![Apply_Policy](/graphics/sea/SEA_Duo_014.png)

8. Click **Apply Policy**.
9. Scroll to the bottom of the page and click **Save**.
    
## Enable Duo integration in SEA

Open IoT OD in a separate page so that both Duo and SEA can be open at the same time. Then continue with Enable Duo Integration in SEA step 1.

>**Note**: You must have SEA System Admin role privileges.

1. In IoT OD navigate to **Secure Equipment Access** and choose **System Management > External Integrations** tab.

![Add External Integration](../graphics/sea/SEA_Duo_element_03.png)
2. Click **Add External Integration** to open the Add External Integration panel.

3. Choose **Duo** from the Integration Type drop-down list.

![Select Duo](/graphics/sea/SEA_Duo_06.png)

4. Type in an appropriate **Name**. 
5. (Optional) Type in a relevant **Description**.
>**Note**: Switch back to Duo and in **Applications > Details** to retrieve the Client ID, Client secret, and API hostname. Beside each field, click Copy (the lettering switches to Copied), then switch to back SEA and perform a paste on the appropriate field. 

6. (Required) Enter the **Duo Account Settings** from the SEA Plus application created in Duo:
   1. Paste the **Client ID** (Alphanumeric Duo application key).
   2. Paste the **Client Secret** (Alphanumeric Duo application password key).
   3. Paste the **API Host** (API server that is validating the login request).

![Duo Parameters](/graphics/sea/SEA_Duo_07c.png)
7. When finished, click **Add Integration** (bottom right). The Enable External Integration prompt opens stating that enabling the new integration record will disable any previously enabled Duo Integration. With the Duo integration enabled, you can now activate SEA Plus with the integrated Duo posture check.
>**Note**: SEA allows only one active integration type (for example, Duo) at a time.

![Enable Ext Integration](/graphics/sea/SEA_Duo_08.png)
>**IMPORTANT**: The external integration for Duo allows adding multiple Duo accounts to SEA Plus, for example, for troubleshooting purposes. But only one Duo account can be chosen as Active in SEA Plus at any moment. 

## Verify SEA Plus and Duo are integrated

1. In IoT OD, from the left pane, click **Secure Equipment Access > System Management**.
2. Click the **External Management** tab.
3. Verify that the Duo integration is **Active**.
![Verify](../graphics/sea/SEA_Duo_element_04.png)
