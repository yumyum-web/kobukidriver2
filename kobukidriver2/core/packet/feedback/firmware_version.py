from io import BytesIO

from kobukidriver2.core.data.version import Version
from kobukidriver2.core.packet.feedback import Feedback


class FirmwareVersion(Feedback, Version):
    identifier = 0x0B

    def __init__(self, patch: int, minor: int, major: int):
        Version.__init__(self, patch, minor, major)
        Feedback.__init__(self)

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 4:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        version_instance = Version.from_bytes(data[0:3])
        return cls(
            patch=version_instance.patch,
            minor=version_instance.minor,
            major=version_instance.major,
        )
