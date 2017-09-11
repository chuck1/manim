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

def mobject_constructor(l):
    #print "mobject_constructor"
    #print l
    return mobject.Mobject(*l)

def transform_copy_constructor(s, d):
    return animation.transform.Transform(s.copy(), d)

es.Transform.constructor = animation.transform.Transform
es.TransformCopy.constructor = transform_copy_constructor
es.Write.anim_write_constructor = animation.simple_animations.Write
es.Mobject.mobject_constructor = mobject_constructor
es.TexMobject.texmobject_constructor = mobject.tex_mobject.TexMobject

class Test(scene.Scene):
    def construct(self):
        a = s.symbol('a')
        b = s.symbol('b')
        x = s.symbol('x')
        y = s.symbol('y')
    
        f = x * y
        g = f * (a + b)
    
        print(f)
        print(g)

        #self.play(animation.simple_animations.Write(f.get_mobject()))
        
        #self.play(animation.simple_animations.Write(g.get_mobject()))
        
        #self.play(animation.simple_animations.Write(Mobject(*g.get_mobject().submobjects[3:5])))

        for anims in g.get_animations():
            self.play(*anims)
        
        changed, h = g.expand()

        if changed:
            for anims in h.get_animations():
                self.play(*anims)

       
        
   




