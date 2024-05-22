import pytest

from agridable.formats.grid import Pin


def test_pin_init_default():
    pin = Pin()
    assert pin.side == 'left'


def test_pin_init_custom():
    pin = Pin(side='right')
    assert pin.side == 'right'


def test_pin_create_col_config_default():
    pin = Pin()
    expected_config = {
        'pinned': 'left'
    }
    assert pin.create_col_config() == expected_config


def test_pin_create_col_config_custom():
    pin = Pin(side='right')
    expected_config = {
        'pinned': 'right'
    }
    assert pin.create_col_config() == expected_config


def test_pin_create_row_config():
    pin = Pin()
    with pytest.raises(NotImplementedError):
        pin.create_row_config()
