from manim import *


class Ex_02(Scene):
    def construct(self):
        circle = Circle()\
            .to_corner(UL,buff=1)

        mobs = [circle,Square(),Star(),Triangle(),Circle()]

        self.add(*mobs)