import csv
import matplotlib.pyplot as plt
import numpy as np
from random import getrandbits
from secrets import randbelow


with open('input.csv') as file:
    reader = csv.reader(file)

    for point in reader:
        plt.plot(point[0], point[1], 'ro', color='hotpink')


# draw result
with open('output.csv') as file:
    reader = csv.reader(file)

    for res in reader:
        func = lambda x : float(res[0])*x + float(res[1])

        x = np.arange(0, 10, 0.01)
        y = list(map(func, x))

        plt.plot(x, y, color='green')


# draw random line
randsign = lambda : 1 if bool(getrandbits(1)) else -1
randa, randb = randbelow(10) * randsign(), randbelow(10) * randsign()
randline = lambda x : randa*x + randb

x = np.arange(0, 10, 0.01)
y = list(map(randline, x))

plt.plot(x, y, color='turquoise')


plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.show()
