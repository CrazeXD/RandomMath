def midpoint(x1, y1, x2, y2):
    ycoord = y2-y1
    if ycoord<=0:
        ycoord*=-1
    ycoord/=2
    xcoord = x2-x1
    if xcoord<=0:
        xcoord*=-1
    xcoord/=2
    if x2>=x1:
        if y2>y1:
            return [xcoord+x1, ycoord+y1]
        else:
            return [xcoord+x1, ycoord+y2]
    else:
        if y2>y1:
            return [xcoord+x2, ycoord+y1]
        else:
            return [xcoord+x2, ycoord+y2]