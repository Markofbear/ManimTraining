from manim import *

class CodeHighlight(Scene):
    def construct(self):
        title = Text("Code Highlight", font_size=64)
        title.to_edge(UP) 
        line = Line(start=LEFT * 3, end=RIGHT * 3)  
        line.next_to(title, DOWN, buff=0.1) 

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
            insert_line_no=False  
        ).scale(1)

        # self.play(Write(title), run_time=1)  
        # self.wait(0.5)

        # self.play(Create(line), run_time=1)  
        # self.wait(1)

        # self.play(Write(code), run_time=3)  
        # self.wait(1)

        highlight = SurroundingRectangle(
            code.code[1:][1:],  
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.4,
            buff=0.01, 
            stroke_width=0
        ).stretch_to_fit_width(code.width).align_to(code,LEFT).align_to(code.code[2:],UP)

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
        
        # self.play(AnimationGroup(Create(highlight), Create(highlight1), Create(highlight2), lag_ratio=0), run_time=2)  
        # self.wait(2)

        # self.remove(highlight2)

        # self.play(AnimationGroup(FadeOut(highlight), FadeOut(highlight1), lag_ratio=0.5), run_time=2)  
        # self.wait(1)

        title_highlight = SurroundingRectangle(
            title,
            color=RED,
            fill_color=RED,
            fill_opacity=0.4,
            buff=0.01,
            stroke_width=0
        )

        self.add(code, highlight)
        # self.play(Create(title_highlight), run_time=1)
        # self.wait(1)

        # self.play(FadeOut(title_highlight), FadeOut(title), FadeOut(line), run_time=1)
