from abc import abstractmethod, ABCMeta

from kobukidriver2.core.packet import Packet


class Command(Packet, metaclass=ABCMeta):
    def serialize(self) -> bytes:
        return bytearray([self.identifier, self.data_length]) + self.data_bytes

    @property
    @abstractmethod
    def data_bytes(self) -> bytes:
        raise NotImplementedError

    @property
    @abstractmethod
    def data_length(self) -> int:
        return self.data_length
