"""Create a function that generates rectangles pyramid given the base number. Do it with two lists comprehensions like exercise 1."""

from manim import *

class Pyramid(Scene):
    def get_pyramid(self, n):
        return VGroup(*[
            VGroup(*[
                Square(side_length=0.5)
                for _ in range(i)
            ]).arrange(RIGHT, buff=0)
            for i in range(n)
        ]).arrange(DOWN, buff=0)
    
    def construct(self):
        pyramids = VGroup(*[
            self.get_pyramid(n)
            for n in range(1,7)
        ]).arrange(RIGHT, aligned_edge=DOWN)

        self.add(pyramids)