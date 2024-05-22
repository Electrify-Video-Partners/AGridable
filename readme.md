<p align="center">
  <img src=agridable_logo.svg width="500"/>
</p>

**AGridable** is a Python library which makes formatting tables in your Dash 
app a breeze.

It's a wrapper for the wonderful [Dash AG Grid](https://github.com/plotly/dash-ag-grid) 
library and enables users to quickly and easily apply formatting that is 
featured mainly in the likes of Excel without having to go through the 
(sometimes rather complex) process of configuration.

The project was created by [James Laidler](https://github.com/lamesjaidler) 
whilst working at [Electrify Video Partners](https://electrify.video/).

# Quickstart

## Install Python Library

First, install the Python library (preferably into a virtual environment):

```base
pip install agridable
```

## Transfer JS and CSS files

**AGridable** relies on some standard Javascript functions and CSS formats; 
these can be found in the `./agridable/assets` folder. You must either:

1) Copy these files into the assets folder of your site, or; 
2) If you already have versions of these files, append the functions and 
formats in these files to the relevant files of your site.

## Using AGridable

The best way to get started with **AGridable** is to look at the examples in 
the `./examples` folder.

# Contributing

