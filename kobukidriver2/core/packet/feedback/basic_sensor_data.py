from io import BytesIO

from kobukidriver2.core.data.battery import Battery
from kobukidriver2.core.data.bumper import Bumper
from kobukidriver2.core.data.button import Button
from kobukidriver2.core.data.charger import Charger
from kobukidriver2.core.data.cliff import Cliff
from kobukidriver2.core.data.encoder import Encoder
from kobukidriver2.core.data.over_current_flags import OverCurrentFlags
from kobukidriver2.core.data.timestamp import Timestamp
from kobukidriver2.core.data.wheel_drop import WheelDrop
from kobukidriver2.core.packet.feedback import Feedback


class BasicSensorData(Feedback):
    identifier = 0x01

    def __init__(
        self,
        timestamp: Timestamp,
        bumper: Bumper,
        wheel_drop: WheelDrop,
        cliff: Cliff,
        left_encoder: Encoder,
        right_encoder: Encoder,
        left_pwm: Encoder,
        right_pwm: Encoder,
        button: Button,
        charger: Charger,
        battery: Battery,
        over_current_flags: OverCurrentFlags,
    ):
        super().__init__()
        self.timestamp = timestamp
        self.bumper = bumper
        self.wheel_drop = wheel_drop
        self.cliff = cliff
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder
        self.left_pwm = left_pwm
        self.right_pwm = right_pwm
        self.button = button
        self.charger = charger
        self.battery = battery
        self.over_current_flags = over_current_flags

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 15:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return BasicSensorData(
            timestamp=Timestamp.from_bytes(data[0:2]),
            bumper=Bumper.from_bytes(data[2:3]),
            wheel_drop=WheelDrop.from_bytes(data[3:4]),
            cliff=Cliff.from_bytes(data[4:5]),
            left_encoder=Encoder.from_bytes(data[5:7]),
            right_encoder=Encoder.from_bytes(data[7:9]),
            left_pwm=Encoder.from_bytes(data[9:10]),
            right_pwm=Encoder.from_bytes(data[10:11]),
            button=Button.from_bytes(data[11:12]),
            charger=Charger.from_bytes(data[12:13]),
            battery=Battery.from_bytes(data[13:14]),
            over_current_flags=OverCurrentFlags.from_bytes(data[14:15]),
        )
