from kobukidriver2.core.data import Data


class Battery(Data):
    def __init__(self, voltage: int):
        self.voltage = voltage

    @classmethod
    def from_bytes(cls, data):
        if len(data) != 1:
            raise ValueError("Battery data must be 1 byte long")
        return cls(
            voltage=data[0],
        )
