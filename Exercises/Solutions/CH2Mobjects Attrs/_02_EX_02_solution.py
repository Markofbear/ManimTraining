from manim import *

class Solution(Scene):
    def construct(self):
        circle = Circle()\
            .to_corner(UL,buff=1)

        mobs = [circle,Square(),Star(),Triangle(),Circle()]

        for i in range(len(mobs)-1):
            mobs[i+1].next_to(mobs[i],RIGHT,aligned_edge=UP)

        self.add(*mobs)