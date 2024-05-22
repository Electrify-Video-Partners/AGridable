from agridable.formats.value import Image


def test_image_init():
    image = Image()
    assert image.cell_renderer == 'formatImg'
