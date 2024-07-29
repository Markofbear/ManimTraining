from manim import *

class Ex_03(Scene):

    def construct(heart):    
        red = {"color": RED, "fill_opacity": 1, "fill_color": RED}

        l_circle = Circle(**red).set(height=2)
        r_circle = Circle(**red).set(height=2)
        square = Square(**red).set(height=1)
        rotate = {"angle":-PI/4}


        l_circle.shift(LEFT*1)
        r_circle.shift(RIGHT*1)
        square.shift(DOWN*1)
        square.rotate(**rotate)
        heart.add(l_circle, r_circle, square)
