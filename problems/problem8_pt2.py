def quick_sort(l, func):
    if len(l) <= 1:
        return l
    pivot = func(l[0])
    less = []
    more = []
    for i in range(1, len(l)):
        if func(l[i]) < pivot:
            less.append(l[i])
        else:
            more.append(l[i])
    return quick_sort(less, func) + [l[0]] + quick_sort(more, func)


def squared_d(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2


def main(): 
    points = []
    with open("inputs/input8.txt", "r") as i_f:
        for line in i_f:
            line = line.strip().split(",")
            points.append([int(n) for n in line])
    dist_points = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist_points.append([squared_d(points[i], points[j]), i, j])
    sorted_dist_points = quick_sort(dist_points, lambda x: x[0])
    point2group = {i: set([i]) for i in range(len(points))}
    i = 0
    connections = 0
    skipped = 0
    while True:
        p1 = sorted_dist_points[i][1]
        p2 = sorted_dist_points[i][2]
        group_p1 = point2group[p1]
        group_p2 = point2group[p2]
        i += 1
        if group_p1 is group_p2:
            skipped += 1
            continue
        connections += 1
        group_p1.update(group_p2)
        for p in group_p2:
            point2group[p] = group_p1
        if len(group_p1) == len(points):
            total = points[p1][0] * points[p2][0]
            break
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
