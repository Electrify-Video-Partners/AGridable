"""
Intermediate example showing how AGridable can be used to apply column-wise 
formatting (based on values in another column) to a grid.

To run the example, you should call the file from the terminal via the command
(assuming you're in the AGridable folder):

python examples/intermediate_example.py
"""

# Standard imports
import pandas as pd
from dash import html
import dash

# AGridable imports
from agridable.agridable import (
    AGridable
)
from agridable.formats.conditional import (
    ContinuousColour,
    DiscreteColour
)
from agridable.formats.cell import (
    Align,
    Border
)
from agridable.formats.value import (
    Percentage,
    Currency,
    Number
)
from agridable.formatters import (
    ColumnFormatter,
    ConditionalColumnFormatter,
    RowFormatter
)

# Create a sample dataframe with dummy data
data = [
    ['Impressions', 100000, 90000, -10000, -0.1],
    ['Visits', 1000, 1100, 100, 0.1],
    ['Purchases', 120, 180, 60, 0.5],
    ['Revenue', 54000, 70000, 16000, 0.2962962963]
]
data = pd.DataFrame(
    data,
    columns=[
        'Metric',
        '2022',
        '2023',
        'Year-on-year Change',
        'Year-on-year % Change'
    ],
)

# Create conditional column formatter (format `2022`, `2023` and `Year-on-year
# Change` columns dependent on the values in the `Metric` column)
COND_COL_FORMATTER = ConditionalColumnFormatter(
    columns=[
        '2022',
        '2023',
        'Year-on-year Change'
    ],
    conditions={
        # If `Metric`=="Impressions", use number format (in thousands to 1
        # decimal place)
        ('Metric', '"Impressions"'): Number(
            unit_scale='thousands',
            precision=1
        ),
        # If `Metric`=="Visits", use number format (in thousands to 1 decimal
        # place)
        ('Metric', '"Visits"'): Number(
            unit_scale='thousands',
            precision=1
        ),
        # If `Metric`=="Revenue", use currency format (in thousands of GBP to 0
        # decimal places)
        ('Metric', '"Revenue"'): Currency(
            currency='GBP',
            unit_scale='thousands',
            precision=0
        )
    }
)

# Create dictionary which configures formats to be applied across each column
COL_FORMATS = {
    # Format `Year-on-year Change` with center alignment and conditional colour
    # formatting (where negative values are coloured red; positive values are
    # coloured green)
    'Year-on-year Change': [
        Align(h_align='center'),
        DiscreteColour(
            conditions={
                '<x> > 0': '#57bb8a',
                '<x> <= 0': '#e67c73'
            }
        )
    ],
    # Format `Year-on-year % Change` with center alignment, as percentage and
    # conditional colour formatting (where higher is better)
    'Year-on-year % Change': [
        Align(h_align='center'),
        Percentage(),
        ContinuousColour(
            min_colour='#e67c73',
            mid_colour='#57bb8a00',  # transparent
            max_colour='#57bb8a',
            mid_point=0  # < 0 will be red shades; > 0 will be green shades
        )
    ]
}
# Create ColumnFormatter with the column format configuration
COL_FORMATTER = ColumnFormatter(
    col_formats=COL_FORMATS
)

# Create RowFormatter to apply a border below the `Metric`=='Purchases' row (to
# distinguish website metrics from revenue metric)
ROW_FORMATTER = RowFormatter(
    rows=2,
    formats=Border(border_style='dotted')
)

# Create grid using AGridable (data + formatter)
table = AGridable(
    df=data,
    formatters=[
        COND_COL_FORMATTER,
        COL_FORMATTER,
        ROW_FORMATTER
    ]
)

# Initialize the Dash app
# IMPORTANT - you should set the `assets_folder` parameter to your assets
# folder, and copy the files from the `assets` folder in the AGridable parent
# directory into this folder
app = dash.Dash(
    __name__,
    assets_folder='..'  # Include `<parent>/agridable/assets` and `<parent>/examples/static`
)

# Define the layout of the app
app.layout = html.Div([
    html.H1("'The Chicken Shop' - 2022 vs 2023"),
    table,
    html.Hr(),
    html.Div(id='table-container')
])

if __name__ == '__main__':
    app.run(port=9999, debug=True)
