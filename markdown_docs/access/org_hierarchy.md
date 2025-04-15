# Organization Hierarchy for IoT OD

The Organization Hierarchy feature lets you group assets. It allows you to segregate assets under a distinct organization in a hierarchical manner, based on your needs. For example, if you are managing the assets of Company 1, Company 2, and Company 3 and you need to segregate the accesses and assets. Assign the assets to different levels of the hierarchy using the supported Services (such as Industrial Asset Vision). You must have the required permissions (see Role Based Access Control below) to view the levels in the Organization Hierarchy. Based on the organization levels that you have access to, you can view the associated assets that are present under the hierarchy level and its child levels. Selecting a specific level in the hierarchy will show the number of assets present under that hierarchy level and all of its child levels. The Organization Hierarchy pane, as well as the levels, can be collapsed/expanded. The **Global** level is the parent (root) level. You can create multiple child levels and each child level can have multiple child levels. The levels **Public** and **Unused** are auto-created by the system.


## Role Base Access Control for Organization Hierarchy

{%note info %}
**Notes**:
* The Tenant Admin role has access to Organization Hierarchy by default.
* To add Tenant Admin role to a new/existing user, add the role name **Tenant Admin**. Click **Access Control > Users** tab. Add or edit a user to add this role.
{%endnote%}

To access the Organization Hierarchy tab in IoT OD Services, you must have at least one of the following permissions:

* Organization Hierarchy Management Read Write (for read-write operations)
* Organization Hierarchy Management Read Only (for read-only operations)
* Tenant Management (for read-write operations)


##  Manage Organization Hierarchy levels

{%note info %}
**Notes**: 
* The **Organization Hierarchy** tab will only show if the Feature Flag for Organization Hierarchy is enabled for your organization.
* The **Impact Rating** column in the Organization Hierarchy screen will be present only if the Feature Flag for Industrial Impact Rating is enabled.
{%endnote%}

### View Organization Hierarchy levels

1. Click the "people icon" on the far right of the header. Click **Access Control**.
2. Click **Organization Hierarchy**.

The Organization Hierarchy page shows the hierarchy levels on the left and the detailed view of the levels on the right in a tabular form.

**Organization Hierarchy level details**

|Heading|Description|
|---|---|
|Level|	Shows the currently selected level and its child levels.|
|Org Hierarchy	|The hierarchy path from Global to the currently selected level.|
|Impact Rating	|**Impact Rating** is a value that you assign to each level, based on the function of the assets within that level. For example, if you are managing sensors to a refrigerated chamber and the temperature in the chamber exceeds a safety level, you can decide how to best manage the contents of the chamber, depending on the threshold margins for the contents. In this example, the impact rating would be higher than another asset that is non-perishable. Impact rating is the criticality of this level to your organization.<br>The rating options are:<br>* 0 — No impact<br>* 1 — Very low<br>* 2 — Low<br>* 3 — Medium<br>* 4 — High<br>* 5 — Very high|
|Count|	The number of assets in the currently selected level. Hover over the count to see a breakdown of the assets per Service (EDM/IAV etc.).|
|Action	|Shows the options to Add, Edit and Delete levels.|


### Add Levels

1. Click the "people icon" on the far right of the header. Click **Access Control**.
2. Click **Organization Hierarchy**.
3. Hover over ![Ellipsis](/graphics/edge_device/ellipsis_global.png) next to a level in the hierarchy or in the **Actions** column in that table and click **Add Level**.
4. Enter an appropriate name in the **Level Name** field.
5. In the **Industrial Impact Rating** field, select a rating from 0 to 5 from the drop-down list. This is an optional field.
   >**Note**: The **Global**, **Public**, and **Unused** levels have a default Impact Rating of 0. If you don't provide the Impact Rating to a level, it defaults to 0.
7. Click **Add**.

The new level is displayed in the table.

{%note info %}
**Notes**:
1. You can add a maximum of 10 child levels per level.
2. You cannot add levels under **Public** and **Unused** levels.
{%endnote%}

### Edit Levels

1. Click the "people icon" on the far right of the header. Click **Access Control**.
2. Click **Organization Hierarchy**.
3. Hover over ![Ellipsis](/graphics/edge_device/ellipsis_global.png) next to a level in the hierarchy or in the **Actions** column in that table and click **Edit**.
4. Make the required changes and click **Save**.

The changes are reflected in the table.

>**Note**: You cannot modify the names of **Global**, **Public** and **Unused** levels since they are system-defined levels, but you can modify their impact ratings.

### Delete Levels

1. Click the "people icon" on the far right of the header. Click **Access Control**.
2. Click **Organization Hierarchy**.
3. Hover over ![Ellipsis](/graphics/edge_device/ellipsis_global.png) next to a level in the hierarchy or in the **Actions** column in that table, click **Delete** and then click **Yes** when prompted.

The deleted level is removed from the table.

{%note info %}
**Notes**: 
You cannot delete:
* **Global**, **Public**, and **Unused** levels since they are system-defined levels.
* A level if it has child levels.
* A level if its count is not 0.
{%endnote%}
