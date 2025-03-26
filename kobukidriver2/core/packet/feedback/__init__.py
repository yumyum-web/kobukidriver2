from abc import ABCMeta, abstractmethod
from io import BytesIO

from kobukidriver2.core.packet import Packet


class Feedback(Packet, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_buffer(cls, buffer: BytesIO, data_length: int):
        raise NotImplementedError
