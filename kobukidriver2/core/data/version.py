from kobukidriver2.core.data import Data


class Version(Data):
    def __init__(self, patch: int, minor: int, major: int):
        self.patch = patch
        self.minor = minor
        self.major = major

    @classmethod
    def from_bytes(cls, data):
        if len(data) != 3:
            raise ValueError("Version data must be 3 bytes long")
        return cls(
            patch=data[0],
            minor=data[1],
            major=data[2],
        )
