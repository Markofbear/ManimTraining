from manim import *


class Dragon(Scene):
    def construct(self):
        path = VGroup()
        first_line = Line(ORIGIN,UP / 5,stroke_width=1.2)
        path.add(first_line)
        iterations = 13

        for i in range(iterations):
            new_path = path.copy()
            new_path.rotate(
                        90*DEGREES,
                        about_point=path[-1].get_end() if i == 0 else path[-1].get_start()
                    )
            post_path = reversed([*new_path])
            path.add(*post_path)

        path.set(height=config.frame_height-1)
        path.move_to(ORIGIN)
        
        self.add(path)