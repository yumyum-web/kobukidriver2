from kobukidriver2.core.data import Data


class WheelDrop(Data):
    def __init__(self, left: bool, right: bool):
        self.left = left
        self.right = right

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("Wheel drop data must be 1 byte long")
        return cls(
            left=bool(data[0] & 0x01),
            right=bool(data[0] & 0x02),
        )
