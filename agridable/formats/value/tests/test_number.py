import pytest
from agridable.formats.value._base import PRECISION_TYPE_JS_MAP
from agridable.formats.value import Number


def test_number_init_default():
    number = Number()
    assert number.precision == 2
    assert number.precision_type == 'dp'
    assert number.precision_type_js == PRECISION_TYPE_JS_MAP['dp']
    assert number.unit_scale is None
    assert number.prefix is None
    assert number.suffix is None
    assert number.prefix_js == "null"
    assert number.suffix_js == "null"


def test_number_init_custom():
    number = Number(
        precision=3,
        precision_type='sf',
        unit_scale='millions',
        prefix='$',
        suffix='%'
    )
    assert number.precision == 3
    assert number.precision_type == 'sf'
    assert number.precision_type_js == PRECISION_TYPE_JS_MAP['sf']
    assert number.unit_scale == 'millions'
    assert number.prefix == '$'
    assert number.suffix == '%'
    assert number.prefix_js == '$'
    assert number.suffix_js == '%'


def test_number_create_format_function_default():
    number = Number()
    expected_function = 'formatNumberPrefixSuffix(params.value, null, null, "None", 2, "f")'
    assert number._create_format_function() == expected_function


def test_number_create_format_function_custom():
    number = Number(
        precision=1,
        precision_type='sf',
        unit_scale='thousands',
        prefix='"€"',
        suffix='"kg"'
    )
    expected_function = 'formatNumberPrefixSuffix(params.value, "€", "kg", "thousands", 1, "r")'
    assert number._create_format_function() == expected_function


if __name__ == '__main__':
    pytest.main()
