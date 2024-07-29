from manim import *

class E4(Scene):
    def construct(self):
        fig_kwargs = {"fill_opacity": 1}
        circle = Circle(color=WHITE,**fig_kwargs).scale(3)

        big_triangle = Triangle(color="#2FA673",**fig_kwargs).scale(2.4)
        big_triangle.rotate(PI,about_point=ORIGIN)

        mid_triangle = big_triangle.copy()
        mid_triangle.scale(2/3,about_edge=UP).set_color("#2A3C4E")

        small_triangle = big_triangle.copy()
        small_triangle.scale(1/3,about_edge=UP).set_color(WHITE)



        self.add(circle,big_triangle,mid_triangle,small_triangle)