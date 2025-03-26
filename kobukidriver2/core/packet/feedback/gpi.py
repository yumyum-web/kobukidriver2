from io import BytesIO

from kobukidriver2.core.data.analog_input import AnalogInput
from kobukidriver2.core.data.digital_input import DigitalInput
from kobukidriver2.core.packet.feedback import Feedback


class GPI(Feedback):
    identifier = 0x10

    def __init__(
        self,
        digital_input: DigitalInput,
        analog_input_channel_0: AnalogInput,
        analog_input_channel_1: AnalogInput,
        analog_input_channel_2: AnalogInput,
        analog_input_channel_3: AnalogInput,
    ):
        super().__init__()
        self.digital_input = digital_input
        self.analog_input_channel_0 = analog_input_channel_0
        self.analog_input_channel_1 = analog_input_channel_1
        self.analog_input_channel_2 = analog_input_channel_2
        self.analog_input_channel_3 = analog_input_channel_3

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 16:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(
            digital_input=DigitalInput.from_bytes(data[0:1]),
            analog_input_channel_0=AnalogInput.from_bytes(data[1:3]),
            analog_input_channel_1=AnalogInput.from_bytes(data[3:5]),
            analog_input_channel_2=AnalogInput.from_bytes(data[5:7]),
            analog_input_channel_3=AnalogInput.from_bytes(data[7:9]),
        )
