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

es.Transform.constructor = animation.transform.Transform
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
        g = f * (a * b)
    
        print(f)
        print(g)

        #self.play(animation.simple_animations.Write(f.get_mobject()))
        
        #self.play(animation.simple_animations.Write(g.get_mobject()))
        
        #self.play(animation.simple_animations.Write(Mobject(*g.get_mobject().submobjects[3:5])))

        for anims in g.get_animations():
            self.play(*anims)

        return

        print(g.get_animations())
        
        o_f = f.get_mobject()

        for anims in g.get_animations():
            print anims
            for anim in anims:
                print anim
                print anim.mobject
                print anim.mobject.get_critical_point(ORIGIN)
                for subo in anim.mobject.submobjects:
                    if isinstance(subo, mobject.tex_mobject.TexMobject):
                        print repr(subo.tex_string)
                        if subo.tex_string == 'b':
                            self.play(animation.simple_animations.Write(subo))
                            self.play(animation.Animation(subo))
                            pass

            self.play(*anims)
        
        
   




