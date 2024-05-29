from importlib.metadata import version

_css_dist = [
    {
        "relative_package_path": "assets/dashAgGridCss.css",
        "namespace": "agridable",
    }
]
_js_dist = [
    {
        "relative_package_path": "assets/dashAgGridFunctions.js",
        "namespace": "agridable",
    },
    {
        "relative_package_path": "assets/dashAgGridComponentFunctions.js",
        "namespace": "agridable",
    },
]

__version__ = version(__package__)

__all__ = ["__version__"]
