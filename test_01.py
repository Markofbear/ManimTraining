 
from manim import *
       
        
class test(Scene):
    def construct(self):
        c= Circle(2, color= WHITE, fill_opacity= 0.5)
        self.play(DrawBorderThenFill(c), run_time= 3.5)
        title= Text("Hello World", font_size= 55, slant= "ITALIC", color= BLACK)
        self.play(Write(title))
        a= Arc(2, TAU * 1/4, -TAU * 2.5/4, color= LOGO_BLUE, stroke_width= 20)
        self.play(Create(a))
        
        
        self.wait(5)