import pytest
import pandas as pd
from unittest.mock import MagicMock
from agridable.formatters import ConditionalColumnFormatter
from agridable.formats.value._base import _BaseValueFormatter, _BaseCellRenderer


def test_conditionalcolumnformatter_init_default():
    columns = ["col1", "col2"]
    conditions = {("col1", 1): MagicMock(spec=_BaseValueFormatter)}
    formatter = ConditionalColumnFormatter(columns, conditions)
    assert formatter.columns == columns
    assert formatter.conditions == conditions
    assert formatter.if_col_not_exist == 'raise'


def test_conditionalcolumnformatter_init_custom():
    columns = ["col1", "col2"]
    conditions = {("col1", 1): MagicMock(spec=_BaseValueFormatter)}
    formatter = ConditionalColumnFormatter(
        columns, conditions, if_col_not_exist='ignore')
    assert formatter.columns == columns
    assert formatter.conditions == conditions
    assert formatter.if_col_not_exist == 'ignore'


def test_conditionalcolumnformatter_format():
    expected_columnDefs_dict = {
        'col1': {
            'valueFormatter': {
                'function': 'conditionalFormat(params.data["col1"], '
                '1, formatFunction())'
            }
        },
        'col2': {}
    }
    columns = ["col1"]
    conditions = {("col1", 1): MagicMock(spec=_BaseValueFormatter)}
    formatter = ConditionalColumnFormatter(columns, conditions)
    columnDefs_dict = {"col1": {}, "col2": {}}
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })

    for condition, fmt in conditions.items():
        fmt._create_format_function.return_value = "formatFunction()"

    formatted_dict = formatter.format(columnDefs_dict, df=df)
    assert formatted_dict == expected_columnDefs_dict


def test_conditionalcolumnformatter_format_ignore_missing_columns():
    columns = ["col3"]
    conditions = {("col3", 1): MagicMock(spec=_BaseValueFormatter)}
    formatter = ConditionalColumnFormatter(
        columns, conditions, if_col_not_exist='ignore')
    columnDefs_dict = {"col1": {}, "col2": {}}
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })

    formatted_dict = formatter.format(columnDefs_dict, df=df)
    assert "col3" not in formatted_dict


if __name__ == '__main__':
    pytest.main()
