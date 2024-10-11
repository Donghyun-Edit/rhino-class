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
