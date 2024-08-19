from manim import *


class BubbleSort(Scene):
    def get_cell(self, n):
        text = Text(f"{n}")
        sq = Square(side_length=0.8)
        vg = VGroup(sq, text)
        return vg

    def get_arr_mob(self, arr):
        return VGroup(*[
            self.get_cell(n)
            for n in arr
        ]).arrange(RIGHT,buff=0)

    def get_end_label(self, n, arr_mob):
        triangle = Triangle(fill_opacity=1).rotate(PI)
        val = Text(f"{n}")
        triangle.match_width(val).next_to(val,DOWN,buff=0.1)
        end = Text("(end)").match_height(triangle)\
            .next_to(val,UP,buff=0.1)
        vg = VGroup(triangle,end,val)
        vg.next_to(arr_mob[n],UP,buff=0.1)
        return vg

    def get_i_label(self, n, arr_mob):
        triangle = Triangle(fill_opacity=1)
        val = Tex("i=",f"{n}")
        triangle.match_width(val).scale(0.5).next_to(val,UP,buff=0.1)
        vg = VGroup(triangle,val)
        vg.next_to(arr_mob[n],DOWN,buff=0.1)
        return vg

    def get_j_label(self, n, arr_mob):
        triangle = Triangle(fill_opacity=1)
        val = Tex("j=",f"{n}")
        triangle.match_width(val).scale(0.5).next_to(val,UP,buff=0.1)
        vg = VGroup(triangle,val)
        vg.next_to(arr_mob[n],DOWN,buff=1.1)
        return vg

    def get_comparator(self, start, arr_mob):
        grp_selected = VGroup(arr_mob[start],arr_mob[start+1])
        comparator = Rectangle(
            width=grp_selected.width,
            height=grp_selected.height,
            stroke_color=RED
        )
        comparator.move_to(grp_selected)
        return comparator


    def construct(self):
        arr = [5, 9, 3, 1, 8, 6, 4, 2, 7]
        arr_mob = self.get_arr_mob(arr)
        arr_len = len(arr)

        indexes = VGroup(*[
            Text(f"{i}")
                .scale(0.5)
                .next_to(cell,UP,buff=0.1)
            for i,cell in enumerate(arr_mob)
        ])
        end = arr_len - 0 - 1
        end_label = self.get_end_label(end,indexes)
        i_label = self.get_i_label(0,arr_mob)
        j_label = self.get_j_label(0,arr_mob)
        comparator = self.get_comparator(0, arr_mob)

        self.add(arr_mob,indexes,end_label,i_label,j_label,comparator)
        self.add_foreground_mobject(comparator)

        for _i in range(arr_len):
            end = arr_len - _i - 1 ###
            self.play(
                Transform(end_label,self.get_end_label(end,indexes)),
                Transform(i_label,self.get_i_label(_i,arr_mob))
            )
            for _j in range(end):
                self.play(
                    Transform(j_label,self.get_j_label(_j,arr_mob)),
                    Transform(comparator,self.get_comparator(_j, arr_mob))
                )
                self.add_foreground_mobject(comparator)
                if arr[_j] > arr[_j + 1]:
                    self.play(
                        comparator.animate.set_fill(opacity=0.5,color=RED),
                        rate_func=there_and_back,run_time=2
                    )
                    self.play(
                        arr_mob[_j].animate.move_to(arr_mob[_j+1]),
                        arr_mob[_j+1].animate.move_to(arr_mob[_j]),
                        run_time=2.5
                    )
                    self.remove(arr_mob)
                    del arr_mob
                    arr[_j], arr[_j + 1] = arr[_j + 1], arr[_j]
                    arr_mob = self.get_arr_mob(arr)
                    self.add(arr_mob)
                else:
                    self.play(
                        comparator.animate.set_fill(opacity=0.5,color=GREEN),
                        rate_func=there_and_back,run_time=2
                    )
                self.wait(0.3)