from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(GrowFromCenter(circle))
        self.wait()