from abc import ABCMeta, abstractmethod


class Data(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_bytes(cls, data: bytes):
        raise NotImplementedError
