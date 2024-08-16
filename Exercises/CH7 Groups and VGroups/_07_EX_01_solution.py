from manim import *

class Chess(Scene):
    def construct(self):
        from itertools import cycle
        colors = cycle([WHITE,BLACK])
        LENGTH = 8

        board = VGroup(*[
            VGroup(*[
                Square(fill_color=next(colors),fill_opacity=1,stroke_width=1)
                    .set(height=0.5)
                for _ in range(LENGTH)
            ]).arrange(RIGHT if i%2 == 0 else LEFT,buff=0)
            for i in range(LENGTH)
        ]).arrange(DOWN,buff=0)
        board.scale(1.3)

        self.add(board)