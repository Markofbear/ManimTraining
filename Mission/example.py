from manim import *

class CodeExample(Scene):
    def construct(self):
        code_string= """
            class Person:
                def __init__(self):
                    _name= self.name
                    _age= self.age
            """
        code= Code(
            code= code_string,
            tab_width= 3,
            language="Python",
            insert_line_no=True,
            background="window",
            font="Monospace"
            ).scale(2)
        
        highlight= Square (color= YELLOW, fill_opacity= .3, stroke_width= 0).scale(.35).stretch_to_fit_width(width= code.code.width-1)
        
        all= VGroup(code, highlight)
        
        
        self.add(all)
        
        
        #all[1].move_to(all[0].code[2]).shift(DOWN*.125)
        
        
        self.move_highlight(all, 3)
        
    def move_highlight(self, all, position):
        if position == 0:
            all[1].move_to(all[0].get_center()).shift(UP*.75)
        else:
            all[1].move_to(all[0].code[position].get_center()).shift(DOWN*.2)