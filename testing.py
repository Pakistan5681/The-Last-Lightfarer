def is_adjacent(coord1, coord2, orthogonal_only=False):
    x1, y1 = coord1
    x2, y2 = coord2
    diffX = abs(x1 - x2)
    diffY = abs(y1 - y2)
    if orthogonal_only:
        return (diffX == 1 and diffY == 0) or (diffX == 0 and diffY == 1)
    else:
        return diffX <= 1 and diffY <= 1 and (diffX + diffY > 0)
is_adjacent((2, 2), (2, 3))  
is_adjacent((2, 2), (3, 3))
is_adjacent((2, 2), (4, 4))  
