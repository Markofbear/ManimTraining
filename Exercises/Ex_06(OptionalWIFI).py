"""Exercise 6 (Optional)

1. Draw the Wi-Fi logo that has the shape of arches, and the one that has the shape of bars.

2. Draw a Piano Keyboard"""

from manim import *

class Ex_06(Scene):
    def construct(Wifi):
        fill = {"fill_opacity": 1}

        L1W = Circle(color=WHITE).set(height=7, stroke_width=20)
        L2W = L1W.copy().set(height=6)
        L3W = L1W.copy().set(height=5)
        L4W = L1W.copy().set(height=4)
        L5W = Circle(color=WHITE, **fill).set(height=1)
        L5W.shift(UP * 1)

        rectangle1 = Rectangle(width=4.5, height=3, color=BLACK, **fill)
        rectangle1.rotate(60 * DEGREES)
        rectangle1.shift(UP *2, RIGHT * 3)

        rectangle2 = Rectangle(width=4.5, height=3, color=BLACK, **fill)
        rectangle2.rotate(-60 * DEGREES)
        rectangle2.shift(UP * 2, LEFT * 3)

        rectangle3 = Rectangle(width=10, height=4, color=BLACK, **fill)
        rectangle3.shift(DOWN * 2)

        group = Group(L1W, L2W, L3W, L4W, L5W, rectangle1, rectangle2, rectangle3)

        group.shift(DOWN * 3)

        Wifi.add(group)
        




