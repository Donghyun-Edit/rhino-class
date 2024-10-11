import Rhino.Geometry as geo


def say_hi(name: str):
    print(f"HI {name}")


def draw_pentagon() -> geo.PolylineCurve:
    points = [
        geo.Point3d(2.5, 0.0, 0.0),
        geo.Point3d(3.0, 4.0, 0.0),
        geo.Point3d(0.0, 6.0, 0.0),
        geo.Point3d(-3.0, 4.0, 0.0),
        geo.Point3d(-2.5, 0.0, 0.0),
    ]
    closing_point = points[0]
    return geo.PolylineCurve(points + [closing_point])
