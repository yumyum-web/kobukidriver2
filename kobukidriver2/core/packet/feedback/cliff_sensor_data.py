from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class CliffSensorData(Feedback):
    identifier: 0x05

    def __init__(self, right: int, center: int, left: int):
        super().__init__()
        self.right = right
        self.center = center
        self.left = left

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 6:
            raise ValueError(f"Invalid data length")
        data = buffer.read(data_length)
        return cls(
            right=int.from_bytes(data[0:2], byteorder="little"),
            center=int.from_bytes(data[2:4], byteorder="little"),
            left=int.from_bytes(data[4:6], byteorder="little"),
        )
