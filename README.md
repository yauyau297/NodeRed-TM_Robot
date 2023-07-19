# TM Robot Connection using Node-RED

This guide provides a brief overview of how to connect and communicate with a TM (Techman) Robot from Taiwan using Node-RED. The TM Robot provides a simple and efficient way to automate your tasks, and by using Node-RED, we can make the process of sending commands to the robot even more accessible.

## Prerequisites

Before you start, make sure you have the following:

- A TM Robot from Techman.
- Node-RED installed on your system.
- Access to your robot's IP address and port (usually provided in the robot's documentation).
- Basic knowledge of Node-RED flows.

## Installation

You'll need the `node-red-contrib-modbus` Node-RED package to connect to your TM Robot. You can install it directly from the Node-RED interface by going to "Manage Palette" -> "Install" and then search for `node-red-contrib-modbus`, or you can install it via npm:

```bash
npm install -g node-red-contrib-modbus
```

## Connecting to the TM Robot
Here is a basic Node-RED flow to establish a Modbus connection with your TM Robot:
```json
[{
    "id": "5cd4b0c4.a5b3e",
    "type": "modbus-read",
    "name": "TM Robot",
    "topic": "",
    "showStatusActivities": false,
    "logIOActivities": false,
    "server": "your_modbus_server",
    "useIOFile": false,
    "ioFile": "",
    "useIOForPayload": false,
    "x": 500,
    "y": 240,
    "wires": [
        ["1a55b4a5.e5aa4b"],
        []
    ]
},
{
    "id": "1a55b4a5.e5aa4b",
    "type": "debug",
    "name": "",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "x": 700,
    "y": 240,
    "wires": []
}]
```
In this example, replace 'your_modbus_server' with your TM Robot's IP address and port. The Modbus Read node will continuously read data from your robot and send it to the Debug node, where you can observe it.

## Sending Commands
To send a command to the robot, you can use a similar setup. Instead of a Modbus Read node, use a Modbus Write node. The command you send will depend on your robot's specifications and the actions you want it to perform.

Please refer to the TM Robot documentation for more details about the specific Modbus registers you should read from or write to.

## Conclusion
By using Node-RED and Modbus, you can create a flexible and powerful interface for controlling your TM Robot. Keep in mind that this is a basic setup, and you might need to adjust it based on your specific use case.

## Troubleshooting
If you're having trouble connecting to your TM Robot, here are a few things you can check:

- Make sure your robot is connected to the same network as your Node-RED instance and that the robot's IP address and port are correctly set up in your Modbus nodes.
- Check your robot's documentation to ensure you're using the correct Modbus function codes and addressing the correct registers.
- If you're still having trouble, you might need to reach out to TM Robot support for more assistance.

## References

- [Node-RED Documentation](https://nodered.org/docs/)
- [node-red-contrib-modbus on npm](https://www.npmjs.com/package/node-red-contrib-modbus)
- [Techman Robot - TM Robot](https://www.tm-robot.com/en/)
