from typing import Literal

from agridable.formats.value._base import (
    _BaseValueFormatter,
    PRECISION_TYPE_JS_MAP
)


class Percentage(_BaseValueFormatter):
    """
    Sets the format to percentage.

    Parameters
    ----------
    precision : int, optional
        The precision to display, by default 2
    precision_type : Literal['sf', 'dp'], optional
        The precision type to use; either 'sf' (significant figures) or 
        'dp' ('decimal points'), by default 'dp'
    is_decimal : bool, optional
        Whether the value is stored as a decimal (True) or in percentage-ready
        format (False). For example, 99% would be 0.99 in decimal format and 
        99 as percentage-ready, by default True
    """

    def __init__(self,
                 precision: int = 2,
                 precision_type: Literal['sf', 'dp'] = 'dp',
                 is_decimal: bool = True):
        self.precision = precision
        self.precision_type = precision_type
        self.precision_type_js = PRECISION_TYPE_JS_MAP[self.precision_type]
        self.is_decimal = is_decimal
        self.is_decimal_js = str(self.is_decimal).lower()

    def _create_format_function(self) -> str:
        return f'formatPercentage(params.value, {self.precision}, "{self.precision_type_js}", {self.is_decimal_js})'
