
from abc import ABC
from agridable.formats._base import _BaseFormat


class _BaseCellFormat(_BaseFormat, ABC):
    def __init__(self) -> None:
        super().__init__()
