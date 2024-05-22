from typing import List, Literal, Dict, Union

from ._base import _BaseColumnFormatter
from ..formats.value._base import _BaseValueFormatter, _BaseCellRenderer


class ConditionalColumnFormatter(_BaseColumnFormatter):
    """
    Formats the given columns based on the conditions provided.

    Parameters
    ----------
    columns : List[str]
        The columns to apply the formats to.
    conditions : Dict[tuple, Union[_BaseValueFormatter, _BaseCellRenderer]]
        The condition-to-format configuration. A given key should be a tuple
        where the first element is the column to check against; the second 
        element is the value that the column must have to apply the format. A 
        given value is a `_BaseValueFormatter` or `_BaseCellRenderer` to apply 
        when the condition is met.
    if_col_not_exist : Literal['ignore', 'raise'], optional
        The behaviour when a column is not found in the dataframe that is 
        listed in `col_formats`; either 'ignore' (don't do anything) or 
        'raise' (raise an exception), by default 'raise'
    """

    def __init__(self,
                 columns: List[str],
                 conditions: Dict[tuple, Union[_BaseValueFormatter, _BaseCellRenderer]],
                 if_col_not_exist: Literal['ignore', 'raise'] = 'raise') -> None:
        super().__init__(columns=columns)
        self.conditions = conditions
        self.if_col_not_exist = if_col_not_exist

    def format(self,
               columnDefs_dict,
               **kwargs):
        for col in self.columns:
            if self.if_col_not_exist == 'ignore' and col not in columnDefs_dict:
                continue
            func_args = []
            for (condition_col, condition_value), format in self.conditions.items():
                format_function = format._create_format_function()
                func_args.append(
                    f'params.data["{condition_col}"], {
                        condition_value}, {format_function}'
                )
            func = f'conditionalFormat({",".join(func_args)})'
            columnDefs_dict[col] = {
                **columnDefs_dict[col],
                "valueFormatter": {
                    "function": func
                },
            }
        return columnDefs_dict
