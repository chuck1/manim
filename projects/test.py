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



