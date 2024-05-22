from typing import Literal

from agridable.formats.cell._base import _BaseCellFormat


class Align(_BaseCellFormat):
    """
    Align the contents of a cell.

    Parameters
    ----------
    h_align : Literal['left', 'center', 'right'], optional
        The horizontal alignment, by default 'center'
    v_align : Literal['start', 'center', 'end'], optional
        The vertical alignment, by default 'center'
    """

    def __init__(self,
                 h_align: Literal['left', 'center', 'right'] = 'center',
                 v_align: Literal['start', 'center', 'end'] = 'center') -> None:
        super().__init__()
        self.h_align = h_align
        self.v_align = v_align

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            'cellStyle': {
                'textAlign': self.h_align,
                'justifyContent': self.h_align,
                'display': 'flex',
                'alignItems': self.v_align,
            }
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        raise NotImplementedError


class HeaderAlign(_BaseCellFormat):
    """
    Align the column header.

    Parameters
    ----------
    alignment : Literal['left', 'center', 'right'], optional
        The alignment of the header, by default 'center'
    """

    def __init__(self,
                 alignment: Literal['left', 'center', 'right'] = 'center') -> None:
        super().__init__()
        self.alignment = alignment

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            'headerClass': f'{self.alignment}-aligned-header'
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        raise NotImplementedError
