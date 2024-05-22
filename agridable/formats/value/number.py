from typing import Literal, Union

from agridable.formats.value._base import (
    _BaseValueFormatter,
    PRECISION_TYPE_JS_MAP
)


class Number(_BaseValueFormatter):
    """
    Sets the format to a number.

    Parameters
    ----------
    precision : int, optional
        The precision to display, by default 2
    precision_type : Literal['sf', 'dp'], optional
        The precision type to use; either 'sf' (significant figures) or 
        'dp' ('decimal points'), by default 'dp'
    unit_scale : Union[Literal['thousands', 'millions', 'billions', 'trillions'], None], optional
        The unit scale to use; either 'thousands', 'millions', 'billions', 
        'trillions', by default None
    prefix : str, optional
        The prefix to add to the number, by default None
    suffix : str, optional
        The suffix to add to the number, by default None
    """

    def __init__(self,
                 precision: int = 2,
                 precision_type: Literal['sf', 'dp'] = 'dp',
                 unit_scale: Union[
                     Literal['thousands', 'millions', 'billions', 'trillion'],
                     None
                 ] = None,
                 prefix: str = None,
                 suffix: str = None):
        self.precision = precision
        self.precision_type = precision_type
        self.precision_type_js = PRECISION_TYPE_JS_MAP[self.precision_type]
        self.unit_scale = unit_scale
        self.prefix = prefix
        self.suffix = suffix
        self.prefix_js = "null" if self.prefix is None else self.prefix
        self.suffix_js = "null" if self.suffix is None else self.suffix

    def _create_format_function(self):
        return f'formatNumberPrefixSuffix(params.value, {self.prefix_js}, {self.suffix_js}, "{self.unit_scale}", {self.precision}, "{self.precision_type_js}")'
