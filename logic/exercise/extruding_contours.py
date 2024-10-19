import Rhino.Geometry as geo


def extrude_contours(contours: list[geo.Curve]) -> list[geo.Surface]:
    # 모든 등고선 커브는 닫혀 있다는 전제 하에 작동한다.
    if not all(c.IsClosed for c in contours):
        raise ValueError

    # 모든 커브를 반시계 방향으로 만든다.
    # 돌출시킬 때, 커브의 방향으로 법선(Normal)이 결정되기 때문이다.
    contours = contours.copy()  # 원본 리스트를 건드리지 않기 위해 복제
    for contour in contours:
        clockwise = geo.CurveOrientation.Clockwise
        if contour.ClosedCurveOrientation() == clockwise:  # type: ignore
            contour.Reverse()

    # 각 커브가 몇 개의 바깥 커브로 둘러싸여 있는지 확인한다.
    # 더 많은 커브로 둘러싸여 있으면 더 안쪽 커브라는 뜻이고,
    # 더 높이 올라가는 등고선으로 취급된다.
    layer_numbers: dict[geo.Curve, int] = {}
    for contour in contours:
        test_point = contour.PointAtStart  # 커브상 임의의 점이면 충분
        layer_number = 1
        other_contours = [c for c in contours if not c is contour]
        for other_contour in other_contours:
            contains = other_contour.Contains(test_point, geo.Plane.WorldXY, 0.001)
            if contains == geo.PointContainment.Inside:
                layer_number += 1
        layer_numbers[contour] = layer_number  # 바깥 개수 기억

    # 등고선 커브들을 돌출(Extrude)시켜 평면을 만든다.
    breps: list[geo.Surface] = []
    for contour in contours:
        layer_number = layer_numbers[contour]
        print(layer_number)
        extrusion = geo.Extrusion.Create(contour, 0.2 * layer_number, True)
        breps.append(extrusion)

    return breps
