from typing import Literal

from agridable.formats.value._base import _BaseValueFormatter


class Duration(_BaseValueFormatter):
    """
    Sets the format to duration.

    Parameters
    ----------
    unit : Literal['seconds', 'minutes', 'hours'], optional
        The unit of the value to convert; either 'seconds', 'minutes' or 
        'hours', by default 'minutes'.
    output_unit : Literal['minutes', 'hours'], optional
        The unit of the formatted value to display; either 'minutes' or 
        'hours', by default 'minutes'
    """

    def __init__(self,
                 unit: Literal['seconds', 'minutes', 'hours'] = 'minutes',
                 output_unit: Literal['minutes', 'hours'] = 'minutes') -> None:
        self.unit = unit
        self.output_unit = output_unit

    def _create_format_function(self):
        return f'formatDuration(params.value, "{self.unit}", "{self.output_unit}")'
