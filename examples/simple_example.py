"""
Simple example showing how AGridable can be used to apply column-wise 
formatting to a grid.

To run the example, you should call the file from the terminal via the command
(assuming you're in the AGridable folder):

python examples/simple_example.py
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
from agridable.formats.grid import (
    Width,
)
from agridable.formats.cell import (
    Align,
    HeaderAlign
)
from agridable.formats.value import (
    Percentage,
    Currency,
    Url,
)
from agridable.formatters import (
    ColumnFormatter,
)

# Create a sample dataframe with dummy data
data = {
    "Product ID": [1, 2, 3, 4, 5],
    "Product Name": [
        'Chicken feed',
        'Chicken vitamins',
        'Chicken coop',
        'Chicken feeder',
        'Chicken waterer'
    ],
    "Product Description": [
        'High quality chicken feed for healthy chickens',
        'High quality chicken vitamins for healthy chickens',
        'Cozy chicken coop for comfy chickens',
        'Automatic chicken feeder for lazy people',
        'Automatic chicken waterer for lazy people',
    ],
    "Product Link": [
        'http://www.test.com',
        'http://www.test.com',
        'http://www.test.com',
        'http://www.test.com',
        'http://www.test.com'
    ],
    "Product Cost (£)": [
        12.99,
        9.99,
        99.99,
        10.99,
        10.99,
    ],
    "Quantity Ordered": [
        500,
        300,
        150,
        400,
        350
    ],
    "Total Order Amount (£)": [
        6495,
        2997,
        14998.5,
        4396,
        3846.5
    ],
    "Quantity Returned": [
        10,
        5,
        50,
        3,
        4
    ],
    "Total Return Amount (£)": [
        129.9,
        49.95,
        4999.5,
        32.97,
        43.96
    ],
    "Percentage Returned": [
        0.02,
        0.01666666667,
        0.3333333333,
        0.0075,
        0.01142857143,
    ],
    "High Return Rate (>30%)": [
        'No',
        'No',
        'Yes',
        'No',
        'No'
    ]
}
data = pd.DataFrame(data)

# Create conditional formats
HIGHER_BETTER_COND_FORMAT = ContinuousColour(
    min_colour='#57bb8a00',  # transparent
    max_colour='#57bb8a',
    min_point=0
)
HIGHER_WORSE_COND_FORMAT = ContinuousColour(
    min_colour='#e67c7300',  # transparent
    max_colour='#e67c73',
    min_point=0
)
HIGH_RETURN_RATE_COND_FORMAT = DiscreteColour(
    conditions={
        '<x> == "Yes"': '#e67c73'
    }
)

# Create dictionary which configures formats to be applied to each column
COL_FORMATS = {
    # Format `Product Link` column as clickable URL
    "Product Link": Url(),
    # Format `Product Description` column with left alignment and a width of
    # 300px
    "Product Description": [
        Align(h_align='left'),
        Width(width=300)
    ],
    # Format `Product Cost (£)` as GBP with penny precision
    "Product Cost (£)": Currency(
        currency='GBP',
        precision=2
    ),
    # Format `Quantity Ordered` with right aligment (including header) and
    # conditional colour formatting (where higher is better)
    "Quantity Ordered": [
        Align(h_align='right'),
        HeaderAlign(alignment='right'),
        HIGHER_BETTER_COND_FORMAT,
    ],
    # Format `Total Order Amount (£)` with right aligment (including header),
    # as GBP (in thousands) and conditional colour formatting (where higher is
    # better)
    "Total Order Amount (£)": [
        Currency(unit_scale='thousands'),
        Align(h_align='right'),
        HeaderAlign(alignment='right'),
        HIGHER_BETTER_COND_FORMAT
    ],
    # Format `Quantity Returned` with right aligment (including header) and
    # conditional colour formatting (where higher is worse)
    "Quantity Returned": [
        Align(h_align='right'),
        HeaderAlign(alignment='right'),
        HIGHER_WORSE_COND_FORMAT
    ],
    # Format `Total Return Amount (£)` with right aligment (including header),
    # as GBP (in thousands) and conditional colour formatting (where higher is
    # worse)
    "Total Return Amount (£)": [
        Currency(unit_scale='thousands'),
        Align(h_align='right'),
        HeaderAlign(alignment='right'),
        HIGHER_WORSE_COND_FORMAT
    ],
    # Format `Percentage Returned` with right aligment (including header), as
    # percentage and conditional colour formatting (where higher is worse)
    "Percentage Returned": [
        Align(h_align='right'),
        HeaderAlign(alignment='right'),
        Percentage(),
        HIGHER_WORSE_COND_FORMAT
    ],
    # Format `High Return Rate (>30%)` with center aligment and conditional
    # colour formatting (where values above 30% are coloured red)
    "High Return Rate (>30%)": [
        Align(h_align='center'),
        HIGH_RETURN_RATE_COND_FORMAT,
    ]
}

# Create ColumnFormatter with the column format configuration
COL_FORMATTER = ColumnFormatter(
    col_formats=COL_FORMATS
)

# Create grid using AGridable (data + formatter)
table = AGridable(
    df=data,
    formatters=COL_FORMATTER
)

# Initialize the Dash app
app = dash.Dash(
    __name__,
    assets_folder='./static'
)

# Define the layout of the app
app.layout = html.Div([
    html.H1("'The Chicken Shop' - March 2021 Sales"),
    table,
    html.Hr(),
    html.Div(id='table-container')
])

if __name__ == '__main__':
    app.run(debug=True)
