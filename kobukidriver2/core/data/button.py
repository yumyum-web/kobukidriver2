from kobukidriver2.core.data import Data


class Button(Data):
    def __init__(self, button_0: bool, button_1: bool, button_2: bool):
        self.button_0 = button_0
        self.button_1 = button_1
        self.button_2 = button_2

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("Button data must be 1 byte long")
        return cls(
            button_0=bool(data[0] & 0x01),
            button_1=bool(data[0] & 0x02),
            button_2=bool(data[0] & 0x04),
        )
