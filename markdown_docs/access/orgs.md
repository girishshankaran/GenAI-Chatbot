# Create sub-organizations

## Introduction

Your organization's account is also called an "organization." All configurations and data are available to the users in this organization based on the user roles for their account. You can optionally create additional sub-organizations to organize your users into groups that have access to different devices, data, features and services. For example, if your organization has multiple locations, you can optionally create sub-organizations for "Campus A" and "Campus B" to segregate users and/or data.

>__Note__: Edge Intelligence admins are not expected to create or use sub-organizations since sub-organizations data will not be aggregated into the main organization data. Create all users and EI configurations in the main organization created by Cisco. If sub-organizations are used, understand that all gateways, assets, destinations and data will be managed separately in each organization. Consult your Cisco support representative before using sub-organizations to understand the implications.

## Create a sub-organization

You can create sub-organizations for an existing organization.

>__Note__: Not recommended for use with Edge Intelligence. EI is not automatically enabled on new sub-organizations. Contact your Cisco representative for assistance.

1.  Click the "people icon"  in the far right of the header. Click __Access Control__.

2.  Click the __Organizations__ tab.

3.  To create a sub-organization for the current org (where you are logged in), click __Add Organization__.<br>Or, to add a sub-org under an existing sub-organization, under the Actions column, click More ![...](/graphics/intro/ellipsis.png) and then __Add Organization__.

4.  Enter the organization details:

      1. Enter a meaningful name for the organization.

      2. Enter the email address of the organization admins. Separate entries with a comma (,).

      3. Select the Cisco IoT OD services that can be accessed by users in that organization.

      4. Click __Add__.
      
         If the admin is not a [Cisco identity platform](https://id.cisco.com/app/bookmark/0oadg3z433OHTcCqL5d6/login) user, you will be required to enter additional parameters such as the **First Name**, **Last Name** and **Country** / **Region**, then click **Add**. For details on Cisco identity platform, see [Cisco SSO Login Experience](../access/sso.md)
         The user will receive two emails: one to activate the Cisco identity platform account and change the password, and another to welcome and log in to IOT OD. 

## Organization status

An organization's status tells you if it is ready for use.

1. **Active**: The organization and all associated Operations Dashboard services are fully functional.
2. **Pending Creation**: An unexpected error occurred while adding Operations Dashboard services to the organization. The organization is not yet accessible.
3. **Pending Service Update**: At least one Operations Dashboard service is operational on the organization, but one or more services are not operational yet due to an unexpected error.
4. **Pending Removal**: The organization still has devices or data that must be removed. Otherwise, errors can occur when removing the services.

## Troubleshoot org status

A **Pending** state can occur when an organization is created, updated or deleted, or when Operations Dashboard services are added or removed. If an error occurs and the organization does not change to Active state, complete the following troubleshooting steps.

### "Pending Services Update" troubleshooting

If a recently created or updated organization is in the "pending services update" state, one or more services failed to be added or removed successfully but at least one service is "active".  You can log into that organization but access to any "pending creation" services will be blocked.

1. Log into a parent organization, ideally the one used to create the organization.
2. Click the "people icon"  in the far right of the header. Click **Access Control** and then click the Organizations tab.
3. Click the affected organization to view details.
4. Click any error messages that require user action, follow that error message, and continue with the next steps.
5. Services in the “pending creation” or “pending removal” state might be experiencing unexpected failures. Wait a couple of minutes before proceeding to the next step to give the service time to be restored.
6. If the status does not change to Active, click **Edit Organization**, deselect that service and click **Save**.
7. Re-select the service and click **Save**. Verify that the service is "active".  If not, remove the service again, save, and re-add it.
8. If a service is in a "pending removal" state, edit the organization, add that service back and save it. Then attempt to remove the service again. Verify that it has been removed. Continue to remove and re-add the service until it is active.

### "Pending Creation" troubleshooting
A recently created organization may be put into a "pending creation" state if none of its Operations Dashboard services are accessible. The "My Organization" details page will show the corresponding services in a "pending creation" state. Any error messages, if available, will show up below that service's status.

To bring the organization into an "active" state, follow the steps below:

1. Log into a parent organization, ideally the one used to create the organization.
2. Click the "people icon"  in the far right of the header. Click **Access Control** and then click the **Organizations** tab.
3. Click the affected organization to view details.
4. Click any error messages that require user action, follow that error message, and continue with the next steps.
5. Services in “Pending Creation” might be experiencing an unexpected failure. Wait a couple of minutes before proceeding to the next step to give the service time to be restored.
6. If the status does not change to Active, click **Delete Organization**, and recreate it.
7. After recreating the organization, expand the organization tree and verify that the status is "active", which means the organization is accessible.

>**Note**: If the organization is in a "pending removal" state after deletion, complete the following steps.

### "Pending Removal" troubleshooting

If service removal fails when deleting an organization, an organization will be put into a "pending removal" state. Services that have been removed successfully will be fully removed, while any service causing errors will remain accessible for the user. To successfully delete the organization:

1. Log into a parent organization, ideally the one used to create the organization.
2. Click the "people icon"  in the far right of the header. Click **Access Control** and then click the **Organizations** tab.
3. Click the affected organization to view details.
4. Click any error messages that require user action, follow that error message, and continue with the next steps.
    1. For example, a common error message is that the organization still has devices and cannot be deleted. In this case, log into that organization, remove all devices, log back into the parent organization, and proceed to the next step.
5. If there are no error messages for a service in “pending removal”, the service might be experiencing unexpected failures. Wait a couple of minutes before proceeding to the next step to give the service time to be restored.
6. Retry deleting the organization. If the organization is still in a "pending removal" state, repeat the previous steps until it is fully removed.
