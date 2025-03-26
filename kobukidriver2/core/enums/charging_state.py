from enum import IntEnum


class ChargingState(IntEnum):
    DISCHARGING = 0x00
    DOCKING_CHARGED = 0x02
    DOCKING_CHARGING = 0x06
    ADAPTER_CHARGED = 0x12
    ADAPTER_CHARGING = 0x16
