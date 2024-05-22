from agridable.formats.value import Url


def test_url_init():
    image = Url()
    assert image.cell_renderer == 'formatUrl'
