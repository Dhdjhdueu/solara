"""
# HBox
Lays out children in horizontal direction.
"""
from solara.kitchensink import react, sol

from .common import ColorCard


@react.component
def Page():
    with sol.VBox() as main:
        colors = "green red orange brown yellow pink".split()
        with sol.HBox():
            for color in colors:
                ColorCard(color, color)
    return main
