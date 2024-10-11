# -*- coding:utf-8 -*-
# 라이노 7에서의 구형 파이썬 2를 지원하기 위한 호환 코드
from __future__ import division, absolute_import
import polyfill  # pylint:disable=C0411,W0611

import Rhino.Geometry as geo


def say_hi():
    print("HI")


def draw_pentagon():
    points = [
        geo.Point3d(2.5, 0.0, 0.0),
        geo.Point3d(3.0, 4.0, 0.0),
        geo.Point3d(0.0, 6.0, 0.0),
        geo.Point3d(-3.0, 4.0, 0.0),
        geo.Point3d(-2.5, 0.0, 0.0),
    ]
    closing_point = points[0]
    return geo.PolylineCurve(points + [closing_point])
