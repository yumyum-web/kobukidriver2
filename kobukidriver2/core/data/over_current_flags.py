from kobukidriver2.core.data import Data


class OverCurrentFlags(Data):
    def __init__(self, left_wheel: bool, right_wheel: bool):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("Over current flags data must be 1 byte long")
        return cls(
            left_wheel=bool(data[0] & 0x01),
            right_wheel=bool(data[0] & 0x02),
        )
