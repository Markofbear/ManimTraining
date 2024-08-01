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
        w_fill = {"fill_opacity": 1}

        w_circle = Circle(color=WHITE).set(height=5)
        w_circle.rotate(PI / 2)  
        
        semi_circle = VMobject(**w_fill).set_points(
            w_circle.points[:int(len(w_circle.points) / 2)]
        )

        b_circle = Circle(color=WHITE, **w_fill).set(height=1)
        b_circle.shift(1 * DOWN + 1 * RIGHT)

        yinyang.add(w_circle, semi_circle, b_circle)


