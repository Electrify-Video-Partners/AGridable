import pytest
from unittest.mock import MagicMock
from agridable.formatters.row_formatter import RowFormatter
from agridable.formats._base import _BaseFormat


def test_rowformatter_init():
    rows = [0, 1, 2]
    formats = [MagicMock(spec=_BaseFormat)]
    formatter = RowFormatter(rows, formats)
    assert formatter.rows == rows
    assert formatter.formats == formats


def test_rowformatter_format():
    rows = [0, 1]
    formats = [MagicMock(spec=_BaseFormat)]
    formatter = RowFormatter(rows, formats)
    getRowStyleConditions_dict = {
        0: {
            'condition': 'params.node.rowIndex === 0',
            'style': {'color': 'red'}
        }
    }
    for fmt in formats:
        fmt.create_row_config.return_value = {
            'style': {'backgroundColor': 'blue'}
        }
    formatted_dict = formatter.format(getRowStyleConditions_dict)
    assert formatted_dict[0]['style']['color'] == 'red'
    assert formatted_dict[0]['style']['backgroundColor'] == 'blue'
    assert 'condition' in formatted_dict[0]
    assert formatted_dict[1]['style']['backgroundColor'] == 'blue'
    assert 'condition' in formatted_dict[1]


def test_rowformatter_format_single_row_single_format():
    rows = 0
    formats = MagicMock(spec=_BaseFormat)
    formatter = RowFormatter(rows, formats)
    getRowStyleConditions_dict = {}

    formats.create_row_config.return_value = {
        'style': {'backgroundColor': 'green'}
    }

    formatted_dict = formatter.format(getRowStyleConditions_dict)
    assert formatted_dict[0]['style']['backgroundColor'] == 'green'
    assert 'condition' in formatted_dict[0]


def test_rowformatter_format_multiple_rows_multiple_formats():
    rows = [0, 1]
    formats = [MagicMock(spec=_BaseFormat), MagicMock(spec=_BaseFormat)]
    formatter = RowFormatter(rows, formats)
    getRowStyleConditions_dict = {}

    formats[0].create_row_config.return_value = {
        'style': {'backgroundColor': 'green'}
    }
    formats[1].create_row_config.return_value = {
        'style': {'color': 'yellow'}
    }

    formatted_dict = formatter.format(getRowStyleConditions_dict)
    assert formatted_dict[0]['style']['backgroundColor'] == 'green'
    assert formatted_dict[0]['style']['color'] == 'yellow'
    assert 'condition' in formatted_dict[0]
    assert formatted_dict[1]['style']['backgroundColor'] == 'green'
    assert formatted_dict[1]['style']['color'] == 'yellow'
    assert 'condition' in formatted_dict[1]
