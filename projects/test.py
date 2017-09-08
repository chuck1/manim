#!/usr/bin/env python2.7

import sys
sys.path.append("/home/crymal/git/c/esolv_python")

import mobject
import mobject.tex_mobject
import animation.transform
import animation.simple_animations
import scene

import libesolv_python as es

print es.Transform.constructor 
print es.Write.anim_write_constructor
print es.Mobject.mobject_constructor
print es.TexMobject.texmobject_constructor

s = es.Storage()

def mobject_constructor(l):
    print "mobject_constructor"
    print l
    return mobject.Mobject(*l)

es.Transform.constructor = animation.transform.Transform
es.Write.anim_write_constructor = animation.simple_animations.Write

es.Mobject.mobject_constructor = mobject_constructor
es.TexMobject.texmobject_constructor = mobject.tex_mobject.TexMobject

print "Mobject ctor   ", es.Mobject.mobject_constructor
print "TexMobject ctor", es.TexMobject.texmobject_constructor

class Test(scene.Scene):
    def construct(self):
        a = s.symbol('a')
        x = s.symbol('x')
        y = s.symbol('y')
    
        print(x)
        print(y)
    
        f = x * y
        g = f * a
    
        print(f)
        print(g)
        
        self.play(*g.get_animations())
        
        
   




