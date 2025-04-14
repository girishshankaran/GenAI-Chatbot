# Record Inline sessions

This Secure Equipment Access (SEA) feature allows you to record sessions for future use, such as auditing or educational purposes. Recordings are stored in your own storage space on AWS S3 using the retention policies for the recordings at this location. The SEA System or Access Admin can enforce the session recording start through the Access Group before an SEA user can access an OT Asset within the group. Recording begins when the user launches a session from a group which enforces recording. 

For more information on AWS S3, see [What is S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

## Prerequisites:

* AWS S3 bucket has been set up and integrated with Secure Equipment Access service. See <a href="#ConfigInline">Configure Inline recording.</a>

## Configure AWS S3 external integration for SEA remote access methods

These links are provided to help create an AWS S3 account and obtain Key Access.
* Create AWS Account and S3 setup: [Get Started With S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
* AWS Account and Key Access: [Userguide](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)

<!--- ## Configure Inline recording --->
<h2><a name="ConfigInline"></a>Configure Inline recording</h2>

{%note info %}
**Note**:
  
* Recording is only available to the SEA System Admin or SEA Access Admin role. 
* Inline session recording is allowed for only SSH, RDP, VNC, and Telnet access methods. 
* The video is limited in size to 640x480 at 25 FPS, and encoded in h264 (MPEG-4-AVC) irrespective of the original access method or screen definition.
{%endnote%}

As an SEA System Admin, you can integrate an S3 bucket to store recorded video files in MP4 format.

### To configure an Inline session recording:

1. Choose **Secure Equipment Access > System Management**.
2. Click the **External Integrations** tab.
3. Click **Add External Integration**.

![Add Ext Integration](../graphics/sea/SEA_Record_sessions_00a.png)

4. In the **Add External Integration Details** pane, choose **S3** as the Integration Type.

![Add Ext Integration Panel](../graphics/sea/SEA_add_external_s3_session_pane_01.png)

5. Enter an appropriate **Name**.
6. (Optional) Create a meaningful **Description**.
7. Add the following parameters that were gathered in your AWS S3 bucket setup:

     >**Note**: Refer to Step 3 in Configuring your account in the Management Console for region and bucket name, and step 18 for access key and secret access key. [Get Started With S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
     1. **Region**: A specific endpoint for an S3 bucket such as: us-east-2.com 
     2. **Bucket**: The name of the bucket created on AWS S3. It will contain the recorded MP4 files.
     3. **Access Key**: The access key generated in AWS.
     4. **Secret Access Key**: The Access Key secret.

8. Click **Add Integration**. The External Integration record is added to the External Integration table. 

![Recording Parameters](../graphics/sea/SEA_record_07_combo.png)

>**Note**: You can configure **multiple S3 buckets** but are limited to only one active bucket at a time. Use the **Activate/Deactivate** action options to choose your active bucket.

When you successfully add the S3 External Integration, the table shows the session as active.

![Record Active Session](../graphics/sea/SEA_Record_s3_sessions_02a.png)

**Important Note**: If the Secret Access Key changes for any reason, you can't update the information. You must then delete the integration and add it again.

## Record an Inline session

Before you begin, verify that the group is enabled and the **Enforce Monitoring and Recording (Enforce Inline (SSH/RDP/VNC) Recording)** setting is also enabled. See [Manage and schedule access for existing SEA access groups](manage_schedule_access.md). 

{%note info %}
**Note**:
  
* The recording session is converted and stored in MP4 format.
*  Recording isn't enforced when launched from the global **All Access Method** group (available only to SEA System Admin). 
{%endnote%} 

![Group Record Config](../graphics/sea/SEA_record_parameters_04a.png)

>**Note**: After the remote session is finished, the recording session is converted and stored in MP4 format in the S3 bucket you created.

**To Record an Inline session**:

1. Choose **Secure Equipment Access > Remote Sessions**.
2. Choose the **Group** that has the Session Recording enabled and launch the **session** you want to record.

>**Note**: Recording isn't enforced when launched from the global **All Access Method** group (available only to SEA System and Access Admin roles).

![Choose Session](../graphics/sea/SEA_record_00.png)

1. Click **Open Session** located in the **Actions** column.

![Record Session](../graphics/sea/SEA_record_01.png)

4. When the Window opens, the session has begun.

>**Note**: Depending on the Access Method you use, you might have to use credentials. (Refer to Access Methods).

5. When you are finished recording, **close the window**, which closes the recording session. The session automatically begins the transcription process to MP4, which can take several minutes depending on how long the session is.
6. Click **Access Management**. The recording session is listed. The recorded status is **Yes**.

>**Note**: You can use the **Only Show Recorded Sessions** to search for sessions with Recorded status marked **Yes**.

>**ATTENTION**: The default recording state is set to **No** during recording and will switch to **Yes** when the transcription process is completed.
>**Note**: The SEA Admin has access to all the recordings generated by any user that launched a session in a Group that has Session Recording enabled.

![List Record Session](../graphics/sea/SEA_Record_s3_sessions_03.png)

1. Click **Actions**. The menu option window opens.
2. Choose the **option** you want to use.

>**Note**: It can take several minutes before all the options become available.

* **View Full Auditing Info**: View details of the recording session.
* **View Screen Recording**: View the recording as an MP4 file.
* **Download Screen Recording**: Download to your local device. 
* **Delete Screen Recording**: Deletes the recording record.

![Recording Options](../graphics/sea/SEA_Record_s3_sessions_04.png)

## Review a recording

**To review a previously recorded session**:

Choose **Access Management > Session History**> **Selected Session**> **Actions**> **...**> **View Inline Recording or Download the video file**.  For more information on reviewing recordings, see [Monitor and terminate sessions](../secure_equipment_access/monitoring_sessions.md).
