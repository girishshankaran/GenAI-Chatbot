## Manage Remote Asset Session Requests

Access Managers usually approve the session requests. However, if Access Managers are unavailable, users with the SEA System Admin or SEA Access Admin role can also approve remote session requests even if they're not explicitly assigned as approvers.

| User Role           | Permissions                           |
|---------------------|---------------------------------------|
| SEA System Admins   | Manage all requests in the organization |
| SEA Access Admins   | Manage all requests in the organization |
| SEA Access Managers | Manage requests only for a group where they're assigned as approvers         |


## Manage Requests as an SEA Access Manager

To manage remote asset session requests, follow these steps:

1. Log in to the Cisco IoT Operations Dashboard as an SEA Access Manager.
2. Choose **Secure Equipment Access** > **Access Management**.
3. On the **Access Management** pane, select the **Pending Requests** tab.
   The **My pending requests** tab appears.

   All requests for which you are an approver are listed in this tab. These requests are submitted by users within your group.
4. In the **Actions** column, select **Approve**, **Deny**, or **View**. 

![Pending Requests](../graphics/sea/SEA_Request_Session_02_approve.png)

## Manage Requests as a SEA System or Access Admin

To manage remote asset session requests, follow these steps:

1. Log in to the Cisco IoT Operations Dashboard as a System or Access Admin.
2. Choose **Secure Equipment Access** > **Access Management**.
3. On the **Access Management** pane, select the **Pending Requests** tab.
    Two additional tabs open under the **Pending Requests** tab: **My Pending Requests** and **All Pending Requests**.
4. Click the **All pending requests** tab.
   All requests in your organization that need approval are listed here, including those assigned to the Access Managers.
5. In the **Actions** column, select **Approve**, **Deny**, or **View**. 

![Pending Requests](../graphics/sea/SEA-Approve-Request-Access-Access-Manager.png)

### **What happens after you act on a request?**

Once you act on a request, an email notification is sent to the SEA user. The email includes details about the actions that the user needs to perform. Clicking the **View** button in the email takes the user to the **Remote Sessions** page on the Cisco IoT Operations Dashboard. 

When you approve a request, the requested user can navigate to and connect to the remote session.

>**Note**: If you deny a request, the session status reverts to **Request Access** and the user must re-initiate the request process.  

### Request History

You can view the history of all access requests in the **Request History** tab. The entries displayed in the **Request History** tab vary depending on your user role.

| User Role           | Request History tab entries                           |
|---------------------|---------------------------------------|
| SEA System Admins   | All approved, denied, expired, revoked, and withdrawn requests for all users across all groups in the organization |
| SEA Access Admins   | All approved, denied, expired, revoked, and withdrawn requests for all users across all groups in the organization  |
| SEA Access Managers | All approved, denied, expired, revoked, and withdrawn requests of all users in the group where they are assigned as approvers. They can't see the entries of a group where they are not the approvers.          |


## Revoke a Request

You can revoke an approved request if you accidentally approved it. The revoked request is listed in the **Request History** tab. Revoking a request doesn't have any effect on active sessions. The sessions continue until they time out. However, users can't establish a new connection on the asset. You can sort the list in the **Request History** tab according to various criteria such as dates, approval status, approver name, etc. You can also download the list as a CSV file.

To revoke an approved request, follow these steps:

1. Go to the **Request History** tab.
2. Select the request you want to revoke.
3. Click **Revoke** in the **Actions** menu.

Alternatively, you can revoke a request by selecting **View** in the **Actions** menu and then clicking **Revoke** on the View Details page.

**SEA Access Manager or Admin view**:

![Revoke Requests](../graphics/sea/Revoke-request-SEA-Admin.png)

**SEA System Admin view**:

![Revoke Requests](../graphics/sea/Revoke-request-access-sys-adm.png)