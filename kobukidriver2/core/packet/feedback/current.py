from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class Current(Feedback):
    identifier = 0x06

    def __init__(self, left: int, right: int):
        super().__init__()
        self.left = left
        self.right = right

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 2:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(left=data[0], right=data[1])
