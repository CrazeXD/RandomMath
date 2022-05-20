def dilate(x1, y1, x2, y2, x3, y3, c1, c2, dilationfactor):
    x1-=c1
    x2-=c1
    x3-=c1
    y1-=c2
    y2-=c2
    y3-=c2
    x1*=dilationfactor
    x2*=dilationfactor
    x3*=dilationfactor
    y1*=dilationfactor
    y2*=dilationfactor
    y3*=dilationfactor
    x1+=c1
    x2+=c1
    x3+=c1
    y1+=c2
    y2+=c2
    y3+=c2    
    return x1, y1, x2, y2, x3, y3