from manim import *

class Ex_04(Scene):

    def construct(logo):
        fill = {"fill_opacity": 1}
        circle = Circle(color=WHITE, **fill).scale(4)

        b_triangle = Triangle(color = GREEN).scale(2.5)
        b_triangle.rotate(PI, about_point=ORIGIN)

        m_triangle = b_triangle.copy()
        m_triangle.scale(2/3, about_edge=UP).set_color(BLACK)

        s_triangle = b_triangle.copy()



        logo.add(circle, b_triangle,m_triangle, s_triangle)