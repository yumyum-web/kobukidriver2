from io import BytesIO

from kobukidriver2.core.enums.controller_gain_type import ControllerGainType
from kobukidriver2.core.packet.feedback import Feedback


class ControllerGain(Feedback):
    identifier = 0x01

    def __init__(
        self,
        controller_gain_type: ControllerGainType,
        p_gain: int,
        i_gain: int,
        d_gain: int,
    ):
        super().__init__()
        self.controller_gain_type = controller_gain_type
        self.p_gain = p_gain
        self.i_gain = i_gain
        self.d_gain = d_gain

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 13:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(
            controller_gain_type=ControllerGainType(data[0]),
            p_gain=int.from_bytes(data[1:5], byteorder="little"),
            i_gain=int.from_bytes(data[5:9], byteorder="little"),
            d_gain=int.from_bytes(data[9:13], byteorder="little"),
        )
