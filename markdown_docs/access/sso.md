
## Cisco SSO Login Experience

IoT Operations Dashboard (OD) is integrated with [Cisco identity platform](https://id.cisco.com/app/bookmark/0oadg3z433OHTcCqL5d6/login) for an improved and seamless login experience. Cisco identity platform is an identity provider managed and used by Cisco and enables users to navigate across multiple Cisco applications and websites with one set of login credentials ensuring seamless operation. This integration of IoT OD with Cisco identity platform provides enhanced secure authentication. To set up login credentials for IoT OD, follow the steps detailed in [Add and manage user access](../access/users_tenants.md).

>**Note**: Currently, Cisco identity platform supports only authentication and does not support authorization which allows assigning user roles and permissions to the users.

* If the email used to log in to the IoT OD is associated with a Cisco identity platform account, you are redirected to Cisco identity platform for authentication. Upon successful authentication, you are redirected to IoT OD.
* If the email used to log in to the IoT Operations Dashboard is not associated with a Cisco identity platform account, nothing changes.
{%endnote%}
### IoT OD User Login Process

The diagram below depicts the authentication process for Cisco SSO Integration with IoT Operations Dashboard users.

   ![Authorization Process ](../graphics/intro/cs_auth_process_02.png)
   
   >**Note**: This functionality applies to all the existing users who have the same email credentials on both IoT OD and Cisco identity platform accounts. If you are logging in to the IoT OD for the first time, you will receive emails to activate and log in. See [Log in to the IoT Dashboard](https://developer.cisco.com/docs/iotod/log-in/).
  
1. Enter your email ID on the IoT OD login page and click **Next**. You are redirected to the Cisco identity platform page.

2. In the Cisco identity platform login page, enter your email ID and click **Next**. You will be re-directed to the multi-factor authentication (MFA) page if one has been set up for your account.

3. Upon successful verification, you will be automatically re-directed to the **IoT Operations Dashboard**.

   For details on resetting the password or managing your Cisco identity platform account, see [Login and Account Help](https://www.cisco.com/c/en/us/about/help/login account-help.html).
   For more details on Cisco identity platform login, see [Cisco identity platform User Login Process](https://www.cisco.com/c/en/us/about/help/login-account-help.html).

#### Using SSO to log in

With the single sign-on feature, you can sign in to any Cisco platform or application using existing login credentials from Cisco identity platform (if you already have an account on id.cisco.com) or your IoT OD login credentials. 

**If you have an IoT Operations Dashboard account *and* a Cisco SSO account with the *same email address*:**

1. Go to [us.ciscoiot.com](https://us.ciscoiot.com/) or [eu.ciscoiot.com](https://eu.ciscoiot.com/) (based on the geographic region).

2. Enter the email address associated with your IoT OD account and click **Next**.
 
3. You are redirected to the Cisco identity platform login page for authentication. Enter your Cisco identity platform credentials.
 
5. Upon successful authentication, you are redirected to the IoT OD and signed in automatically.
   

### Resetting Password 
 
**For IoT OD and Cisco identity platform Account Users**

This section applies to users that have both IoT OD and Cisco identity platform accounts.

For details on resetting the password or managing your Cisco identity platform account, see [Login and Account Help](https://www.cisco.com/c/en/us/about/help/login-account-help.html).

**For Vendor IdP Users**

This applies to customers using vendor IdP for authentication of users accounts. 

For details on resetting the password or managing your IdP account, check your IdP system.

### Cisco identity platform Account Deletion

In order to delete your Cisco identity platform account, you will need to ensure that your email is removed from id.cisco.com domain.

To do so, send an email to support at web-help@cisco.com and request for Cisco identity platform account profile deletion.

You will receive an email asking you to confirm your account deletion. Follow the instructions on the email.

Once your account has been deleted successfully, you will receive an email notification to confirm the same.

# Customer IDP Integration

## Overview

Single sign-on (SSO) allows users to log in using their corporate account credentials. When a user enters their Email ID, they are redirected to your organization's Identity Provider (IdP) authentication page. After authentication, they are redirected back to the IoT Operations Dashboard (IoT OD) and logged in.

{%note info %}
**Note**:
* Cisco IoT OD is the service provider (SP) and your organization's identity server is the Identity Provider (IdP).
* Your organization's identity provider must be compliant with the SAML 2.0 protocol.
{%endnote%}

### Options for authentication only, or authentication and authorization

Single sign-on can be configured in IoT OD for two use cases:

* Authentication only: Your organization's IdP authenticates the user, which logs them into IoT OD. But authorization, which provides access privileges to specific functions, is applied by Cisco IoT OD.
* Authentication and Authorization: Your organization's IdP authenticates and authorizes the user.

## Authentication only procedure

For authentication, integrate IdP into Cisco identity platform. To integrate, contact  iotod-account-request@cisco.com or use the email id provided to start the process.

## Authentication and authorization procedure

Complete the following procedure if your organization's IDP will authenticate the user's credentials, and authorize their access permissions.

### Prerequisites

1. The customer must export and share the IDP Metadata with Cisco.
2. The Cisco super admin user must import this and then share the SP metadata.
3. The customer must import the SP metadata into their identity server.
4. The Tenant Admin role must do the mapping of a role to an organization ***before*** a specified user logs in to IoT Operations Dashboard.
5. The customer must provide the SAML attribute which will contain the email id of the user. For example, the NameID or Email ID attributes.
6. Customer must send the user roles in the SAML response which will be used for authorization.
7. If user has multiple roles assigned in IDP then, all those roles must be sent as comma-separated values in SAML response.

**To enable SSO for Cisco IoT Operations Dashboard**:

1. Ask your Cisco representative to integrate the Operations Dashboard with your corporate identity provider.
2. Update the SAML response to send the roles to IoT OD. If there are multiple roles for a user, then all the roles need to be sent in different key-value pair, but not as comma-separated values under one key.
3. The Cisco support team will contact you to start the integration process:
    * The identity provider's SAML metadata and the email domain(s) must use SSO.
    * The SAML response keys which contain the following user values:
      1. Email ID (Mandatory)
      2. Role (Mandatory)
      3. First Name (Optional)
      4. Last Name (Optional)
      5. Phone Number (Optional)
    * Cisco provides the required metadata for your identity provider.
      1. Wait for Cisco and your identity provider to complete the SSO setup.
      2. After the SSO setup is complete, the tenant admin can map roles in the Access Control page of the IoT OD.
      
      ![Roles](/graphics/edge_device/sso_01.png)
      
    * Multiple IDP Roles can be mapped to one IoT OD role, but the IdP Role which has been mapped once, cannot be mapped to any other IoT OD Role.
    * If there are subtenants, the mapping is not inherited to the lower level. The Tenant Admin needs to do the mapping for subtenants.
    * The Tenant Admin needs to enter the role in the same format as the one available in IdP.
    
    
    * After the mapping is done, a user will be able to login to the application on authentication and authorization by IdP.
    * Roles and Permissions are assigned to user to access IoT OD application based on the role mapping done by the Tenant Admin.
