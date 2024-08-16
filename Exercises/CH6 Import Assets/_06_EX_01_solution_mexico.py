from manim import *

config.assets_dir = "./"

class MexicoBandera(Scene):
    def construct(self):
        big_rec = Rectangle(width=7,height=4,fill_opacity=1,color=WHITE)
        GREEN_FLAG_COLOR = "#005940"
        RED_FLAG_COLOR   = "#BE1126"

        green_rec = big_rec.copy()
        green_rec.scale([1/3,1,1],about_edge=LEFT).set_color(GREEN_FLAG_COLOR)
        red_rec = big_rec.copy()
        red_rec.scale([1/3,1,1],about_edge=RIGHT).set_color(RED_FLAG_COLOR)

        logo = SVGMobject("mexico_logo").scale(0.9)

        self.play(
            Write(big_rec),
            Write(green_rec),
            Write(red_rec),
        )
        self.play(Write(logo,stroke_color=BLACK,run_time=3))
        self.wait()