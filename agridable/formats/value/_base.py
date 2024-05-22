
from abc import ABC, abstractmethod
from agridable.formats._base import _BaseFormat

PRECISION_TYPE_JS_MAP = {
    'dp': 'f',
    'sf': 'r'
}


class _BaseValueFormatter(_BaseFormat, ABC):
    def __init__(self) -> None:
        super().__init__()

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        format_function = self._create_format_function()
        return {
            "valueFormatter": {
                "function": format_function
            },
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        return super().create_row_config(*args, **kwargs)

    @abstractmethod
    def _create_format_function(self) -> str:
        pass


class _BaseCellRenderer(_BaseFormat, ABC):
    cell_renderer = None

    def __init__(self) -> None:
        super().__init__()

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            "cellRenderer": self.cell_renderer
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        return super().create_row_config(*args, **kwargs)
