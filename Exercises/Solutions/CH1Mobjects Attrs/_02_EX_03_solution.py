from manim import *

class E3(Scene):
    def construct(self):
        fig_kwargs = {"color": RED, "fill_opacity": 0.8, "stroke_width": 0}
        left_circle = Circle(**fig_kwargs).set(height=4)
        right_circle = left_circle.copy()
        square = Square(**fig_kwargs).set(height=4)

        left_circle.shift(LEFT*2)
        right_circle.shift(UP*2)

        pivot_kwargs = {"angle":-PI/4, "about_point": square.get_center()}

        square.rotate(**pivot_kwargs)
        left_circle.rotate(**pivot_kwargs)
        right_circle.rotate(**pivot_kwargs)

        self.add(square,left_circle,right_circle)