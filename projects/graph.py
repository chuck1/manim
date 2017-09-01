#!/usr/bin/env python

import numpy as np

from helpers import *

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject
from mobject.vectorized_mobject import *

from animation.animation import Animation
from animation.transform import *
from animation.simple_animations import *
from animation.playground import *
from topics.geometry import *
from topics.characters import *
from topics.functions import *
from topics.number_line import *
from topics.combinatorics import *
from scene import Scene
from camera import Camera
from mobject.svg_mobject import *
from mobject.tex_mobject import *

from mobject.vectorized_mobject import *

## To watch one of these scenes, run the following:
## python extract_scenes.py -p file_name <SceneName>

points = [
            np.array([-1, 0, 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            ]
end_points = [
            np.array([-1, -1, 0]),
            np.array([0, 1, 0]),
            np.array([1, -1, 0]),
            ]

def create_circles():

    for p, ep in zip(points, end_points):
        c = Circle(radius = 0.25)
        c.shift(p)
        l = Line(p, ep)
        yield c, l


class Vertex(object):
    def __init__(self, p):
        self.p = p
        self.circle = Circle(radius = 0.25)
        self.circle.shift(p)

class Edge(object):
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.line = self.generate_line()

    def generate_line(self):
        return Line(self.u.p, self.v.p)

class Graph(VMobject):

    def __init__(self, vertices, edges, **kwargs):
        digest_config(self, kwargs)
        self.vertices = [Vertex(p) for p in vertices]
        self.edges = [Edge(self.vertices[i], self.vertices[j]) for i, j in edges]
        VMobject.__init__(self, **kwargs)
        
    def generate_points(self):
        for v in self.vertices:
            self.add(v.circle)

        for e in self.edges:
            self.add(e.line)

    def anim_move_vertex(self, i, p):
        v = self.vertices[i]
        l = Line(v.p, p)
        v.p = p
        
        for e in self.edges:
            if (e.u == v) or (e.v == v):
                old_line = e.line
                e.line = e.generate_line()
                yield Transform(old_line, e.line)
        
        yield MoveAlongPath(v.circle, l)

class Basic(Scene):
    def construct(self):
    
        g = Graph(end_points, [(0,1),(1,2),(2,0)])
            
        self.play(Animation(g))

        self.play(*list(g.anim_move_vertex(0, [0,0,0])))

        return

        circles, lines = zip(*list(create_circles()))

        #self.play(ShowCreation(circle))
        for c in circles:
            self.play(Animation(c, run_time = 0))

        self.play(*[MoveAlongPath(c, l) for c, l in zip(circles, lines)])

        self.dither()




