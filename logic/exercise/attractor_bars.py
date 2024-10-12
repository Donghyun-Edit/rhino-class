import Rhino.Geometry as geo
import Rhino.Display as dis
import scriptcontext as sc


SCALE = 5.0
DISPLAY_KEY = "my_display"


def draw_bars_with_attractors(attractors: list[geo.Point3d]):
    if DISPLAY_KEY in sc.sticky:
        custom_display: dis.CustomDisplay = sc.sticky[DISPLAY_KEY]
        custom_display.Clear()
    else:
        custom_display = dis.CustomDisplay(True)
        sc.sticky[DISPLAY_KEY] = custom_display

    # 최소 1개의 Attractor가 있어야 한다.
    if not attractors:
        raise ValueError

    # Attractor별로 색상을 지정해 준다.
    colors: dict[geo.Point3d, dis.ColorHSL] = {}
    for i, attractor in enumerate(attractors):
        colors[attractor] = dis.ColorHSL(
            1.0,  # Alpha
            i / len(attractors) + 0.1,  # Hue
            1.0,  # Saturation
            0.7,  # Value
        )

    # 그리드 배치점을 나열해 놓는다.
    grid_points: list[geo.Point3d] = []
    for x in range(100):
        for y in range(100):
            grid_points.append(geo.Point3d(x, y, 0))

    # Attractor와의 거리에 따라 높이가 변하는 막대를 그린다.
    for grid_point in grid_points:
        closest_attractor = min(
            attractors,
            key=lambda a, gp=grid_point: a.DistanceTo(gp),
        )
        distance = grid_point.DistanceTo(closest_attractor)
        importance = SCALE / (SCALE + distance**2 / SCALE)  # 0 ~ 1
        color = colors[closest_attractor]
        color = dis.ColorHSL(color)  # 복제  # type: ignore
        color.L = 1 - importance * 0.5
        shift_vector = geo.Vector3d(0.0, 0.0, SCALE * importance)
        extrusion = geo.Line(  # type: ignore
            grid_point - shift_vector,  # type: ignore
            grid_point + shift_vector,  # type: ignore
        )
        custom_display.AddLine(extrusion, color, 2)
