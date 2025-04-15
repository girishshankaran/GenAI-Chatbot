<!--# Set up IoT Operations Dashboard (IoT OD)-->
<h1><a name="SetupIoTOperationsDashboard"></a>Set up IoT Operations Dashboard (IoT OD)</h1>

{%note info %}
**Note**: 
* In the onboarding process: This procedure comes after [Firewall Rules: Device and network requirements](../edge_manager/requirements.md).
* This procedure is applicable for EDM-managed devices only. 
{%endnote%}

As an administrator, complete the following procedures to set up IoT OD software.

__Before you begin__

* Create a [Cisco Smart Account](https://software.cisco.com/software/csws/smartaccount/accountCreation/createSmartAccount), and note your Smart Account credentials and the Virtual Account.
* For EDM-managed IR1101 and IR1800s, you must use Smart Account for PnP redirect. Additionally, Smart Account can help set up auto-population of purchased IR1101 and IR1800s devices from manufacturing to the IoT OD Organization. If you don't have it, please create a Cisco Smart Account. Note your Smart Account credentials and the Virtual Account.

__Procedure__
1. Enter the URL in a supported web browser:
    * In the US use https://us.ciscoiot.com/
    * In the EU use https://eu.ciscoiot.com/
2. Check your email for a Welcome message and click the link to get started.
3. The IoT OD web page opens by default. To enable additional services, such as Secure Equipment Access (SEA), send an email request to iotod-account-request@cisco.com.

![IoT OD Login Page](/graphics/sea/22856_sea_login_00.png)

>__Note:__ The eCVD templates that provide pre-defined network configurations are not automatically added to the cloud when a new Organization is created. To enable eCVDs, send an email request to iotod-account-request@cisco.com.

## For new customers who have not received an account verification email

Complete the steps for requesting an organization.

The **Request an Organization** link located on the right side of the screen above the **email address** field. This link takes you to the Setup page and is for customers who have:

* Purchased an account, but who have not received an confirmation email from CCW.
* Customers who have not purchased a service, but want a new Organization for trial or demonstration.

Click the **Request an Organization** link to open the [Setup up IoT Operations Dashboard](../access/new_org.md) page where you use iotod-account-request@cisco.com to request to create and have access to an organization.

### Information needed for those customers that have not received a verification email

* **Company Name and location**
* **Purchase Order Number**
* **Service(s) purchased**
* **Admin Manager Name and Email**
* **Account Manager**

### Information needed for internal customers or partners who want to set up a POC

* **Customer name and Location** (city/state/country)
* **Customer market segment** (example: Public Sector)
* **Desired IoT OD organization name** (for IoT OD organization tenant name)
* **IoT OD organization admin name and email address** (adminname@provider.com)
* **Do you need SEA/Application Management features** (yes/no)
* **Primary reason for requesting an IoT OD**
* **Service(s) purchased** (SEA, EI, etc.)
* **AM/PSS/TSA names** (first and last name)
* **New Solution** (yes/no)

# Next step
To continue device(s) onboarding, go to [Get Started with Operations Dashboard](../overview_iot/get_started.md).

