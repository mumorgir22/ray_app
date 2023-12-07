from abc import ABC, abstractmethod
from typing import Any


class BaseConnection(ABC):
    @abstractmethod
    def connect(self) -> Any:
        pass

    @abstractmethod
    def disconnect(self) -> Any:
        pass
