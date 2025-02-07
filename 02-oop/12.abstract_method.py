from abc import ABC, abstractmethod

class Phone(ABC):
    def __init__(self,model:str):
        super().__init__()
        self.model = model

    @abstractmethod
    def call_target(self, person:str):
          ...

    @property
    @abstractmethod
    def power(self):
          ...


class IPhone(Phone):
    def __init__(self, model:str):
        super().__init__(model)

    @property
    def power(self):
        pass

    def call_target(self, person:str):
        pass


iphone  = IPhone('iphone-17')
