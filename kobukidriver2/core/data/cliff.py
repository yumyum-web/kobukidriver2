from kobukidriver2.core.data import Data


class Cliff(Data):
    def __init__(self, right: bool, center: bool, left: bool):
        self.right = right
        self.center = center
        self.left = left

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("Cliff data must be 1 byte long")
        return cls(
            right=bool(data[0] & 0x01),
            center=bool(data[0] & 0x02),
            left=bool(data[0] & 0x04),
        )
