import matplotlib.pyplot as plt
from functools import cmp_to_key
# import random if ypu want generate point comment out

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
        
def nextToTop(S):
    return S[-2]

def distSq(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clock wise
    else:
        return 2  # counterclockwise

def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if distSq(p0, p2) >= distSq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1

def convexHull(points):
    global p0
    n = len(points)

    ymin = points[0].y
    min_idx = 0
    for i in range(1, n):
        y = points[i].y
        if y < ymin or (ymin == y and points[i].x < points[min_idx].x):
            ymin = points[i].y
            min_idx = i

    points[0], points[min_idx] = points[min_idx], points[0]
    p0 = points[0]

    points[1:] = sorted(points[1:], key=cmp_to_key(compare))
    
    m = 1
    for i in range(1, n):
        while i < n - 1 and orientation(p0, points[i], points[i + 1]) == 0:
            i += 1

        points[m] = points[i]
        m += 1

    if m < 3:
        return []

    hull = [points[0], points[1], points[2]]
    for i in range(3, m):
        while len(hull) > 1 and orientation(nextToTop(hull), hull[-1], points[i]) != 2:
            hull.pop()

        hull.append(points[i])

    return hull


def get_user_input():
    n = int(input('Enter number of points: '))
    points = []
    
    for i in range(n):
        x = float(input('x[' + str(i) + '] = '))
        y = float(input('y[' + str(i) + '] = '))
        points.append(Point(x=x, y=y))

    return points


# Driver Code

input_points = get_user_input()

# or you can use this point
# input_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
# Generate additional random points
# additional_points = [(random.uniform(0, 5), random.uniform(0, 5)) for _ in range(50)]
# all_points = input_points + additional_points

points = [Point(point[0], point[1]) for point in input_points]

# Visualize the points
plt.scatter([p.x for p in points], [p.y for p in points], label='Points', color='blue')


# Find and visualize the convex hull
convex_hull_points = convexHull(points)
if convex_hull_points:
    convex_hull_x = [p.x for p in convex_hull_points]
    convex_hull_y = [p.y for p in convex_hull_points]
    convex_hull_x.append(convex_hull_x[0])
    convex_hull_y.append(convex_hull_y[0])
    plt.plot(convex_hull_x, convex_hull_y, label='Convex Hull', color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
