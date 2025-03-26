from enum import IntEnum


class RequestFlags(IntEnum):
    HARDWARE_VERSION = 0x01
    FIRMWARE_VERSION = 0x02
    UDID = 0x03
