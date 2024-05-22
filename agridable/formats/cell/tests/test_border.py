import pytest

from agridable.formats.cell import Border


def test_border_init_default():
    border = Border()
    assert border.border_side == 'borderBottom'
    assert border.border_width == '1px'
    assert border.border_style == 'solid'
    assert border.border_colour == 'white'
    assert border.border_prop == '1px solid white'


def test_border_init_custom():
    border = Border(border_side='top', border_width='2px',
                    border_style='dashed', border_colour='black')
    assert border.border_side == 'borderTop'
    assert border.border_width == '2px'
    assert border.border_style == 'dashed'
    assert border.border_colour == 'black'
    assert border.border_prop == '2px dashed black'


def test_border_create_col_config_default():
    border = Border()
    expected_config = {
        'cellStyle': {
            'borderBottom': '1px solid white'
        }
    }
    assert border.create_col_config() == expected_config


def test_border_create_col_config_custom():
    border = Border(border_side='left', border_width='3px',
                    border_style='dotted', border_colour='blue')
    expected_config = {
        'cellStyle': {
            'borderLeft': '3px dotted blue'
        }
    }
    assert border.create_col_config() == expected_config


def test_border_create_row_config_default():
    border = Border()
    expected_config = {
        'style': {
            'borderBottom': '1px solid white'
        }
    }
    assert border.create_row_config() == expected_config


def test_border_create_row_config_custom():
    border = Border(border_side='right', border_width='4px',
                    border_style='double', border_colour='red')
    expected_config = {
        'style': {
            'borderRight': '4px double red'
        }
    }
    assert border.create_row_config() == expected_config
