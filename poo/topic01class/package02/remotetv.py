from abc import ABC, abstractmethod

# Interfaz / Abstract Class
class RemoteTv(ABC):
    """Abstrac Class RemoteTv"""

    # This variable should be privated
    is_turned_on_tv = False

    @classmethod
    def power(cls) -> bool:
        if cls.is_turned_on_tv is False:
            cls.is_turned_on_tv = True
        else:
            cls.is_turned_on_tv = False
        return cls.is_turned_on_tv

    @abstractmethod
    def increase_volume(self) -> str:
        pass

    @abstractmethod
    def lower_volume(self) -> str:
        pass

    @abstractmethod
    def upload_channel(self) -> str:
        pass

    @abstractmethod
    def down_channel(self) -> str:
        pass
