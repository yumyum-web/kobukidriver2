from enum import IntEnum


class SequenceNumber(IntEnum):
    ON = 0x00
    OFF = 0x01
    RECHARGE = 0x02
    BUTTON = 0x03
    ERROR = 0x04
    CLEANING_START = 0x05
    CLEANING_END = 0x06
