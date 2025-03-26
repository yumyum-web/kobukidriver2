from kobukidriver2.core.data import Data
from kobukidriver2.core.enums.charging_state import ChargingState


class Charger(Data):
    def __init__(self, charging_state: ChargingState):
        self.charging_state = charging_state

    @classmethod
    def from_bytes(cls, data: bytes):
        if len(data) != 1:
            raise ValueError("Charger data must be 1 byte long")
        return cls(
            charging_state=ChargingState(data[0]),
        )
