# Firewall Rules: Devices and Network Requirements

This page provides information on the firewall rules for your devices and key network requirements which helps to create a secure and efficient infrastructure for your organization. 

>**Note**: The below details are applicable for externally-managed devices only. Externally-managed devices refers to devices that are managed through CLI, Cisco Controllers, or other third-party systems. It excludes devices managed by the Edge Device Manager (EDM) service in IoT OD.

## Supported browsers

Use the latest version of a supported web browser to access the admin console.

| **Browser** | **Supported version** |
|-------------|-----------------------|
| Chrome      | Latest                |
| Firefox      | Latest                |
| Microsoft Edge    | Latest         |

## DHCP and DNS requirements

* Devices on your network must be able to connect to your IoT OD cloud cluster at either https://us.ciscoiot.com/ or https://eu.ciscoiot.com/.
* The network to which the device connects for the uplink traffic must provide:
    * A DHCP IP address to the device.
    * Default route and Domain Name System (DNS) server, and be able to resolve domain names such as eu.ciscoiot.com/, us.ciscoiot.com/
* The device should have an accurate clock set manually or through the use of NTP.

## Network ports and protocols

The following TCP/UDP network ports and IP protocols must be opened on the network firewall to allow the edge devices to communicate with Cisco IoT OD.

We recommend using a Dynamic Domain Name Service (DDNS) firewall, where possible.

>**Note**: When you set up IoT OD cloud for a new organization, depending on your access, you can go to either https://us.ciscoiot.com/ or https://eu.ciscoiot.com/  to create an account. These two links represent IP address clusters established for the Cisco IoT Cloud. Each cluster has nine IP addresses. The complete list of IP addresses for each cluster is listed in this table.

| **Port** | **Protocol** |**Destination** | **Description**  |
|----------|--------------|----------------|------------------|
| 53       | UDP          | IP of assigned DNS Server |The network device must have access to DNS resolution service. |
| 443      | TCP          | The complete list of IP addresses for each cluster.<br>US Cluster: [https://us.ciscoiot.com](http://us.ciscoiot.com)<br>Address:<br>34.208.194.240<br>54.149.83.252<br>44.240.60.228<br>52.41.249.164<br>35.84.105.79<br>44.239.87.207<br>52.13.236.221<br>35.82.65.56<br>44.233.50.219<br><br>EU Cluster: [https://eu.ciscoiot.com](http://eu.ciscoiot.com)<br>Address:<br>52.48.70.216<br>34.248.53.167<br>52.214.211.181<br>54.78.150.189<br>52.18.172.175<br>99.80.35.117<br>52.17.112.150<br>34.251.125.44<br>34.241.227.241  | HTTPS connection to access IoT OD and for devices to register.  |

>**Note**: These settings are subject to change and will need to be updated in future releases.

