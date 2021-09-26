import matplotlib.pyplot as plt
import numpy as np

points = [(1, 5.3), (2, 6.3), (3, 4.8), (4, 3.8), (5, 3.3)]

sumx = 0
sumy = 0
sumxdouble = 0
sumxy = 0
n = len(points)

for point in points:
    sumx += point[0]
    sumy += point[1]
    sumxdouble += point[0]**2
    sumxy += point[0]*point[1]

det = sumxdouble * n - sumx**2

print(sumx, sumy, sumxdouble, sumxy, det)

if (det != 0):
    deta = sumxy * n - sumx * sumy
    a = deta / det

    detb = sumxdouble * sumy - sumxy * sumx
    b = detb / det

    def func(arg):
        return a*arg + b

    x = np.arange(0, n, 0.01)
    y = list(map(func, x))

    plt.plot(x, y)

    for point in points:
        plt.plot(point[0], point[1], 'ro')

    plt.grid(True)
    plt.show()
else:
    print('no solutions')
