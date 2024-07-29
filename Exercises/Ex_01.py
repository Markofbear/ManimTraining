# Write code in Manim to replicate the following picture. 

from manim import *

class Ex_01(Scene):
    def setup(self):
        self.add(NumberPlane())
    
    def construct(self):
        x_range = range(-6,6)
        y_range = range(-3,4)

        dots = [
            Dot([x,y,0])
            for x in x_range
            for y in y_range
        ]

        self.add(*dots)