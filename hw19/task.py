def dep_point(points):
    n = len(points)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = points[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], points[i])

    max_right[n - 1] = points[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], points[i])

    max_depth = 0
    for i in range(1, n - 1):
        water_level = min(max_left[i], max_right[i])
        depth = water_level - points[i]
        if depth > max_depth:
            max_depth = depth

    return max_depth


heights = [1, 2, 5, 6, 1, 1, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
print(dep_point(heights))
