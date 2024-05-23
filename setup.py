# Authors: James Laidler <james.a.laidler@gmail.com>
import setuptools
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
    version="0.0.0",
    author="James Laidler",
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
)
