from typing import Dict

from agridable.formats.conditional._base import _BaseConditionalFormat


class DiscreteColour(_BaseConditionalFormat):
    """
    Applies discrete colours to cells based on a set of conditions.

    Parameters
    ----------
    conditions : Dict[str, str]
        The set of conditions to apply. A given key should be a stringified
        javascript condition, where the cell value placeholder is defined using 
        <x>; a given value should be the hex colour to apply if the condition 
        is met. For example, {"<x> > 0": "#00FF00"} would colour all cells 
        greater than 0 green.
    """

    def __init__(self,
                 conditions: Dict[str, str]) -> None:
        super().__init__()
        self.conditions = conditions

    def create_col_config(self,
                          *args,
                          **kwargs):
        styleConditions = []
        for condition, colour in self.conditions.items():
            styleConditions.append(
                {
                    "condition": condition.replace('<x>', 'params.value'),
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
