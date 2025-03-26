# KobukiDriver2

KobukiDriver2 is a Python driver for the Kobuki robot. It provides an interface to communicate with the robot, send commands, and receive feedback.

## Installation

To install the package, use pip:

```sh
pip install kobukidriver2
```

## Usage

### Initializing the Kobuki

To initialize the Kobuki driver, you can either autodetect it or specify the port and baud rate:

```python
from kobukidriver2.core.kobuki import Kobuki

# Autodetect the Kobuki robot
kobuki = Kobuki.autodetect()

# Or initialize with a specific port and baud rate
kobuki = Kobuki(port='/dev/ttyUSB0', baud_rate=115200)
```

### Sending Commands

You can send commands to the Kobuki robot using the `send_command_transmission` method:

```python
from kobukidriver2.core.command_transmission import CommandTransmission
from kobukidriver2.core.packet.command.base_control import BaseControl
from kobukidriver2.core.packet.command.get_controller_gain import GetControllerGain

# Create a command transmission
command = CommandTransmission(
    BaseControl(speed=100, radius=0),
    GetControllerGain()
)

# Send the command to the Kobuki
kobuki.send_command_transmission(command)
```

### Receiving Feedback

You can receive feedback from the Kobuki robot using the `receive_feedback_transmission` method:

```python
# Start the feedback reader thread
kobuki.start()

# Get feedback transmission
feedback = kobuki.get_feedback_transmission()

# Stop the feedback reader thread
kobuki.stop()
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the LGPLv3 License - see the [LICENSE](LICENSE) file for details.
