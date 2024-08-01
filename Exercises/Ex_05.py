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
    def construct(yinyan):
        fill = {"fill_opacity": 1}
        

        w_circle = Circle(color=WHITE).set(height=6)
        w_circle.rotate(PI / 2)  
        
        semi_circle = VMobject(**fill).set_points(
            w_circle.points[:int(len(w_circle.points) / 2)]
        )

        u_circle = Circle(COLOR=WHITE, **fill)
        
        sw_circle = Circle(color=BLACK, **fill).set(height=1.5)
        sw_circle.shift(1.5 * UP)
        sb_circle = Circle(color=WHITE, **fill).set(height=1.5)
        sb_circle.shift(1.5 * DOWN)



        yinyan.add(w_circle, semi_circle, sb_circle,sw_circle)


