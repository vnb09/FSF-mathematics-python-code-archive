from manimlib.imports import *
class RN_Line(LinearTransformationScene):
    def construct(self):

        self.setup()
        self.wait()
        
        predim = TextMobject("Dimension of this vector space is 2")
        predim.move_to(DOWN+4*LEFT)
        predim.scale(0.75)
        predim.add_background_rectangle()
        self.play(Write(predim))
        self.wait()
        self.play(FadeOut(predim))

        afterlt = TextMobject("After Linear transformation")
        afterlt.move_to(DOWN+4*LEFT)
        afterlt.scale(0.75)
        afterlt.add_background_rectangle()
        
        afterlt2 = TextMobject("Dimension of the vector space","changes to 1")
        afterlt2[0].move_to(1.5*DOWN+4*LEFT)
        afterlt2[1].move_to(2*DOWN+4*LEFT)
        afterlt2.scale(0.75)
        afterlt2.add_background_rectangle()
        matrix = [[1,1],[1,1]]
        self.apply_matrix(matrix)
        self.play(Write(afterlt))
        self.play(Write(afterlt2))
        self.wait()
        nullity = TextMobject("Hence, nullity = 1")
        nullity.move_to(DOWN+4*LEFT)
        self.play(FadeOut(afterlt),FadeOut(afterlt2),Write(nullity))
        self.wait(1)
        self.play(FadeOut(nullity))

class RN_Point(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.wait()
        predim = TextMobject("Another One")
        predim.move_to(DOWN+4*LEFT)
        predim.scale(0.75)
        predim.add_background_rectangle()
        self.play(Write(predim))
        self.wait()
        self.play(FadeOut(predim))
        afterlt = TextMobject("After Linear transformation")
        afterlt.move_to(DOWN+4*LEFT)
        afterlt.scale(0.75)
        afterlt.add_background_rectangle()
        afterlt2 = TextMobject("Dimension of the vector space","changes to 0")
        afterlt2[0].move_to(1.5*DOWN+4*LEFT)
        afterlt2[1].move_to(2*DOWN+4*LEFT)
        afterlt2.scale(0.75)
        afterlt2.add_background_rectangle()
        matrix = [[0,0],[0,0]]
        self.apply_matrix(matrix)
        self.play(Write(afterlt))
        self.play(Write(afterlt2))
        self.wait()
        nullity = TextMobject("Hence, nullity = 2")
        nullity.move_to(DOWN+4*LEFT)
        self.play(FadeOut(afterlt),FadeOut(afterlt2),Write(nullity))
        self.wait(1)
        self.play(FadeOut(nullity))

class RN_SameDim(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.wait()
        predim = TextMobject("Let us look at another example")
        predim.add_background_rectangle()
        predim.move_to(DOWN+4*LEFT)
        predim.scale(0.75)
        self.play(Write(predim))
        self.wait()
        self.play(FadeOut(predim))
        afterlt = TextMobject("After Linear transformation")
        afterlt.move_to(DOWN+4*LEFT)
        afterlt.scale(0.75)
        afterlt.add_background_rectangle()
        afterlt2 = TextMobject("Dimension of the vector space","remains to be 2")
        afterlt2[0].move_to(1.5*DOWN+4*LEFT)
        afterlt2[1].move_to(2*DOWN+4*LEFT)
        afterlt2.scale(0.75)
        afterlt2.add_background_rectangle()
        matrix = [[1,1],[0,1]]
        self.apply_matrix(matrix)
        self.play(Write(afterlt))
        self.play(Write(afterlt2))
        self.wait()
        nullity = TextMobject("Hence, nullity = 0")
        nullity.move_to(DOWN+4*LEFT)
        self.play(FadeOut(afterlt),FadeOut(afterlt2),Write(nullity))
        self.wait(1)
        self.play(FadeOut(nullity))