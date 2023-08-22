from abc import ABC, abstractmethod

class BaseConstraint(ABC):
    @abstractmethod
    def validate(self, value):
        raise NotImplementedError

    @abstractmethod
    def error_message(self):
        raise NotImplementedError