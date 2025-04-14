# Advanced parameters for RDP access method
RDP access methods include an Advanced Parameters field in the Advanced Settings section. The Advanced Parameters field provides allows you to add additional parameters for specific settings such as color depth, screen width and height, etc. The tables listed here are for each access method. 

>**Note**: When entering the parameters, use the following format: parameter1: value, parameter2: value, parameter3: value. For example: hostname: documentation, password: docpass, color-depth: 24.

## RDP access method parameters 
|Parameter Name | Description |
|-------------- | ----------- |
| width  | This optional parameter lists the width of the display in pixels.  If this value is not specified, the width of the connecting client display is used, for example 1000 pixels.|
| height | This optional parameter lists the height of the display in pixels. If this value is not specified, the height of the connecting client display is used, for example 800 pixels. |
| server<br>layout | This parameter only covers the RDP server-side keyboard layout. <br><br> **Note**: The RDP protocol is not independent of keyboard layout, and needs to "know" the keyboard layout of the server to send the proper keys when a user is typing.<br><br>Possible values are:<br>* en-us-qwerty<br>English (US) keyboard<br>* de-de-qwertz<br>German keyboard (qwertz)<br>* fr-fr-azerty<br>French keyboard azerty<br>failsafe<br>* Unknown keyboard - this option sends only Unicode events and should work for any keyboard, though not necessarily all RDP servers or applications.<br><br> **Note**: If your server's keyboard layout is not yet supported, this option should work in the meantime. 
| ignore-cert | Setting this parameter to true, enables server to ignore the returned certificate even if that certificate cannot be validated. This parameter is useful if you trust the server and your connection to the server, and the server's certificate cannot be validated.|
| disable-auth | Setting this parameter to true disables authentication while connecting to the server.<br><br>Any authentication enforced by the server over the remote desktop session (such as a login dialog) will still takes place. By default, authentication is enabled and only used when requested by the server.<br><br> **Note**: If you are using NLA, authentication must be enabled by definition.|
|another row |here it is | another change |
