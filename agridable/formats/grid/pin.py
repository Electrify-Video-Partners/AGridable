from typing import Literal

from ._base import _BaseGridFormat


class Pin(_BaseGridFormat):
    """
    Pins columns to the given side of the grid.

    Parameters
    ----------
    side : Literal['left', 'right'], optional
        The side of the grid to pin the columns to, by default 'left'
    """

    def __init__(self,
                 side: Literal['left', 'right'] = 'left') -> None:
        self.side = side

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            'pinned': self.side
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        raise NotImplementedError
