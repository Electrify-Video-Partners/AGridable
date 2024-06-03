# Authors: James Laidler <james.a.laidler@gmail.com>
import setuptools
# Create long description
long_description = """
**AGridable** is a Python library which makes formatting tables in your Dash 
app a breeze 💨

It's a wrapper for the wonderful [Dash AG Grid](https://github.com/plotly/dash-ag-grid) 
library and enables users to quickly and easily apply formatting, without having to go through the (sometimes rather complex) process of configuration. 

For example, you can quickly and easily apply conditional colour formatting based on the range of values in a column.

The project was created by [James Laidler](https://github.com/lamesjaidler) 
whilst working at [Electrify Video Partners](https://electrify.video/).
"""

INSTALL_REQUIRES = [
    'dash-ag-grid>=31.0.0,<32.0.0',
    'pandas>=2.0.0,<3.0.0',
]
EXTRAS_REQUIRE = {
    'dev': [
        'twine>=5.0.0,<6.0.0',
        'pytest>=8.2.1,<9.0.0'
    ]
}
setuptools.setup(
    name="agridable",
    version="0.0.3",
    author="James Laidler",
    url="https://github.com/Electrify-Video-Partners/AGridable",
    description="AGridable is a Python library which makes formatting tables in your Dash app a breeze.",
    packages=setuptools.find_packages(exclude=['examples']),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    long_description=long_description,
    long_description_content_type='text/markdown',

    include_package_data=True
)
