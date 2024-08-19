"""Draw a fractal dragon (don't use list comprehension here)."""

from manim import * 

class Dragon(Scene):
    def construct(self):
        path = VGroup()
        line = Line(ORIGIN, UP * 5, stroke_width=1.2)
        path.add(line)
        iteration = 13

        for i in range(iteration):
            path2 = path.copy()
            path2.rotate(90*DEGREES, about_point=path[-1].get_end() if i == 0 else path[-1].get_start())
            pathreversed = reversed([*path2])
            path.add(*pathreversed)

            path.set(height=config.frame_height-1)
            path.move_to(ORIGIN)

            self.add(path)
