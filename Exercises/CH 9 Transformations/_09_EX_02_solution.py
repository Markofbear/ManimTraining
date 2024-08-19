from manim import *

class T2(Scene):
    def construct(self):
        up_tex = MathTex(
            # 0         1       2   3    4
            "\\neg","\\forall","x",":","P(x)",
        ).scale(2)
        down_tex = MathTex(
            #    0      1   2      3     4
            "\\exists","x",":","\\neg","P(x)"
        ).scale(2)
        VGroup(up_tex,down_tex).arrange(DOWN)
        self.play(
            Write(up_tex)
        )
        self.wait()
        steps = [
            # Step 1
            [[2,3,4],
             [1,2,4]],
            # Step 2
            [[0],
             [3]],
            # Step 3
            [[1],
             [0]],
        ]
        for step in steps:
            base, target = step
            self.play(*[
                ReplacementTransform(up_tex[i].copy(),down_tex[j],run_time=3)
                for i,j in zip(base,target)
            ])
            self.wait()