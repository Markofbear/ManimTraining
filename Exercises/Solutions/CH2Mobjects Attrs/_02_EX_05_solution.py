from manim import *

class E5(Scene):
    def construct(self):
        fig_kwargs = {"fill_opacity": 1, "stroke_width": 0, "color": WHITE}
        big_circle = Circle(color=WHITE).set(height=6)

        semi_circle = VMobject(**fig_kwargs).set_points(
            big_circle.points[:int(len(big_circle.points)/2)]
        )

        semi_circle.rotate(-PI/2,about_point=ORIGIN)

        up_black_circle = Circle(**fig_kwargs).set_color(BLACK)
        up_black_circle.set(height=3)
        up_black_circle.move_to(UP*3/2)

        down_white_circle = up_black_circle.copy()
        down_white_circle.set_color(WHITE)
        down_white_circle.move_to(-UP*3/2)

        small_black_circle = down_white_circle.copy()
        small_black_circle.set_color(BLACK).scale(0.3)

        small_white_circle = up_black_circle.copy()
        small_white_circle.set_color(WHITE).scale(0.3)

        self.add(
            semi_circle,
            up_black_circle,down_white_circle,
            small_black_circle,small_white_circle,
            big_circle
        )