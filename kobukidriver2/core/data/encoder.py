from kobukidriver2.core.data import Data


class Encoder(Data, int):
    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 2:
            raise ValueError("Encoder data must be 2 bytes long")
        return cls(int.from_bytes(data, "little", signed=False))
