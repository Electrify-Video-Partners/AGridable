import pytest
import pandas as pd

from agridable.formats.conditional import ContinuousColour


def test_continuouscolour_init_default():
    continuous_colour = ContinuousColour(
        min_colour='#000000',
        max_colour='#FFFFFF'
    )
    assert continuous_colour.min_colour == '#000000'
    assert continuous_colour.max_colour == '#FFFFFF'
    assert continuous_colour.mid_colour is None
    assert continuous_colour.min_point is None
    assert continuous_colour.mid_point is None
    assert continuous_colour.max_point is None


def test_continuouscolour_init_custom():
    continuous_colour = ContinuousColour(
        min_colour='#000000',
        max_colour='#FFFFFF',
        mid_colour='#888888',
        min_point=0,
        mid_point=50,
        max_point=100
    )
    assert continuous_colour.min_colour == '#000000'
    assert continuous_colour.max_colour == '#FFFFFF'
    assert continuous_colour.mid_colour == '#888888'
    assert continuous_colour.min_point == 0
    assert continuous_colour.mid_point == 50
    assert continuous_colour.max_point == 100


def test_continuouscolour_create_col_config_default():
    df = pd.Series([1, 2, 3, 4, 5])
    continuous_colour = ContinuousColour(
        min_colour='#000000',
        max_colour='#FFFFFF'
    )
    config = continuous_colour.create_col_config(df)
    assert 'cellStyle' in config
    assert 'styleConditions' in config['cellStyle']
    assert len(config['cellStyle']['styleConditions']) == len(df.unique())


def test_continuouscolour_create_col_config_empty():
    df = pd.Series([])
    continuous_colour = ContinuousColour(
        min_colour='#000000',
        max_colour='#FFFFFF'
    )
    config = continuous_colour.create_col_config(df)
    assert config == {}


def test_continuouscolour_create_row_config():
    continuous_colour = ContinuousColour(
        min_colour='#000000',
        max_colour='#FFFFFF'
    )
    with pytest.raises(NotImplementedError):
        continuous_colour.create_row_config()


def test_interpolate_colour_no_mid_colour():
    colour = ContinuousColour._interpolate_colour(
        value=50,
        min_point=0,
        max_point=100,
        min_colour='#000000',
        max_colour='#FFFFFF',
        mid_colour=None,
        mid_point=50
    )
    assert colour == '#7f7f7fff'


def test_interpolate_colour_with_mid_colour():
    colour = ContinuousColour._interpolate_colour(
        value=25,
        min_point=0,
        max_point=100,
        min_colour='#000000',
        max_colour='#FFFFFF',
        mid_colour='#888888',
        mid_point=50
    )
    assert colour == '#444444ff'


def test_interpolate_colour_mid_point():
    colour = ContinuousColour._interpolate_colour(
        value=50,
        min_point=0,
        max_point=100,
        min_colour='#000000',
        max_colour='#FFFFFF',
        mid_colour='#888888',
        mid_point=50
    )
    assert colour == '#888888ff'
