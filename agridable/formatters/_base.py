from abc import ABC, abstractmethod


class _BaseFormatter(ABC):
    def __init__(self) -> None:
        pass


class _BaseColumnFormatter(_BaseFormatter, ABC):
    def __init__(self,
                 columns) -> None:
        super().__init__()
        self.columns = columns

    @abstractmethod
    def format(self,
               columnDefs_dict,
               **kwargs):
        pass


class _BaseRowFormatter(_BaseFormatter, ABC):
    def __init__(self,
                 rows) -> None:
        super().__init__()
        self.rows = rows

    @abstractmethod
    def format(self,
               getRowStyleConditions_dict,
               **kwargs):
        pass
