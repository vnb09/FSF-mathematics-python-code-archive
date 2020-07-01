from manimlib.imports import *

class Examples1(GraphScene):
    def construct(self):
       
        rectangle = Rectangle(height = 3, width = 4, color = GREEN)
        rectangle_area_func = TexMobject("Area", "=", "f(", "Length", ",", "Breadth", ")").scale(0.6)
        rectangle_area_func[0].set_color(RED_C)
        rectangle_area_func[2].set_color(ORANGE)
        rectangle_area_func[3].set_color(YELLOW_C)
        rectangle_area_func[5].set_color(BLUE_C)
        rectangle_area_func[6].set_color(ORANGE)


        rectangle_area = TexMobject("Area", "=", "Length", "\\times", "Breadth").scale(0.6)
        rectangle_area[0].set_color(RED_C)
        rectangle_area[2].set_color(YELLOW_C)
        rectangle_area[4].set_color(BLUE_C)


        square = Square(side_length = 5, color = PURPLE)
        square_area_func = TexMobject("Area", "=", "f(", "Length", ")")
        square_area_func[0].set_color(GREEN_C)
        square_area_func[2].set_color(ORANGE)
        square_area_func[3].set_color(BLUE_C)
        square_area_func[4].set_color(ORANGE)

        square_area = TexMobject("Area", "=", "Length^2")
        square_area[0].set_color(GREEN_C)
        square_area[2].set_color(BLUE_C)


        circle = Circle(radius = 2, color = PINK)
        circle_area_func = TexMobject("Area", "=", "f(", "r", ")")
        circle_area_func[0].set_color(YELLOW_C)
        circle_area_func[2].set_color(ORANGE)
        circle_area_func[3].set_color(GREEN_C)
        circle_area_func[4].set_color(ORANGE)

        circle_area = TexMobject("Area", "=", "\\pi", "r^2")
        circle_area[0].set_color(YELLOW_C)
        circle_area[2].set_color(BLUE_C)
        circle_area[3].set_color(GREEN_C)

        radius = Line(ORIGIN,2*RIGHT, color = RED_C)
        


        braces_rect1 = Brace(rectangle, LEFT)
        eq_text1 = braces_rect1.get_text("Length").set_color(YELLOW_C)
        braces_rect2 = Brace(rectangle, UP)
        eq_text2 = braces_rect2.get_text("Breadth").set_color(BLUE_C)

        braces_square = Brace(square, LEFT)
        braces_square_text = braces_square.get_text("Length").set_color(BLUE_C)

        radius_text = TexMobject("r", color = GREEN_C).next_to(radius,UP)
        


        self.play(ShowCreation(rectangle))
        self.wait(1)
        self.play(GrowFromCenter(braces_rect1),Write(eq_text1),GrowFromCenter(braces_rect2),Write(eq_text2))
        self.wait(1)
        self.play(Write(rectangle_area_func))
        self.wait(1)
        self.play(Transform(rectangle_area_func, rectangle_area))
        self.wait(1)
        self.play(FadeOut(braces_rect1),FadeOut(eq_text1),FadeOut(braces_rect2),FadeOut(eq_text2),FadeOut(rectangle_area_func))


        self.play(Transform(rectangle, square))
        self.wait(1)
        self.play(GrowFromCenter(braces_square),Write(braces_square_text))
        self.wait(1)
        self.play(Write(square_area_func))
        self.wait(1)
        self.play(Transform(square_area_func, square_area))
        self.wait(1)
        self.play(FadeOut(braces_square),FadeOut(braces_square_text),FadeOut(square_area_func))


        self.play(Transform(rectangle, circle))
        self.wait(1)
        self.play(ShowCreation(radius),Write(radius_text))
        self.wait(1)
        self.play(FadeOut(radius_text),FadeOut(radius))
        self.wait(1)
        self.play(Write(circle_area_func))
        self.wait(1)
        self.play(Transform(circle_area_func, circle_area))
        self.wait(1)
        self.play(FadeOut(circle_area_func))



class Examples2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        rectangle_x_y_0 = Polygon(np.array([-1,-2,0]),np.array([-1,2,0]),np.array([1,2,0]),np.array([1,-2,0]),np.array([-1,-2,0]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)
        rectangle_x_y_3 = Polygon(np.array([-1,-2,3]),np.array([-1,2,3]),np.array([1,2,3]),np.array([1,-2,3]),np.array([-1,-2,3]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)

        rectangle_y_z_1 = Polygon(np.array([1,-2,3]),np.array([1,2,3]),np.array([1,2,0]),np.array([1,-2,0]),np.array([1,-2,3]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)
        rectangle_y_z_minus_1 = Polygon(np.array([-1,-2,3]),np.array([-1,2,3]),np.array([-1,2,0]),np.array([-1,-2,0]),np.array([-1,-2,3]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)

        rectangle_x_z_2 = Polygon(np.array([1,2,3]),np.array([-1,2,3]),np.array([-1,2,0]),np.array([1,2,0]),np.array([1,2,3]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)
        rectangle_x_z_minus_2 = Polygon(np.array([1,-2,3]),np.array([-1,-2,3]),np.array([-1,-2,0]),np.array([1,-2,0]),np.array([1,-2,3]), color = RED_E, fill_color = RED_C, fill_opacity = 0.1)

        box = VGroup(rectangle_x_y_0, rectangle_x_y_3, rectangle_y_z_1, rectangle_y_z_minus_1, rectangle_x_z_2, rectangle_x_z_minus_2)

        braces_rectangle_x_y_0 = Line(np.array([1,2,0]), np.array([1,-2,0]), color = BLUE_C)
        braces_rectangle_x_y_0_text = TextMobject("Length").set_color(BLUE_C).move_to(np.array([2,-1,0]))

        braces_rectangle_y_z_1 = Line(np.array([1,2,0]), np.array([1,2,3]), color = YELLOW_C)
        braces_rectangle_y_z_1_text = TextMobject("Height").set_color(YELLOW_C).move_to(np.array([2,3.8,2]))

        braces_rectangle_x_z_2 = Line(np.array([1,2,3]), np.array([-1,2,3]), color = PURPLE)
        braces_rectangle_x_z_2_text = TextMobject("Breadth").set_color(PURPLE).move_to(np.array([0,3.8,3.3]))

        box_area_func = TexMobject("Area =", "f(", "Length", ",", "Breadth", ",", "Height", ")").move_to(4*LEFT+3.5*UP).scale(0.6)
        box_area_func[0].set_color(GREEN_C)
        box_area_func[1].set_color(ORANGE)
        box_area_func[2].set_color(BLUE_C)
        box_area_func[4].set_color(PURPLE)
        box_area_func[6].set_color(YELLOW_C)
        box_area_func[7].set_color(ORANGE)

        box_area_func_2 = TexMobject("Area =", "Length", "\\times", "Breadth", "\\times", "Height").move_to(4*LEFT+3.5*UP).scale(0.6)
        box_area_func_2[0].set_color(GREEN_C)
        box_area_func_2[1].set_color(BLUE_C)
        box_area_func_2[3].set_color(PURPLE)
        box_area_func_2[5].set_color(YELLOW_C)


        self.set_camera_orientation(phi=70 * DEGREES, theta = 45*DEGREES)

        self.add(axes)
        
        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(ShowCreation(box), ShowCreation(braces_rectangle_x_y_0))
        self.add_fixed_orientation_mobjects(braces_rectangle_x_y_0_text)
        self.play(ShowCreation(braces_rectangle_y_z_1))
        self.add_fixed_orientation_mobjects(braces_rectangle_y_z_1_text)
        self.play(ShowCreation(braces_rectangle_x_z_2))
        self.add_fixed_orientation_mobjects(braces_rectangle_x_z_2_text)
        self.wait(2)

        self.move_camera(phi=60* DEGREES,theta=80*DEGREES)
        self.add_fixed_in_frame_mobjects(box_area_func)
        self.play(Write(box_area_func))
        self.wait()

        
        self.play(ReplacementTransform(box_area_func,box_area_func_2))
        self.add_fixed_in_frame_mobjects(box_area_func_2)
        
        
        self.wait(3)        