from manim import *

class EX(Scene):
    def construct(self):
        # We will learn this in deep in
        # Chapter 7
        texts = VGroup(*[
            Text(f"{i}")
            for i in range(-6,7)
        ]).arrange(RIGHT,buff=1)
        texts.set(width=config.frame_width-1)
        # Learn to use `enumerate` func
        for t in texts:
            # Use print("...") to help you
            self.play(GrowFromCenter(t))
            self.wait()
        self.wait()