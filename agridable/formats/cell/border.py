from agridable.formats.cell._base import _BaseCellFormat


class Border(_BaseCellFormat):
    """
    Add a border to a cell(s).

    Parameters
    ----------
    border_side : str, optional
        The side of the border, by default 'bottom'
    border_width : str, optional
        The width of the border, by default '1px'
    border_style : str, optional
        The style of the border, by default 'solid'
    border_colour : str, optional
        The colour of the border, by default 'white'
    """

    def __init__(self,
                 border_side: str = 'bottom',
                 border_width: str = '1px',
                 border_style: str = 'solid',
                 border_colour: str = 'white') -> None:

        self.border_side = border_side
        self.border_width = border_width
        self.border_style = border_style
        self.border_colour = border_colour
        self.border_side = f'border{self.border_side.title()}'
        self.border_prop = f'{self.border_width} {
            self.border_style} {self.border_colour}'

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            'cellStyle': {
                self.border_side: self.border_prop
            },
        }

    def create_row_config(self,
                          *args,
                          **kwargs):
        return {
            'style': {
                self.border_side: self.border_prop
            }
        }
