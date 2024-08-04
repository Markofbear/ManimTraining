from manim import *

class MyScene(Scene):
    def construct(self):
        config.frame_width = 3
        config.pixel_height = 600
        config.pixel_width = 800
        
        self.play(Write(NumberPlane()), run_time=4)
        self.wait()