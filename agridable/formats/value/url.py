from agridable.formats.value._base import _BaseCellRenderer


class Url(_BaseCellRenderer):
    """
    Sets the format to a clickable URL.
    """

    cell_renderer = 'formatUrl'

    def __init__(self):
        pass
