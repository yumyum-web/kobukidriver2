from io import BytesIO

from kobukidriver2.core.packet.feedback import Feedback


class DockingIR(Feedback):
    identifier = 0x03

    def __init__(
        self,
        right: bool,
        center: bool,
        left: bool,
        far_right: bool,
        far_center: bool,
        far_left: bool,
        near_right: bool,
        near_center: bool,
        near_left: bool,
    ):
        super().__init__()
        self.right = right
        self.center = center
        self.left = left
        self.far_right = far_right
        self.far_center = far_center
        self.far_left = far_left
        self.near_right = near_right
        self.near_center = near_center
        self.near_left = near_left

    @classmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        if data_length != 3:
            raise ValueError("Invalid data length")
        data = buffer.read(data_length)
        return cls(
            right=bool(data[0]),
            center=bool(data[1]),
            left=bool(data[2]),
            far_right=bool(data[1] & 0x20),
            far_center=bool(data[1] & 0x10),
            far_left=bool(data[1] & 0x08),
            near_right=bool(data[1] & 0x04),
            near_center=bool(data[1] & 0x02),
            near_left=bool(data[1] & 0x01),
        )
