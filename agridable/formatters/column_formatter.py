from typing import List, Literal, Dict

from ._base import _BaseColumnFormatter
from ..formats._base import _BaseFormat
from ..formats.cell._base import _BaseCellFormat
from ..formats.conditional._base import _BaseConditionalFormat
from ..formats.grid._base import _BaseGridFormat
from ..formats.value._base import _BaseCellRenderer, _BaseValueFormatter

FORMAT_TYPE_ORDER = [
    # Apply conditional format first, since need to add other formats into
    # styleConditions after (if present)
    _BaseConditionalFormat,
    _BaseValueFormatter,
    _BaseCellRenderer,
    _BaseCellFormat,
    _BaseGridFormat
]


class ColumnFormatter(_BaseColumnFormatter):
    """
    Formats the given columns with the provided formats.

    Parameters
    ----------
    col_formats : Dict[str, List[_BaseFormat]]
        The column-wise formats to apply. A given key should be a column; a
        given value should be the list of formats to apply to that column.
    if_col_not_exist : Literal['ignore', 'raise'], optional
        The behaviour when a column is not found in the dataframe that is 
        listed in `col_formats`; either 'ignore' (don't do anything) or 
        'raise' (raise an exception), by default 'raise'
    """

    def __init__(self,
                 col_formats: Dict[str, List[_BaseFormat]],
                 if_col_not_exist: Literal['ignore', 'raise'] = 'raise') -> None:

        self.col_formats = col_formats
        self.if_col_not_exist = if_col_not_exist

    def format(self,
               columnDefs_dict,
               df):
        for col, formats in self.col_formats.items():
            # Ignore missing columns if if_col_not_exist == 'ignore'
            if self.if_col_not_exist == 'ignore' and col not in columnDefs_dict:
                continue
            # If one format given, convert to list
            if not isinstance(formats, (list, set, tuple)):
                formats = [formats]
            # Order formats
            formats = sorted(formats, key=self._type_index)
            for format in formats:
                # Create the config using the format class
                format_config = format.create_col_config(
                    col_df=df[col]
                )
                # Iterate through the formatting config and update
                # columnDefs_dict
                columnDefs_dict = self._update_columnDefs_dict(
                    format_config=format_config,
                    columnDefs_dict=columnDefs_dict,
                    col=col
                )
                # If conditional formats have already been applied, update the
                # styleConditions style components with the current format
                # (otherwise only the conditional formatting is seen)
                columnDefs_dict = self._update_styleConditions(
                    format=format,
                    format_config=format_config,
                    columnDefs_dict=columnDefs_dict,
                    col=col,
                )
        return columnDefs_dict

    @staticmethod
    def _update_columnDefs_dict(format_config,
                                columnDefs_dict,
                                col):
        for param in format_config:
            if param in columnDefs_dict[col]:
                columnDefs_dict[col][param] = {
                    **columnDefs_dict[col][param],
                    **format_config[param]
                }
            else:
                columnDefs_dict[col][param] = format_config[param]
        return columnDefs_dict

    @staticmethod
    def _update_styleConditions(format,
                                format_config,
                                columnDefs_dict,
                                col):
        format_not_conditional = not isinstance(format, _BaseConditionalFormat)
        # Use {} when key not found (will be falsey)
        format_config_has_cell_style = format_config.get('cellStyle', {})
        columnDefs_dict_has_style_conds = columnDefs_dict[col].get(
            'cellStyle', {}
        ).get('styleConditions', {})
        if format_not_conditional and format_config_has_cell_style and columnDefs_dict_has_style_conds:
            for cond in columnDefs_dict[col]['cellStyle']['styleConditions']:
                cond['style'] = {
                    **cond['style'],
                    **format_config['cellStyle']
                }
            # Also add as non-conditional formats as defaultStyle (so any
            # cells that don't meet conditions still have format applied)
            columnDefs_dict[col]['cellStyle']['defaultStyle'] = format_config['cellStyle']
        return columnDefs_dict

    @staticmethod
    def _type_index(obj):
        for i, format_type in enumerate(FORMAT_TYPE_ORDER):
            if isinstance(obj, format_type):
                return i
        # If the type is not found in type_order, place it at the end
        return len(FORMAT_TYPE_ORDER)
