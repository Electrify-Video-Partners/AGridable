import pytest

from agridable.formats.cell import Align, HeaderAlign


def test_align_init_default():
    align = Align()
    assert align.h_align == 'center'
    assert align.v_align == 'center'


def test_align_init_custom():
    align = Align(h_align='left', v_align='start')
    assert align.h_align == 'left'
    assert align.v_align == 'start'


def test_align_create_col_config_default():
    align = Align()
    expected_config = {
        'cellStyle': {
            'textAlign': 'center',
            'justifyContent': 'center',
            'display': 'flex',
            'alignItems': 'center',
        }
    }
    assert align.create_col_config() == expected_config


def test_align_create_col_config_custom():
    align = Align(h_align='right', v_align='end')
    expected_config = {
        'cellStyle': {
            'textAlign': 'right',
            'justifyContent': 'right',
            'display': 'flex',
            'alignItems': 'end',
        }
    }
    assert align.create_col_config() == expected_config


def test_align_create_row_config():
    align = Align()
    with pytest.raises(NotImplementedError):
        align.create_row_config()


def test_headeralign_init_default():
    header_align = HeaderAlign()
    assert header_align.alignment == 'center'


def test_headeralign_init_custom():
    header_align = HeaderAlign(alignment='left')
    assert header_align.alignment == 'left'


def test_headeralign_create_col_config_default():
    header_align = HeaderAlign()
    expected_config = {
        'headerClass': 'center-aligned-header'
    }
    assert header_align.create_col_config() == expected_config


def test_headeralign_create_col_config_custom():
    header_align = HeaderAlign(alignment='right')
    expected_config = {
        'headerClass': 'right-aligned-header'
    }
    assert header_align.create_col_config() == expected_config


def test_headeralign_create_row_config():
    header_align = HeaderAlign()
    with pytest.raises(NotImplementedError):
        header_align.create_row_config()
