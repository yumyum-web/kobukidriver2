from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class InertialSensorData(Feedback):
    identifier = 0x04

    def __init__(self, angle: int, angle_rate: int):
        super().__init__()
        self.angle = angle
        self.angle_rate = angle_rate

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 7:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(
            angle=int.from_bytes(data[0:2], byteorder="little", signed=True),
            angle_rate=int.from_bytes(data[2:4], byteorder="little", signed=True),
        )
