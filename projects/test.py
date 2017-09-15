#!/usr/bin/env python2.7

import sys
sys.path.append("/home/crymal/git/c/esolv_python")

from constants import *
from mobject import Mobject
import mobject.tex_mobject
import animation.transform
import animation.simple_animations
import scene

import libesolv_python as es

es.Transform.constructor 
es.Write.anim_write_constructor
es.Mobject.mobject_constructor
es.TexMobject.texmobject_constructor

s = es.Storage()

def mobject_constructor(*args):
    #print "mobject_constructor"
    #print l
    return mobject.Mobject(*args)

def transform_constructor(s, d):
    return animation.transform.ReplacementTransform(s, d)

def transform_copy_constructor(s, d):
    return animation.transform.Transform(s.copy(), d)

es.Transform.constructor = transform_constructor
es.TransformCopy.constructor = transform_copy_constructor
es.Write.anim_write_constructor = animation.simple_animations.Write
es.Uncreate.anim_uncreate_constructor = animation.simple_animations.Uncreate

es.Mobject.mobject_constructor = mobject_constructor
es.TexMobject.texmobject_constructor = mobject.tex_mobject.TexMobject

es.Factory().init()

class Test(scene.Scene):
    
    def construct(self):
        a = s.symbol('a')
        b = s.symbol('b')
        x = s.symbol('x')
        y = s.symbol('y')
    
        f = x * y

        # This line produces lists of animations to transform f into g.
        g = f * (a + b)
        
        # The animations can be accessed by the get_animations function of g.
        [self.play(*anims) for anims in g.get_animations()]
        
        # The expand function attempts to manipulate the equation.
        # The first value returned tells us whether the equation changed and 
        # the second is the new equation.
        # As before, animations are producted to transform the old equation to the new
        # equation.
        changed, h = g.expand()

        if changed:
            [self.play(*anims) for anims in h.get_animations()]

        self.dither()

        print(f)
        print(g)
        print(h)
        
class Test2(scene.Scene):
    def construct(self):
        x = s.symbol('x')
    
        f = x.intpower(2,1)
        
        self.play(animation.simple_animations.Write(f.get_mobject()))
        
        print('derivative')
        d = f.derivative(x)
        print(d)

        for anims in d.get_animations():
            print(anims)
            self.play(*anims)

class GeoAlg(scene.Scene):
    def construct(self):
        
        e1 = s.symbol("\\mathbf{e}_1")
        e2 = s.symbol("\\mathbf{e}_2")
        e3 = s.symbol("\\mathbf{e}_3")
        r0 = s.symbol("r_0")
        r12 = s.symbol("r_{1,2}")
        r13 = s.symbol("r_{1,3}")
        r23 = s.symbol("r_{2,3}")
        v1 = s.symbol("v_1")
        v2 = s.symbol("v_2")
        v3 = s.symbol("v_3")
        
        rotor2 = r12 * e1 * e2 + r13 * e1 * e3 + r23 * e2 * e3
        
        rotor   = r0 + rotor2
        rotor_c = r0 - rotor2
        
        vec     = v1 * e1 + v2 * e2 + v3 * e3

        mo_vec     = vec.get_mobject()
        mo_rotor   = rotor.get_mobject()
        mo_rotor_c = rotor_c.get_mobject()

        mo_rotor.shift(DOWN)
        mo_rotor_c.shift(2*DOWN)
        
        f = rotor_c * vec * rotor
        
        mo_f = f.get_mobject()

        mo_f.scale(0.5)

        print(rotor_c)

        a = rotor_c

        def repeat(a, f):
            b = f(a)
            while b:
                print(b)
                a = b
                b = f(a)
            return a

        a = repeat(a, es.Operand.iso_bring_up_add)

        a = repeat(a, es.Operand.simplify_once_top)
       
        #print(a.str_debug())

        return

        self.play(
                animation.simple_animations.Write(mo_f),
                #animation.simple_animations.Write(mo_vec),
                #animation.simple_animations.Write(mo_rotor),
                #animation.simple_animations.Write(mo_rotor_c),
                )
        
        
        
        







