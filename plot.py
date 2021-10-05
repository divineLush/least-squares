import csv
import matplotlib.pyplot as plt

with open('input.csv') as file:
    reader = csv.reader(file)

    for point in reader:
        plt.plot(point[0], point[1], 'ro', color='hotpink')


plt.grid(True)
plt.show()
