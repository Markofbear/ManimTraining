#Move a circle to the upper left corner, and position several objects in a row to the right, aligned with the top edge of the circle, as shown in the following picture, try doing it with a loop.

from manim import *


class Ex_02(Scene):
    def construct(self):
        circle = Circle()\
            .to_corner(UL,buff=1)

        mobs = [circle,Square(),Star(),Triangle(),Circle()]

        for i in range(len(mobs)-1):
            mobs[i+1].next_to(mobs[i],RIGHT,aligned_edge=UP)

        self.add(*mobs)