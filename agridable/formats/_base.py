from abc import ABC, abstractmethod


class _BaseFormat(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        pass

    @abstractmethod
    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        pass
