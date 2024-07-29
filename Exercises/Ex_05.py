"""Draw the Yin-Yang symbol as shown in the following picture.

Hint: Use this to draw a semi circle

------------

big_circle = Circle().scale(3)

semi_circle = VMobject(**fig_kwargs).set_points(

  big_circle.points[:int(len(big_circle.points)/2)]

)

-----------
"""

from manim import *

class ex_05(Scene):
    def construct(yinyang):
    
    