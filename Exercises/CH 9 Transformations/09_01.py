from manim import *

class T1(Scene):

    def construct(self):

        tex = MathTex(

            "\\frac{d}{dx}",  # 0

            "(",              # 1

            "u",              # 2

            "+",              # 3

            "v",              # 4

            ")=",             # 5

            "\\frac{d}{dx}",  # 6

            "u",              # 7

            "+",              # 8

            "\\frac{d}{dx}",  # 9

            "v"               # 10

        ).scale(2)

        self.play(

            Write(tex[:6])

        )

        self.wait()
        steps = [
            # Step 1
            [[2,3,4],
             [7,8,10]],
            # Step 2
            [[0,0],
             [6,9]],
        ]


        for step in steps:
            base, target = step
            self.play(*[
                ReplacementTransform(tex[i].copy(), tex[j],run_time=5)
                for i, j in zip (base,target)


            ])
