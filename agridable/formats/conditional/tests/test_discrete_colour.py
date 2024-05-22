import pytest

from agridable.formats.conditional import DiscreteColour


def test_discretecolour_init():
    conditions = {"<x> > 0": "#00FF00", "<x> < 0": "#FF0000"}
    discrete_colour = DiscreteColour(conditions)
    assert discrete_colour.conditions == conditions


def test_discretecolour_create_col_config():
    conditions = {"<x> > 0": "#00FF00", "<x> < 0": "#FF0000"}
    discrete_colour = DiscreteColour(conditions)
    expected_config = {
        'cellStyle': {
            'styleConditions': [
                {
                    "condition": "params.value > 0",
                    "style": {
                        "backgroundColor": "#00FF00",
                    },
                },
                {
                    "condition": "params.value < 0",
                    "style": {
                        "backgroundColor": "#FF0000",
                    },
                },
            ]
        }
    }
    assert discrete_colour.create_col_config() == expected_config


def test_discretecolour_create_col_config_empty_conditions():
    conditions = {}
    discrete_colour = DiscreteColour(conditions)
    expected_config = {
        'cellStyle': {
            'styleConditions': []
        }
    }
    assert discrete_colour.create_col_config() == expected_config


def test_discretecolour_create_row_config():
    conditions = {"<x> > 0": "#00FF00"}
    discrete_colour = DiscreteColour(conditions)
    with pytest.raises(NotImplementedError):
        discrete_colour.create_row_config()
