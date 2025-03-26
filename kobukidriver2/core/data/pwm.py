from kobukidriver2.core.data import Data


class PWM(Data, int):
    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("PWM data must be 1 byte long")
        return cls(int.from_bytes(data, "little", signed=True))
