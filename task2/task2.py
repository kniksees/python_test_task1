import sys

def ans(center_x: int, center_y: int, r: int, point_x: int, point_y: int) -> int:
    if (center_x - point_x) * (center_x - point_x) + (center_y - point_y) *  (center_y - point_y) == r * r:
        return 0
    elif (center_x - point_x) * (center_x - point_x) + (center_y - point_y) *  (center_y - point_y) < r * r:
        return 1
    else :
        return 2


if __name__ == "__main__":
    circle_file = open(sys.argv[1])
    circle_param = []
    for line in circle_file:
        circle_param.append([int(x) for x in line.split()])
    
    dots_file = open(sys.argv[2])
    for line in dots_file:
        dot = [int(x) for x in line.split()]
        print(ans(circle_param[0][0], circle_param[0][1], circle_param[1][0], dot[0], dot[1]))


