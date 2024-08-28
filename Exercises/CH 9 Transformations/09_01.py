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

axes = Axes( 
    x_range=[-8, 9, 2], 
    y_range=[-6, 7, 2], 
    x_length=4, 
    y_length=4, 
    axis_config={'include_numbers': True, 'numbers_to_exclude': [0]}, 
    x_axis_config={'color': ORANGE}, 
    y_axis_config={'color': ORANGE}, 
) 
axes_label = axes.get_axis_labels(x_label='x', y_label='f(x)') 
graph = axes.plot(lambda x: 5*np.e ** (-x**2/2), x_range=[-5, 5], color=YELLOW) 
graph_label = axes.get_graph_label(graph, label='e^{-x^2}', color=YELLOW, x_val=1,dot=False) 
self.add(axes, graph, graph_label, axes_label) 
