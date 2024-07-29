from manim import *

class Ex_04(Scene):

    def construct(logo):
        fill = {"fill_opacity": 1}
        circle = Circle(color=WHITE, **fill).scale(4)




        logo.add(circle)