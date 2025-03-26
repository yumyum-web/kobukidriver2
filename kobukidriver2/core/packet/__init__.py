from abc import ABCMeta, abstractmethod


class Packet(metaclass=ABCMeta):
    @property
    @abstractmethod
    def identifier(self) -> int:
        return self.identifier
