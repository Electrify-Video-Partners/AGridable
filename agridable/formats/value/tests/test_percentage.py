import pytest
from agridable.formats.value._base import PRECISION_TYPE_JS_MAP
from agridable.formats.value import Percentage


def test_percentage_init_default():
    percentage = Percentage()
    assert percentage.precision == 2
    assert percentage.precision_type == 'dp'
    assert percentage.precision_type_js == PRECISION_TYPE_JS_MAP['dp']
    assert percentage.is_decimal is True
    assert percentage.is_decimal_js == 'true'


def test_percentage_init_custom():
    percentage = Percentage(
        precision=3,
        precision_type='sf',
        is_decimal=False
    )
    assert percentage.precision == 3
    assert percentage.precision_type == 'sf'
    assert percentage.precision_type_js == PRECISION_TYPE_JS_MAP['sf']
    assert percentage.is_decimal is False
    assert percentage.is_decimal_js == 'false'


def test_percentage_create_format_function_default():
    percentage = Percentage()
    expected_function = 'formatPercentage(params.value, 2, "f", true)'
    assert percentage._create_format_function() == expected_function


def test_percentage_create_format_function_custom():
    percentage = Percentage(
        precision=1,
        precision_type='sf',
        is_decimal=False
    )
    expected_function = 'formatPercentage(params.value, 1, "r", false)'
    assert percentage._create_format_function() == expected_function


if __name__ == '__main__':
    pytest.main()
