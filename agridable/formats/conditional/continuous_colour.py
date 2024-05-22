from typing import Union
import pandas as pd
import numpy as np

from agridable.formats.conditional._base import _BaseConditionalFormat


class ContinuousColour(_BaseConditionalFormat):
    """
    Applies a continuous colour spectrum to cells based on the minimum,
    midpoint and maximum values.

    Parameters
    ----------
    min_colour : str
        The colour of the minimum point (as a hex string).
    max_colour : str
        The colour of the maximum point (as a hex string).
    mid_colour : Union[str, None], optional
        The colour of the midpoint (as a hex string). If None, is
        calculated as the midpoint between min_colour and max_colour, by
        default None.
    min_point : Union[int, None], optional
        The minimum point. If None, is calculated as the minimum point in
        the column, by default None
    mid_point : Union[int, None], optional
        The midpoint. If None, is calculated as the midpoint between
        min_point and max_point, by default None
    max_point : Union[int, None], optional
        The maximum point. If None, is calculated as the maximum point in
        the column, by default None
    """

    def __init__(self,
                 min_colour: str,
                 max_colour: str,
                 mid_colour: Union[str, None] = None,
                 min_point: Union[int, None] = None,
                 mid_point: Union[int, None] = None,
                 max_point: Union[int, None] = None) -> None:

        super().__init__()
        self.min_colour = min_colour
        self.max_colour = max_colour
        self.mid_colour = mid_colour
        self.min_point = min_point
        self.mid_point = mid_point
        self.max_point = max_point

    def create_col_config(self,
                          col_df: pd.Series):
        unique_col_values = set(col_df[~col_df.isna()])
        # Sometimes there's still np.nan values remaining - explicitly filter
        # these out
        unique_col_values = {i for i in unique_col_values if not np.isnan(i)}
        if not unique_col_values:
            return {}
        styleConditions = []
        # Calculate min, mid and max points
        min_point = min(
            unique_col_values
        ) if self.min_point is None else self.min_point
        max_point = max(
            unique_col_values
        ) if self.max_point is None else self.max_point
        mid_point = (min_point + max_point) / 2
        # Calculate colours for each unique value and update styleConditions
        for col_value in unique_col_values:
            colour = self._interpolate_colour(
                value=col_value,
                min_point=min_point,
                max_point=max_point,
                min_colour=self.min_colour,
                max_colour=self.max_colour,
                mid_colour=self.mid_colour,
                mid_point=mid_point
            )
            styleConditions.append(
                {
                    "condition": f"params.value == {col_value}",
                    "style": {
                        "backgroundColor": colour,
                    },
                }
            )
        return {
            'cellStyle': {
                'styleConditions': styleConditions,
            }
        }

    def create_row_config(self,
                          *args,
                          **kwargs) -> dict:
        raise NotImplementedError

    @staticmethod
    def _interpolate_colour(value,
                            min_point,
                            max_point,
                            min_colour,
                            max_colour,
                            mid_colour,
                            mid_point):
        """
        Interpolates colour based on value between min and max using optional 
        midpoint colour.
        """
        if max_point == min_point:  # Prevent division by zero
            # Default to midpoint colour or minimum colour
            return mid_colour if mid_colour else min_colour

        def hex_to_rgba(hex_colour):
            """Convert hex colour to an RGBA tuple."""
            hex_colour = hex_colour.lstrip('#')
            if len(hex_colour) == 8:  # Includes alpha
                r, g, b, a = tuple(int(hex_colour[i:i+2], 16)
                                   for i in (0, 2, 4, 6))
            elif len(hex_colour) == 6:  # Standard RGB hex code
                r, g, b = tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))
                a = 255  # Default to fully opaque if alpha is not specified
            else:
                raise ValueError("Invalid hex colour format")
            return (r, g, b, a)

        def rgba_to_hex(rgb):
            """Convert RGB or RGBA tuple to hex colour."""
            if len(rgb) == 3:  # RGB without alpha
                return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
            elif len(rgb) == 4:  # RGBA with alpha
                return '#{:02x}{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]), int(rgb[3]))
            else:
                raise ValueError("Input must be an RGB or RGBA tuple")

        def colour_lerp_rgba(colour1, colour2, t):
            """Linearly interpolate between two RGBA colours."""
            if len(colour1) != len(colour2) or not (len(colour1) == 3 or len(colour1) == 4):
                raise ValueError(
                    "Both colours must be RGB or RGBA tuples of the same length")

            return tuple(colour1[i] + (colour2[i] - colour1[i]) * t for i in range(len(colour1)))

        # Convert hex to RGB
        min_colour = hex_to_rgba(min_colour)
        max_colour = hex_to_rgba(max_colour)
        # If a mid colour is provided
        if mid_colour:
            mid_colour = hex_to_rgba(mid_colour)
            if value == mid_point:
                return rgba_to_hex(mid_colour)
            elif value < mid_point:
                proportion = (value - min_point) / (mid_point - min_point)
                return rgba_to_hex(colour_lerp_rgba(min_colour, mid_colour, proportion))
            elif value > mid_point:
                proportion = (value - mid_point) / (max_point - mid_point)
                return rgba_to_hex(colour_lerp_rgba(mid_colour, max_colour, proportion))
        # If a mid colour isn't provided, use colour between min_colour and
        # max_colour
        else:
            if value <= mid_point:
                proportion = (value - min_point) / (mid_point - min_point)
                midpoint_colour = colour_lerp_rgba(
                    min_colour, max_colour, 0.5)  # Get colour at mid_point
                return rgba_to_hex(colour_lerp_rgba(min_colour, midpoint_colour, proportion))
            else:
                proportion = (value - mid_point) / (max_point - mid_point)
                midpoint_colour = colour_lerp_rgba(
                    min_colour, max_colour, 0.5)  # Get colour at mid_point
                return rgba_to_hex(colour_lerp_rgba(midpoint_colour, max_colour, proportion))
