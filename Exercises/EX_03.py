from manim import *

class Ex_03(Scene):

    def construct(heart):    
        red = {"color": RED}
        l_circle = Circle(**red)
        r_circle = Circle(**red)
        square = Square(**red)

        heart.add(l_circle, r_circle, square)
