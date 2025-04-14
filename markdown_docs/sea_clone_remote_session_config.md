# Bulk Configuration Cloning

This feature is useful for replicating the SEA configuration, such as assets and remote sessions, across multiple network devices. You can configure one network device and use it as a reference for configuring other network devices. You can copy SEA assets and SEA access methods from one network device to multiple devices using a three-step workflow. During this process, the selected assets and remote sessions, such as IP addresses, URLs, and credentials, are copied from the source device to the target devices. If the target devices require different configurations or values, you can use the bulk configuration workflow and then update the specific values for each device.


## Clone the Session Configuration

To clone the asset and remote session configurations from a network device to one or more target devices, follow these steps:
1. Log in to the Cisco IoT Operations Dashboard as a user with SEA System Admin role.
2. Choose **Secure Equipment Access** > **System Management**.
3. On the **System Management** pane, select the network device whose configuration you want to clone, and then select **Clone Remote Session Configuration** in the **Action** column. 
   
   ![Bulk Configuration Cloning](../graphics/sea/bulk_config_cloning_1.png)
4. On the **Clone Remote Session Configuration** page, select the remote sessions you want to clone, and then click **Next**.
   
   ![Select remote sessions](../graphics/sea/bulk_config_cloning_2.png)
   
   **Notes**: 
   - An asset must contain remote sessions for the configuration to be copied. If you add assets but don't create remote sessions under them, the assets won't be copied.
   - If the target devices already have remote sessions with the same names as those being cloned, the cloned session names will be appended with the string "-copy" to avoid conflicts. For example, if the source network device has a remote session called "Ubuntu-Server" and the target network device already has a session with the same name, the cloned session on the target device will be renamed to "Ubuntu-Server-copy 1."

5. In the **Assign Access Control Group** area, choose one of the following options:
   - **Add all cloned remote sessions to all the original access control groups** - Use this option if you want to keep the cloned remote sessions associated with the original access control groups. If the remote sessions in the source device are associated with access control groups, the same associations will be made for the cloned remote sessions in the target devices. This means that the users who had access to the remote sessions in the source device will automatically have access to the cloned remote sessions in the target device after cloning.
   - **Do not add any cloned remote sessions to the original access control groups** - Use this option if you don't want to associate the cloned remote sessions with the original access control groups. In this case, you can associate the cloned remote sessions with different access control groups.
6. Click **Next**.
7. In the **Choose Target Network Devices** area, select the target devices from the list. 
   The remote sessions and the assets are copied to these devices.
8. Click **Done**.
   You receive a success message indicating that cloning of remote sessions and assets is initiated.

## View Cloning History
You can view the history of all cloning activities that you have performed on the Cisco IoT Operations Dashboard. The history includes details of the source network device, the user who initiated the cloning, the cloned remote sessions, the cloned assets, the target devices, and the date and time of the cloning.

To view the history, follow these steps:
1. Log in to the Cisco IoT Operations Dashboard as a user with SEA System Admin role.
2. Choose **Secure Equipment Access** > **System Management**.
3. On the **System Management** pane, select **View Cloning History** from the **More Actions** drop-down list.
   
   The Remote Session and Asset Cloning History page appears.
   ![Bulk Cloning History](../graphics/sea/bulk_cloning_history.png)
4. To view the cloning history for a specific period, select start and end dates in the box preceding the Search Table.
   The cloning history specific to the given period appears. The history may include one or more cloning activities.
5. To get the details of a specific cloning activity, click the associated job name.

## Clear Assets and Access Methods

This feature enables you to quickly clear all assets and access methods from a network device with a single click.

To clear the configuration, follow these steps:
1. Log in to the Cisco IoT Operations Dashboard as a user with SEA System Admin role.
2. Choose **Secure Equipment Access** > **System Management**.
3. On the **System Management** pane, select the network devices whose configuration you want to clear, and then select **Clear All Assets and Access Methods** from the **More Actions**.
4. On the confirmation window, click **Delete**.
   
The configurations of the selected network devices are cleared.


