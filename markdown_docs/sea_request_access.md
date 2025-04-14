# Request access to a remote session

This feature enables SEA users to request access to an asset. Once the request is approved by the designated approvers, users can remotely access the resource for a specific time.

The workflow includes the following:

1. The SEA System Admin or SEA Access Admin logs in to the IoT Operations Dashboard and creates an access control group with the “Request Access” feature enabled. 
   
   Ensure that a user with at least the “SEA User” role is assigned to the group and that an asset is added to it. For more information, see the "Create groups for remote access" topic in [Manage access control groups for remote access](./manage_schedule_access.md).

2. The remote access user logs in to the IoT Operations Dashboard and requests access to the asset in the previously created group. For more information, see [Request access to sessions](#request-access-to-sessions).

3. The SEA Access Manager reviews the request. For more information, see [Manage remote asset session requests](./manage_remote_asset_session_requests.md).

   >**Note**: Other roles such as SEA System Admin, SEA Access Admin, or any role containing “Access Approver” permissions can also review requests.

4. The remote access user can now access the asset upon approval of the request. For more information, see [Connecting to an asset](#connect-to-a-session).

## Request access to sessions

After SEA System Admins or SEA Access Admins add users to an access group with "Request Access" enabled, users can request for a session.

1. Log in to the IoT OD as an SEA user.
2. Choose **Secure Equipment Access** > **Remote Sessions**.
3. Choose the **Remote Access Group**, that contains the session you need to access. 
4. In the **session** you need access, click **Request Access**.

>**Note**: If you are in the list view, choose **Request Access** from the **Actions** column.

**Remote Session screen-Card View**
![Request Access Tile](../graphics/sea/20509_SEA_Request_Session_00_request_tile.png)

**Remote Session screen-Table View**
![Request Access List](../graphics/sea/20509_SEA_Request_Session_00_request_list.png)

4. In the **Request Access** pop-up, you can perform the following actions:
   1. (Optional) Type in a relevant comment in the **Requester Comments** field.
   2. (Required) Select a **Start Group Access Date** and **Time** using the **Calendar** and **Clock** icons.
   3. (Required) Select an **End Group Access Date and Time** using the **Calendar** and **Clock** icons.
   
>**Note**: The maximum time limit is **72 hours**.

5.  Click **Request**. The screen opens to show a **View Request** button. A **Success** pop-up opens at the bottom right corner of the screen. 
6.  Click **View Request** to open the **Sent Access Request** panel that shows the status as **Pending**. 

>**Note**: In the table view, from the **Actions** column, choose **View Request**.


**View Request-Card View**

![View Request Card](../graphics/sea/20509_SEA_Request_Session_01_view_request.png)

**View Request-Table View**

![View Request Table](../graphics/sea/20509_SEA_Request_Session_06_view%20request_table.png)

>**Note**: A request is approved by either a user with the **SEA Access Manager**, **SEA Access Admin**, or **SEA System Admin** role.

7. Once the request is approved, the session status changes to **Connect** (Card View) or the Session **Asset Name** becomes an active link (Table View).

**Session Connect-Card View**
![Connect status-Card](../graphics/sea/20509_SEA_Request_Session_04_connect_tile.png)

**Session Connect-Table View**

![Connect status-Table](../graphics/sea/20509_SEA_Request_Session_04_connect_list.png)


## Withdraw session requests

If you need to re-schedule or cancel a request, you have the option to withdraw. 

**To withdraw a request**:

1. In the session, click **View Request** (Card View) or choose **View Request** from the Actions column (Table View). 
2. From the Sent Access Request panel, click **Withdraw** (located at the bottom right corner in red).
3. In the **Withdraw Access Request** pop-up, type in **Your Reason**.
4. Click **Withdraw**. The session returns to **Request Access** status.

![Withdraw request](../graphics/sea/20509_SEA_Request_Session_01_withdraw_request.png)

## Connect to remote sessions

1. Log in IoT OD as an SEA user.
2. Click **Secure Equipment Access** > **Remote Sessions**. When a session is approved, the **Connect** button is enabled.

![Connect to a session](../graphics/sea/sea-connect-session.png)