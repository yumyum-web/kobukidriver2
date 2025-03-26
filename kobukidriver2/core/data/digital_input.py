from kobukidriver2.core.data import Data


class DigitalInput(Data):
    def __init__(
        self, channel_0: bool, channel_1: bool, channel_2: bool, channel_3: bool
    ):
        self.channel_0 = channel_0
        self.channel_1 = channel_1
        self.channel_2 = channel_2
        self.channel_3 = channel_3

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 2:
            raise ValueError("Digital input data must be 2 bytes long")
        return cls(
            channel_0=bool(data[0] & 0x01),
            channel_1=bool(data[0] & 0x02),
            channel_2=bool(data[0] & 0x04),
            channel_3=bool(data[0] & 0x08),
        )
