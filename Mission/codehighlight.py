from manim import *

class VSCodeTextHighlight(Scene):
    def construct(self):
        code_string = """
def hello_world():
    print('Hello, World!')
    print('Hello, Mr Milton!')
    print('Hello, Gandalf!')
    print('Hello, Mathematich Kokchung!')
"""

        code = Code(
            code=code_string,
            tab_width=4,
            language="Python",
            background="window",
            font="Monospace", 
            insert_line_no=True  
        ).scale(1.5)
        
        self.play(Write(code), run_time=3)  
        self.wait(1)

        highlight = SurroundingRectangle(
            code.code[1][1:6],  
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.4,
            buff=0.01, 
            stroke_width=0  
        )

        highlight1 = SurroundingRectangle(
            code.code[2][1:999],  
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.4,
            buff=0.01, 
            stroke_width=0  
        )

        highlight2 = SurroundingRectangle(
            code.code[3][6:50],  
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.4,
            buff=0.01, 
            stroke_width=0  
        )
        
        self.play(AnimationGroup(Create(highlight), Create(highlight1), Create(highlight2), lag_ratio=0), run_time=2)  
        self.wait(2)

        self.play(AnimationGroup(FadeOut(highlight), FadeOut(highlight1), FadeOut(highlight1), lag_ratio=0.5), run_time=2)  
        self.wait(1)
