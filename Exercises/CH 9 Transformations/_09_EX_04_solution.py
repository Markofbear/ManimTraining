from manim import *

class EX(Scene):
    def get_part_spiral(self, sq, corner_vector):
        return Line(
                sq.get_corner(corner_vector),
                sq.get_corner(rotate_vector(corner_vector,-PI)),
                path_arc=-90*DEGREES,
                color=RED
        )

    def construct(self):
        phi = (1+np.sqrt(5))/2
        phi_inv = 1 / phi
        edge = RIGHT
        sq = Square(stroke_width=2).scale(2.3).shift(LEFT)
        corner_vector = DL
        spiral = self.get_part_spiral(sq, corner_vector)

        sq_grp = VGroup(sq)

        self.add(sq)

        for _ in range(9):
            last_sq = sq_grp[-1]
            new_sq = last_sq.copy()
            aligned_edge = rotate_vector(edge,PI/2)

            new_sq.scale(phi_inv)
            new_sq.next_to(last_sq,edge,buff=0,aligned_edge=aligned_edge)
            edge = rotate_vector(edge,-PI/2)
            corner_vector = rotate_vector(corner_vector,-90*DEGREES)
            spiral.append_vectorized_mobject(self.get_part_spiral(new_sq, corner_vector))
            sq_grp.add(new_sq)
            self.play(
                TransformFromCopy(last_sq,new_sq),
                run_time=2
            )
            self.wait(0.5)

        # self.add(spiral)
        self.play(Create(spiral),run_time=6)
        self.wait()



