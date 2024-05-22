from typing import Literal, Union

from agridable.formats.value._base import (
    _BaseValueFormatter,
    PRECISION_TYPE_JS_MAP
)


class Currency(_BaseValueFormatter):
    """
    Sets the format to currency.

    Parameters
    ----------
    currency : str, optional
        The 3 character currency code, by default 'USD'
    precision : int, optional
        The precision to display, by default 2
    precision_type : Literal['sf', 'dp'], optional
        The precision type to use; either 'sf' (significant figures) or 
        'dp' ('decimal points'), by default 'dp'
    unit_scale : Union[Literal['thousands', 'millions', 'billions', 'trillions'], None], optional
        The unit scale to use; either 'thousands', 'millions', 'billions', 
        'trillions', by default None
    """

    def __init__(self,
                 currency: str = 'USD',
                 precision: int = 2,
                 precision_type: Literal['sf', 'dp'] = 'dp',
                 unit_scale: Union[
                     Literal['thousands', 'millions',
                             'billions', 'trillions'], None
                 ] = None):
        self.currency = currency
        self.precision = precision
        self.precision_type = precision_type
        self.precision_type_js = PRECISION_TYPE_JS_MAP[self.precision_type]
        self.unit_scale = unit_scale

    def _create_format_function(self):
        return f'formatCurrency(params.value, "{self.currency}", "{self.unit_scale}", {self.precision}, "{self.precision_type_js}")'
