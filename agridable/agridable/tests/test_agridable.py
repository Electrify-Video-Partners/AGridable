import pytest
import pandas as pd
from unittest.mock import MagicMock

from agridable.agridable import AGridable
from agridable.formatters._base import (
    _BaseFormatter,
    _BaseColumnFormatter,
    _BaseRowFormatter
)


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })


@pytest.fixture
def sample_formatters():
    column_formatter = MagicMock(spec=_BaseColumnFormatter)
    column_formatter.format.return_value = {
        'A': {'field': 'A', 'formatted': True},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    row_formatter = MagicMock(spec=_BaseRowFormatter)
    row_formatter.format.return_value = {
        'styleConditions': [{'condition': 'row_condition'}]
    }
    return [column_formatter, row_formatter]


def test_agridable_init(sample_dataframe, sample_formatters):
    grid = AGridable(df=sample_dataframe, formatters=sample_formatters)

    assert isinstance(grid, AGridable)
    assert 'rowData' in grid.__dict__
    assert 'columnDefs' in grid.__dict__
    assert 'getRowStyle' in grid.__dict__
    assert grid.rowData == sample_dataframe.to_dict('records')
    assert 'field' in grid.columnDefs[0]
    assert 'styleConditions' in grid.getRowStyle


def test_create_columnDefs_dict_all_columns(sample_dataframe):
    expected_dict = {
        'A': {'field': 'A'},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    result = AGridable._create_columnDefs_dict(sample_dataframe, None)
    assert result == expected_dict


def test_create_columnDefs_dict_specific_columns(sample_dataframe):
    columns = ['A', 'C']
    expected_dict = {
        'A': {'field': 'A'},
        'C': {'field': 'C'}
    }
    result = AGridable._create_columnDefs_dict(sample_dataframe, columns)
    assert result == expected_dict


def test_apply_formatters(sample_dataframe, sample_formatters):
    columnDefs_dict = {
        'A': {'field': 'A'},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    getRowStyleConditions_dict = {}

    expected_columnDefs_dict = {
        'A': {'field': 'A', 'formatted': True},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    expected_getRowStyleConditions_dict = {
        'styleConditions': [{'condition': 'row_condition'}]
    }

    columnDefs_dict, getRowStyleConditions_dict = AGridable._apply_formatters(
        df=sample_dataframe,
        columnDefs_dict=columnDefs_dict,
        getRowStyleConditions_dict=getRowStyleConditions_dict,
        formatters=sample_formatters
    )

    assert columnDefs_dict == expected_columnDefs_dict
    assert getRowStyleConditions_dict == expected_getRowStyleConditions_dict


def test_apply_formatters_no_formatters(sample_dataframe):
    columnDefs_dict = {
        'A': {'field': 'A'},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    getRowStyleConditions_dict = {}

    result_columnDefs_dict, result_getRowStyleConditions_dict = AGridable._apply_formatters(
        df=sample_dataframe,
        columnDefs_dict=columnDefs_dict,
        getRowStyleConditions_dict=getRowStyleConditions_dict,
        formatters=None
    )

    assert result_columnDefs_dict == columnDefs_dict
    assert result_getRowStyleConditions_dict == getRowStyleConditions_dict


def test_apply_formatters_invalid_formatters(sample_dataframe):
    columnDefs_dict = {
        'A': {'field': 'A'},
        'B': {'field': 'B'},
        'C': {'field': 'C'}
    }
    getRowStyleConditions_dict = {}

    invalid_formatter = MagicMock(spec=_BaseFormatter)

    result_columnDefs_dict, result_getRowStyleConditions_dict = AGridable._apply_formatters(
        df=sample_dataframe,
        columnDefs_dict=columnDefs_dict,
        getRowStyleConditions_dict=getRowStyleConditions_dict,
        formatters=[invalid_formatter]
    )

    assert result_columnDefs_dict == columnDefs_dict
    assert result_getRowStyleConditions_dict == getRowStyleConditions_dict


if __name__ == '__main__':
    pytest.main()
