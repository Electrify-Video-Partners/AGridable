import pandas as pd
from unittest.mock import MagicMock

from agridable.formatters.column_formatter import (
    ColumnFormatter,
    FORMAT_TYPE_ORDER
)
from agridable.formats._base import _BaseFormat
from agridable.formats.cell._base import _BaseCellFormat
from agridable.formats.conditional._base import _BaseConditionalFormat
from agridable.formats.grid._base import _BaseGridFormat
from agridable.formats.value._base import (
    _BaseCellRenderer,
    _BaseValueFormatter
)


def test_columnformatter_init_default():
    col_formats = {
        "col1": [MagicMock(spec=_BaseFormat)]
    }
    column_formatter = ColumnFormatter(col_formats)
    assert column_formatter.col_formats == col_formats
    assert column_formatter.if_col_not_exist == 'raise'


def test_columnformatter_init_custom():
    col_formats = {
        "col1": [MagicMock(spec=_BaseFormat)]
    }
    column_formatter = ColumnFormatter(
        col_formats,
        if_col_not_exist='ignore'
    )
    assert column_formatter.col_formats == col_formats
    assert column_formatter.if_col_not_exist == 'ignore'


def test_columnformatter_format():
    expected_columnDefs_dict = {
        'col1': {
            'cellStyle': {
                'color': 'red',
                'defaultStyle': {'color': 'red'},
                'styleConditions': [
                    {
                        'condition': 'params.value == 1',
                        'style': {
                            'backgroundColor': 'black',
                            'color': 'red'
                        }
                    }
                ]
            }
        },
        'col2': {}
    }
    # Create mock formats
    cell_format = MagicMock(spec=_BaseCellFormat)
    cell_format.create_col_config.return_value = {
        "cellStyle": {"color": "red"}
    }
    cond_format = MagicMock(spec=_BaseConditionalFormat)
    cond_format.create_col_config.return_value = {
        "cellStyle": {
            'styleConditions': [
                {
                    "condition": "params.value == 1",
                    "style": {
                        "backgroundColor": 'black',
                    }
                }
            ]
        }
    }
    # Create col_formats
    col_formats = {
        "col1": [
            cell_format,
            cond_format
        ]
    }
    # Create ColumnFormatter and necessary params
    column_formatter = ColumnFormatter(col_formats)
    columnDefs_dict = {
        "col1": {},
        "col2": {}
    }
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })
    formatted_dict = column_formatter.format(columnDefs_dict, df)
    assert formatted_dict == expected_columnDefs_dict


def test_columnformatter_format_ignore_missing_columns():
    col_formats = {
        "col3": [MagicMock(spec=_BaseFormat)]
    }
    column_formatter = ColumnFormatter(col_formats, if_col_not_exist='ignore')
    columnDefs_dict = {"col1": {}, "col2": {}}
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })

    formatted_dict = column_formatter.format(columnDefs_dict, df)
    assert "col3" not in formatted_dict


def test_update_columnDefs_dict():
    format_config = {"cellStyle": {"color": "red"}}
    columnDefs_dict = {"col1": {"cellStyle": {"backgroundColor": "blue"}}}
    updated_dict = ColumnFormatter._update_columnDefs_dict(
        format_config, columnDefs_dict, "col1")
    assert updated_dict["col1"]["cellStyle"]["color"] == "red"
    assert updated_dict["col1"]["cellStyle"]["backgroundColor"] == "blue"


def test_update_styleConditions():
    format = MagicMock(spec=_BaseCellFormat)
    format_config = {"cellStyle": {"color": "red"}}
    columnDefs_dict = {"col1": {"cellStyle": {
        "styleConditions": [{"style": {"backgroundColor": "blue"}}]}}}
    updated_dict = ColumnFormatter._update_styleConditions(
        format, format_config, columnDefs_dict, "col1")
    assert updated_dict["col1"]["cellStyle"]["styleConditions"][0]["style"]["color"] == "red"
    assert updated_dict["col1"]["cellStyle"]["styleConditions"][0]["style"]["backgroundColor"] == "blue"
    assert updated_dict["col1"]["cellStyle"]["defaultStyle"]["color"] == "red"


def test_type_index():
    column_formatter = ColumnFormatter({"col1": [MagicMock(spec=_BaseFormat)]})
    obj = MagicMock(spec=_BaseCellFormat)
    assert (
        column_formatter._type_index(obj) ==
        FORMAT_TYPE_ORDER.index(_BaseCellFormat)
    )
    obj = MagicMock(spec=_BaseConditionalFormat)
    assert (
        column_formatter._type_index(obj) ==
        FORMAT_TYPE_ORDER.index(_BaseConditionalFormat)
    )
    obj = MagicMock(spec=_BaseValueFormatter)
    assert (
        column_formatter._type_index(obj) ==
        FORMAT_TYPE_ORDER.index(_BaseValueFormatter)
    )
    obj = MagicMock(spec=_BaseCellRenderer)
    assert (
        column_formatter._type_index(obj) ==
        FORMAT_TYPE_ORDER.index(_BaseCellRenderer)
    )
    obj = MagicMock(spec=_BaseGridFormat)
    assert (
        column_formatter._type_index(obj) ==
        FORMAT_TYPE_ORDER.index(_BaseGridFormat)
    )
    obj = MagicMock(spec=_BaseFormat)
    assert column_formatter._type_index(obj) == len(FORMAT_TYPE_ORDER)
