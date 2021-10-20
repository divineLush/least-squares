import csv
from secrets import randbelow


rows = []
pointsnum = randbelow(150) + 10

for i in range(pointsnum):
    point = (randbelow(100), randbelow(100))
    rows.append(point)


with open('input.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
