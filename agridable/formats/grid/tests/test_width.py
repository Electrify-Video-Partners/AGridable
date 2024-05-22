import pytest
from agridable.formats.grid import Width


def test_width_init_default():
    width = Width()
    assert width.width is None
    assert width.min_width is None
    assert width.max_width is None
    assert width.suppress_size_to_fit is True


def test_width_init_custom():
    width = Width(
        width=100,
        min_width=50,
        max_width=150,
        suppress_size_to_fit=False
    )
    assert width.width == 100
    assert width.min_width == 50
    assert width.max_width == 150
    assert width.suppress_size_to_fit is False


def test_width_create_col_config_default():
    width = Width()
    expected_config = {
        'width': None,
        'minWidth': None,
        'maxWidth': None,
        'suppressSizeToFit': True
    }
    assert width.create_col_config() == expected_config


def test_width_create_col_config_custom():
    width = Width(
        width=100,
        min_width=50,
        max_width=150,
        suppress_size_to_fit=False
    )
    expected_config = {
        'width': 100,
        'minWidth': 50,
        'maxWidth': 150,
        'suppressSizeToFit': False
    }
    assert width.create_col_config() == expected_config


def test_width_create_row_config():
    width = Width()
    with pytest.raises(NotImplementedError):
        width.create_row_config()


if __name__ == '__main__':
    pytest.main()
