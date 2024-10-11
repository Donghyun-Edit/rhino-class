# -*- coding:utf-8 -*-
# Compatibility code for Python 2 in Rhino 7
from __future__ import division, absolute_import
import polyfill  # pylint:disable=C0411,W0611

import Rhino.Geometry as geo


def say_hi(name):
    # type: (str) -> None
    print("HI {}".format(name))


def draw_pentagon():
    # type: () -> geo.PolylineCurve
    points = [
        geo.Point3d(2.5, 0.0, 0.0),
        geo.Point3d(3.0, 4.0, 0.0),
        geo.Point3d(0.0, 6.0, 0.0),
        geo.Point3d(-3.0, 4.0, 0.0),
        geo.Point3d(-2.5, 0.0, 0.0),
    ]
    closing_point = points[0]
    return geo.PolylineCurve(points + [closing_point])
