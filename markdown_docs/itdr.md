# Identity Threat Detection and Response (ITDR) insights

This feature enables administrators to proactively identify and respond to potential identity threats. By collecting and analyzing user activity data, information security professionals gain valuable insights into user behavior, allowing them to detect and mitigate potential identity risks.

SEA administrators can gather valuable data about user activity and access privileges, including:
* The number of remote sessions initiated by each user.
* User membership in access control groups.
* The number of assets each user has access to.

Administrators can block a user from accessing SEA if the user exhibits any suspicious or malicious behavior. This includes activities like unusual number of sessions on a given day, unusual usage times (for example, weekend access when the user typically works weekdays), logins from unexpected devices (for example, mobile devices when laptop use is expected), or prolonged periods of inactivity when regular activity is anticipated.

## View user activity

Follow these steps to view the user activity on Cisco IoT Operations Dashboard.

1. Log in to the Cisco IoT Operations Dashboard as an SEA Admin.
2. Choose **Secure Equipment Access** > **Access Management**.
3. On the **Access Management** pane, select the **Users** tab.
>The **Users** tab lists the following information about each user:

>>| Field | Description |
>>|---|---|
>>| User | The email ID of the user |
>>| Status | The status can have the following values:<br> - Active - The user has logged in to SEA one or more times in the last 30 days.<br> - Inactive - The user hasn't logged in to SEA at least once in the last 30 days.<br> - Blocked - The user is blocked by the administrator. |
>>| Highest Role | Users may have multiple roles assigned to them. Highest role is the one with the highest privileges. |
>>| Assets | Number of assets the user can access. |
>>| Access Control Groups | Number of access control groups which the user belongs to. |
>>| Last Connected | The date when the user last connected to a remote session. |
>>| Last Login | The date when the user last logged in to SEA. |
>>| Remote Sessions | Number of remote sessions the user owns. |
>>| Network Devices | Number of network devices associated with the assets the user owns. |

>**Note**: The number of fields varies depending on your selection on the **Table Settings** page.

1. To find more details about a user, click the corresponding email ID. A new page opens with sections for **User Details**, **Assets**, **Last Known Device Status**, **Remote Session History**, and **Access Control Groups**. Explore each section for more information.
2. To block a user, click **Block** in the **User Details** section.
>**Notes**:
 - Blocking users immediately prevents them from accessing SEA and terminates all active sessions. The user's access remains suspended until explicitly unblocked by an administrator.
 - Admin users can't be blocked because they can unblock themselves. Attempting to block an admin user results in the 'Cannot perform user action block' message.




