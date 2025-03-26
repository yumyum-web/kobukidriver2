from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class Raw3DGyro(Feedback):
    identifier = 0x0D

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        buffer.read(data_length)
        return cls()
