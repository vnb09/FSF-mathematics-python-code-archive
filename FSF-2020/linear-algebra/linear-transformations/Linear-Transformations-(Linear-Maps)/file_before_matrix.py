from manimlib.imports import *

class linear(GraphScene):

    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN+RIGHT,
    "x_labeled_nums": list(range(-5, 6)),
    "y_labeled_nums": list(range(-5, 6)),
    "x_axis_width": 7,
    "y_axis_height": 7,
    }

    def construct(self):
        
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)
        heading = TextMobject(r"$T(x,y) = T(x+2y,x-y)$")
        heading.move_to(UP*3+LEFT*4)
        self.play(Write(heading))
        self.wait()

        before = TextMobject("Before Linear Transformation")
        before.set_color(DARK_BLUE)
        before.move_to(3*UP+4*RIGHT)
        before.scale(0.75)
        dot1 = Dot().shift(self.graph_origin+1*XTD*RIGHT+1*YTD*UP)
        dot2 = Dot().shift(self.graph_origin+2*XTD*RIGHT+1*YTD*UP)
        dot1.set_color(DARK_BLUE)
        dot2.set_color(DARK_BLUE)
        p1 = TextMobject(r"$P_1$")
        p1.set_color(DARK_BLUE)
        p1.move_to(self.graph_origin+1*XTD*RIGHT+2*YTD*UP)
        p2 = TextMobject(r"$P_2$")
        p2.set_color(DARK_BLUE)
        p2.move_to(self.graph_origin+2*XTD*RIGHT+2*YTD*UP)

        after = TextMobject("After applying Linear Transformation")
        after.set_color(RED)
        after.move_to(3*UP+4.5*RIGHT)
        after.scale(0.75)
        dot3 = Dot().shift(self.graph_origin+3*XTD*RIGHT+0*YTD*UP)
        dot4 = Dot().shift(self.graph_origin+4*XTD*RIGHT+1*YTD*UP)
        dot3.set_color(RED)
        dot4.set_color(RED)
        p3 = TextMobject(r"$P_3$")
        p3.set_color(RED)
        p3.move_to(self.graph_origin+3*XTD*RIGHT-1.1*YTD*UP)
        p4 = TextMobject(r"$P_4$")
        p4.set_color(RED)
        p4.move_to(self.graph_origin+4*XTD*RIGHT+2*YTD*UP)

        tp1 = TextMobject(r"$T(P_1) = P_3$")
        tp1.set_color(RED)
        tp1.move_to(DOWN+4*LEFT)
        tp2 = TextMobject(r"$T(P_2) = P_4$")
        tp2.set_color(RED)
        tp2.move_to(2*DOWN+4*LEFT)

        self.play(Write(before), ShowCreation(dot1), ShowCreation(dot2),Write(p1), Write(p2))
        self.wait(3)
        self.play(Transform(before,after), Transform(dot1,dot3), Transform(dot2,dot4), Transform(p2,p4), Transform(p1,p3), Write(tp1), Write(tp2))
        self.wait(3)


class withgrid(LinearTransformationScene):
    def construct(self):

        heading = TextMobject(r"$T(x,y) = (x+2y,x-y)$")
        heading.move_to(UP*2.5+LEFT*4)
        self.play(Write(heading))
        self.wait()

        before = TextMobject("Before Linear Transformation")
        before.set_color(DARK_BLUE)
        before.move_to(3.5*UP+4*RIGHT)
        before.scale(0.75)
        dot1 = Dot().shift(1*RIGHT+1*UP)
        dot2 = Dot().shift(2*RIGHT+1*UP)
        dot1.set_color(DARK_BLUE)
        dot2.set_color(DARK_BLUE)
        
        dot1_c = Dot(radius = 0.05).shift(1*RIGHT+1*UP)
        dot2_c = Dot(radius = 0.05).shift(2*RIGHT+1*UP)
        dot1_c.set_color(RED)
        dot2_c.set_color(RED)
        self.add_transformable_mobject(dot1_c)
        self.add_transformable_mobject(dot2_c)
        
        p1 = TextMobject(r"$P_1$")
        p1.set_color(DARK_BLUE)
        p1.move_to(1*RIGHT+1.5*UP)
        p2 = TextMobject(r"$P_2$")
        p2.set_color(DARK_BLUE)
        p2.move_to(2*RIGHT+1.5*UP)

        after = TextMobject("After applying Linear Transformation")
        after.set_color(RED)
        after.move_to(3.5*UP+3.5*RIGHT)
        after.scale(0.75)
        dot3 = Dot().shift(3*RIGHT+0*UP)
        dot4 = Dot().shift(4*RIGHT+1*UP)
        dot3.set_color(RED)
        dot4.set_color(RED)
        p3 = TextMobject(r"$P_3$")
        p3.set_color(RED)
        p3.move_to(3*RIGHT-0.6*UP)
        p4 = TextMobject(r"$P_4$")
        p4.set_color(RED)
        p4.move_to(4*RIGHT+1.5*UP)

        self.play(Write(before), ShowCreation(dot1), ShowCreation(dot2),Write(p1), Write(p2))
        self.wait(3)
        matrix = [[1,2],[1,-1]]
        self.apply_matrix(matrix)
        self.play(Transform(before,after), Transform(p2,p4), Transform(p1,p3))
        self.play(Transform(before,after))
        self.wait(3)

        ending = TextMobject(r"$T(\left[\begin{array}{c}x \\ y\end{array}\right]) = \left[\begin{array}{c} x+2y \\ x-y\end{array}\right]$")
        ending.move_to(UP*2+LEFT*4)
        self.play(Transform(heading,ending))
        self.wait()

from manimlib.imports import *
class ThreeDExplanation(ThreeDScene):
    
    def construct(self):

        text = TextMobject(r"$T(x,y) = (x+y,x-y,x+2y)$")
        text.scale(0.75)
        text.move_to(UP*2.5+LEFT*4)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text))
        self.wait()

        before = TextMobject("Before Linear Transformation")
        self.add_fixed_in_frame_mobjects(before)
        before.set_color(GREEN_E)
        before.move_to(3.5*UP+4*RIGHT)
        before.scale(0.75)
        dot1 = Dot().shift(1*RIGHT+1*UP)
        dot2 = Dot().shift(2*RIGHT+1*UP)
        dot3 = Dot().shift(1*RIGHT+1*UP)
        dot1.set_color(GREEN_E)
        dot2.set_color(GREEN_E)
        dot3.set_color(GREEN_E)
        self.play(ShowCreation(before))

        dot1_c = Dot(radius = 0.05).shift(1*RIGHT+1*UP)
        dot2_c = Dot(radius = 0.05).shift(0*RIGHT+2*UP)
        dot3_c = Dot(radius = 0.05).shift(1*RIGHT-1*UP)
        dot1_c.set_color(RED)
        dot2_c.set_color(RED)
        dot3_c.set_color(RED)
        
        axes = ThreeDAxes(x_min = -7,x_max=7,y_min=-4,y_max=4,z_min=-4,z_max=4)
        self.play(ShowCreation(axes))
        self.move_camera(distance = 100, phi=30*DEGREES,theta=45*DEGREES,run_time=3)
        
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1)
        self.stop_ambient_camera_rotation()

        plane = NumberPlane()
        self.play(ShowCreation(dot1),ShowCreation(dot3),ShowCreation(dot2),ShowCreation(plane))
        
        self.play(FadeOut(before))
        after = TextMobject("After applying Linear Transformation")
        self.add_fixed_in_frame_mobjects(after)
        after.set_color(RED)
        after.move_to(3.5*UP+3.5*RIGHT)
        after.scale(0.75)
      
        matrix = [[1,1],[1,-1],[2,1]]
        self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),ApplyMethod(plane.apply_matrix,matrix),ApplyMethod(dot1_c.apply_matrix,matrix),ApplyMethod(dot3_c.apply_matrix,matrix),ApplyMethod(dot2_c.apply_matrix,matrix))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        ending = TextMobject(r"$T(\left[\begin{array}{c}x \\ y\end{array}\right]) = \left[\begin{array}{c} x+y \\ x-y \\ x+2y \end{array}\right]$")
        ending.scale(0.75)
        ending.move_to(-UP*2+LEFT*4)
        self.play(Transform(text,ending))
        self.add_fixed_in_frame_mobjects(ending)
        self.wait(9)