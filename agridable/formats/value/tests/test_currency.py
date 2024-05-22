from agridable.formats.value._base import PRECISION_TYPE_JS_MAP
from agridable.formats.value import Currency


def test_currency_init_default():
    currency = Currency()
    assert currency.currency == 'USD'
    assert currency.precision == 2
    assert currency.precision_type == 'dp'
    assert currency.precision_type_js == PRECISION_TYPE_JS_MAP['dp']
    assert currency.unit_scale is None


def test_currency_init_custom():
    currency = Currency(
        currency='EUR',
        precision=3,
        precision_type='sf',
        unit_scale='millions'
    )
    assert currency.currency == 'EUR'
    assert currency.precision == 3
    assert currency.precision_type == 'sf'
    assert currency.precision_type_js == PRECISION_TYPE_JS_MAP['sf']
    assert currency.unit_scale == 'millions'


def test_currency_create_format_function_default():
    currency = Currency()
    expected_function = 'formatCurrency(params.value, "USD", "None", 2, "f")'
    assert currency._create_format_function() == expected_function


def test_currency_create_format_function_custom():
    currency = Currency(
        currency='JPY',
        precision=0,
        precision_type='sf',
        unit_scale='billions'
    )
    expected_function = 'formatCurrency(params.value, "JPY", "billions", 0, "r")'
    assert currency._create_format_function() == expected_function
