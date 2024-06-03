<p align="center">
  <img src=agridable_logo.svg width="500"/>
</p>

**AGridable** is a Python library which makes formatting tables in your Dash 
app a breeze 💨

It's a wrapper for the wonderful [Dash AG Grid](https://github.com/plotly/dash-ag-grid) 
library and enables users to quickly and easily apply formatting, without having to go through the (sometimes rather complex) process of configuration. 

For example, you can quickly and easily apply conditional colour formatting based on the range of values in a column.

The project was created by [James Laidler](https://github.com/lamesjaidler) 
whilst working at [Electrify Video Partners](https://electrify.video/).

# Quickstart

## Install AGridable

First, it's good practice to create a virtual environment to install **AGridable** into; here, we're using conda:

```bash
conda create -n agridable python=3.12
```

Once the environment is created, activate it:

```bash
conda activate agridable
```

Then install the AGridable library:

```bash
pip install agridable
```

## Use AGridable

The best way to get started with **AGridable** is to look at the examples in the [examples](./examples) folder. These contain simple Dash apps that showcase how **AGridable** can be used to quickly and easily format a dataframe.

To run these examples, first ensure you have the virtual environment where you installed AGridable activated (here, we're using the virtual environment created in the [Install Python Library](#install-python-library) step):

```bash
conda activate agridable
```

Then, clone the repo (here, we clone it to the home directory):

```bash
# cd to home directory
cd
# Clone repo
git clone https://github.com/Electrify-Video-Partners/AGridable.git
```

Finally, run one of the examples (here, we're running the `simple_example.py`):

```bash
python AGridable/examples/simple_example.py
```

This should start a Flask server running the example Dash app; navigate to the URL where the server is running in your browser to see the app.

# Contributing to AGridable

Contributing to **AGridable** is actively encouraged; we'd love to see more functionality added to the library! For steps on how to contribute, see the [contributing doc](./CONTRIBUTING.md).
