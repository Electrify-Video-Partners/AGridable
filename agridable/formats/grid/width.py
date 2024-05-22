from ._base import _BaseGridFormat


class Width(_BaseGridFormat):
    """
    Sets the width of column(s).

    Parameters
    ----------
    width : int, optional
        The width of the column(s) in pixels, by default None
    min_width : int, optional
        The minimum width of the column(s) in pixels, by default None
    max_width : int, optional
        The maximum width of the column(s) in pixels, by default None
    suppress_size_to_fit : bool, optional
        Whether or not to suppress the size-to-fit grid config (if set), by 
        default True
    """

    def __init__(self,
                 width: int = None,
                 min_width: int = None,
                 max_width: int = None,
                 suppress_size_to_fit: bool = True) -> None:
        super().__init__()
        self.width = width
        self.min_width = min_width
        self.max_width = max_width
        self.suppress_size_to_fit = suppress_size_to_fit

    def create_col_config(self,
                          *args,
                          **kwargs) -> dict:
        return {
            'width': self.width,
            'minWidth': self.min_width,
            'maxWidth': self.max_width,
            'suppressSizeToFit': self.suppress_size_to_fit
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        raise NotImplementedError
