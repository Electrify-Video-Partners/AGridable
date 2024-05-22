from agridable.formats.value._base import _BaseCellRenderer


class Image(_BaseCellRenderer):
    """
    Sets the format to a rendered image.
    """

    cell_renderer = 'formatImg'

    def __init__(self):
        pass
