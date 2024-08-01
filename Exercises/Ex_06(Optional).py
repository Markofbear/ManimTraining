"""Exercise 6 (Optional)

1. Draw the Wi-Fi logo that has the shape of arches, and the one that has the shape of bars.

2. Draw a Piano Keyboard"""

from manim import *

class Ex_06(Scene):
    def construct(self):
        fill = {"fill_opacity": 1}

        L1W = Circle(color=WHITE).set(height=7)
        L1W = VMobject(**fill).set_points(
            L1W.points[:int(len(L1W.points) / 2)]
        )
        L1W.set_stroke(BLACK, width=1)

        L1B = Circle(color=BLACK,**fill).set(height=6)

        L2W = L1W.copy().set(height= 2)

        self.add(L1W,L1B,L2W)


