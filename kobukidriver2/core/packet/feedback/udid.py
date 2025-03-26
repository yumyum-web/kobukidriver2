from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class UDID(Feedback):
    identifier = 0x13

    def __init__(self, udid0: int, udid1: int, udid2: int):
        super().__init__()
        self.udid0 = udid0
        self.udid1 = udid1
        self.udid2 = udid2

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 12:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(
            udid0=int.from_bytes(data[0:4], byteorder="little"),
            udid1=int.from_bytes(data[4:8], byteorder="little"),
            udid2=int.from_bytes(data[8:12], byteorder="little"),
        )
