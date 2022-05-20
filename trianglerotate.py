def trianglerotation(x1, y1, x2, y2, x3, y3, counter = True, center1 = 0, center2 = 0):
    if counter:
        return [[-y1+center2, x1+center1], [-y2+center2, x2+center1], [-y3+center2, x3+center1]]
    else:
        return [[y1+center2, x1+center1], [y2+center2, x2+center1], [y3+center2, x3+center1]]