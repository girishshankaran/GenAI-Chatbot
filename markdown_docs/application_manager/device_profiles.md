# Device Profiles 

This section introduces Device Profiles, which serve as common templates for groups of devices.

> **Note**: Device Profiles are applicable only to externally-managed devices. Externally-managed devices pertains to devices that are managed through CLI, Cisco Controllers, and other third-party systems. It excludes EDM-managed devices (devices managed by the Edge Device Manager (EDM) service) in IoT OD. 

Device Profiles contain common settings such as user credentials which are applicable to a group of externally-managed devices. Instead of adding these details individually to each device, you can create a profile with the username and password credentials, and link it to all devices sharing these credentials. When onboarding a device, IoT OD will use the associated user credentials configured in the device profile to establish a connection.

## Create a Device Profile

When onboarding a device, you can choose to create a new profile or use an existing one. If a suitable device profile already exists, there's no need to create a new one.

1. From the **Services** pane, select **Application Manager**.
2. Go to **Device Profiles > Create Device Profile**. The **Device Profile** page opens.
3. In the **Create Device Profile** page, specify the following parameters:
   1. **Device Profile Setup**: Provide a name and description for the device profile, and click **Next**.
   2. **Device Profile Configuration**: Provide a Username and Password for the device profile configuration, and click **Next**. 

    >**Note**: The user credentials configured in the device profile must exist on all assigned devices and have the privilege level set to 15. If not, the IoT OD won't be able to manage the applications on the device using the given credentials.

    3. **Assign Devices**: Select all the devices you want to add to the device profile and click **Next**.
    >**Note**: You can select one or more devices to move from one device profile to another.

    4. **Review**: Review all the details and click **Create Device Profile**. Click **Cancel** to exit without saving or **Back** to edit previous steps. A success pop-up opens.
 4. Click the **Device Profiles** tab to see your new device profile listed.

## Delete a Device Profile

>**Note**: To delete a Device Profile, you must first reassign all associated devices to a different Device Profile.

1. Click **Device Profiles**.
2. Select a **Device Profile Name(s)** and click **Delete**.

## Edit a Device Profile

Initiate the edit workflow when you require device reassignment to a new device profile or need to modify settings, such as user credentials, within a specific device profile.

1. From the **Services** pane, select **Application Manager**.
2. Click the **Device Profiles** tab from the left pane.
3. Select a **device profile** listed by its name or use the **Search** field. 
4. Click **Edit Device Profile**.
5. View the details given under **Device Profile**, **Device Profile Configuration**, **Assign Device**, and **Review** to modify the details and click **Save**.
