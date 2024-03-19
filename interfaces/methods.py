from abc import ABC, abstractmethod


class MethodsInterface(ABC):
    @abstractmethod
    def euler_method(self) -> list:
        pass

    @abstractmethod
    def runge_kutta_method(self) -> list:
        pass
