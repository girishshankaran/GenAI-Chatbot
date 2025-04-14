# Manage access control groups for remote access

An access control group is a way to manage remote access for SEA users. You can create an access control group and add SEA users who want to access remote assets to the group.
This allows you to control who can access what and when.

You can configure three types of access control groups:

- **Always Active** - users in this group can always access the access methods defined in this group.
- **Scheduled Access** - users in the group can access remote assets for the configured duration.
- **Request Access** - users must explicitly request access to the remote assets, and they can access the assets only after the Access manager (approver) approves the requests.

## Create groups for remote access

>**Note**: You must have either an SEA System Admin or an SEA Access Admin role to create access control groups.

1. From the left **Service** panel, choose **Secure Equipment Access > Access Management**.
    The **Access Management** page appears.
2. On the **Access Management** page, the **Access Control Groups** table is displayed.

![Access Mgmt screen](../graphics/sea/SEA_Manage_Schedule_00a.png)

The **Access Control Groups** table lists the available access control groups and their details such as the name of the group and the number of users assigned to the group.
You can search for a specific group in the **Search** field at the top of the table.

3. Click **Add Group**. 
   The **Add New Access Control Group** page appears.

![Add Users](../graphics/sea/SEA_Mgmt_Sch_Add_Group_Schedule_00a.png)

4. On the **Add New Access Control Group** page:
   1. Enter the name of the access group in the **Name** field.
   2. (Optional) Enter brief description about the access group in the **Description** field.
   3. Choose a group type in the **Group Type** section depending on the remote session you want to configure. For more information, see [Request access to a remote session](./sea_request_access.md) and [Schedule access for a group](#schedule-access-for-a-group).
   4. (Optional) Click the **Group Enabled** toggle switch if you want to disable the group. By default, the group is enabled. If you disable it, the SEA users can't access remote sessions in the group.
    >**Note**: You can disable a group if there are conditions, such as device upgrade or repair, where the Access Admin doesn't want to access certain remote sessions. When you disable a group, the group wont be listed in the Access Sessions screen. 
   5. (Optional) Click the **Enforce Inline (SSH/RDP/VNC) Recording** toggle switch to enforce inline recording. By default, it's disabled. 

5.  Click **Next**.
   The **Assign Users** section appears. This section lists the users who are added to the system.
6. (Optional) In the **Assign Users** section, choose the users from the list who you want to add to the group, and click **Next**.
   The **Assign Remote Sessions** section appears. 
7. (Optional) In the **Assign Remote Sessions** section, choose the assets you want the SEA users to access.
8. Click **Save**.


## Add users to an access group
1. From the left **Service** panel, choose **Secure Equipment Access > Access Management**.
2. Choose a **group** from the **Access Management** screen.
3. From the **Users** tab, click **Add Users**.
4. Choose the **users** (click the check box to the left of their name) to add to the group and click **Save**.

**Note**: If the required User isn't shown, it must be added using SEA System Management. Ask your SEA System Admin for assistance.
![Add Users Panel](../graphics/sea/SEA_Mgmt_Sch_Add_Users_00.png)

## Add asset access to an access group

1. From the left **Service** panel, choose **Secure Equipment Access > Access Management**.
2. Choose a **group** from the Access Management page.
3. Click the **Asset Access** tab. Click **Add Asset Access**.
4. Choose **Assets** from the list by clicking the **checkbox** next to the asset. 

![Add Assets](../graphics/sea/SEA_Mgmt_Sch_Add_Assets_00.png)

SEA users in the group can now view the remote session when they log in to IoT Operations Dashboard, but they can't connect to the session yet.

>**Note**: You can optionally assign a specific approver for the access request. If approvers are assigned, they will be responsible for reviewing and approving the request. If no approver is assigned, all admins (both SEA Access Admins and SEA System Admins) in your organization will receive email notifications, and any of them can review and approve the request.

## (Optional) Assign approvers

1. From the left **Service** panel, choose **Secure Equipment Access > Access Management**.
   The **Access Management** page appears, displaying a list of all access groups.
2. On the **Access Management** page, click the name of the access group created for the **Request Access** feature.
    A page appears displaying the **Assigned Users**, **Assigned Remote Sessions**, and **Access Approvers** sections.
3. In the **Access Approvers** section, click **Add access approver**.
    The **Add access approver** window appears.
4. In the **Add access approver** window, select an approver from the available list.
>**Note**: The person you choose as an approver must have the Access Admin or Access Manager role.
5. Click **Save**.

The selected approvers receive an email notification when an SEA user in the group requests access to a session. 
Even if you are a tenant admin, you won't receive the email notification unless you are explicitly selected as an approver. 
The approvers can log in to the IoT Operations Dashboard and manage the access requests.


## Schedule access for a group
When you add a group, you can schedule a specific time to access a remote group of assets.

**To schedule a specific time to access a remote group:**

{%note info %}
**Note**:
* A new, scheduled group start date/time must be for a future date. After you schedule a group, you can edit that scheduled group without being required to have future start date/time.
* The maximum allowed interval between start and stop times is 72 hours.
{%endnote%}

1. From the **Group Details** screen, enable **Schedule Settings**.
2. (Required) From the **drop-down list**, choose a **Group Time Zone**.
3. Use the **calendar** icon to set the Start Group Access **Date** and **Time**. 
4. Use the **calendar** icon to set the End Group Access **Date** and **Time**. 
5. Click **Add Group**.

The Schedule Status for the group is listed as: **Scheduled** with the Start and End time and dates for the designated **Time Zone**. 

**Note**: If a scheduled session is listed as **Schedule Expired**, that expired session can be updated for a future date without having to create a new scheduled session.

![Schedule Status](../graphics/sea/SEA_Mgmt_Sch_Add_Group_Schedule_01b.png)

The **Access Management** screen lists the scheduled groups and their status.

![Scheduled group and Status](../graphics/sea/SEA_Mgmt_Sch_Add_Group_Schedule_Status_04.png)

## SEA schedule status states for access to a session

When you open the **SEA Access Management** screen and choose **Access Control Groups**, the session schedule status column is displayed.

![SEA_Schedule_Status](../graphics/sea/SEA_Mgmt_Sch_Add_Group_Schedule_Status_02a.png)

The **Schedule Status** column lists the following four status states used for a remote session.

* **Always Active**: This state designates no specific time for access. Access is always available.
* **Scheduled**: This state designates that a specific time span for access to a session has been scheduled for a future date. 
* **Active**: This state indicates that the scheduled time for access to a session is currently in progress.
* **Schedule Expired**: This state indicates that the scheduled time for access to a session has expired.

>**Note**: If a scheduled session is listed as **Schedule Expired**, that expired session can be updated for a future date without having to create a new scheduled session.

## Send invitations to group members in a scheduled meeting
>**Note**: You must have either an SEA System Admin or an SEA Access Admin role to use this feature. 

Once you create a group, assign members, schedule a meeting, you can invite specific members or all to the scheduled meeting by email invitation. 

**To invite group members to a scheduled meeting**
1. Choose the **group** that has the meeting scheduled.
2. In the **Actions** column, choose **Send Invitation** from the drop-down list. 

![Send Invitation](../graphics/sea/21132_Request_Access_Schedule_02.png)

3. To choose specific member(s), check the **checkbox** to the left of each User's Name.

>**Note**: To select all members, check the **checkbox** to the left of **User Name heading**.

![Select all members](../graphics/sea/SEA_Mgmt_Sch_Add_Group_Schedule_Status_Inivite_04.png)

4. After choosing members, click **Send Invitation** from bottom right of the screen. Each of the chosen members receives an email notification that provides the pertinent information for the meeting.

## Modify a remote session

>**Note**: You can only modify a remote session in the **List View**.

1. To modify a remote session hover over the **3 dots** in the **Actions** column and the **Edit** option opens.
2. Click **Edit**. The **Session Details** panel opens.
3. Click the **Edit** icon and edit the session details.
4. Click **Close** to save your changes.

![Modify a remote session](../graphics/sea/21121_SEA_Remote_Session_List_Edit_Composite.png)

