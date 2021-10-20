import csv
from secrets import randbelow

def genCoord():
    return randbelow(50) + randbelow(50) + 1


rows = []
pointsnum = randbelow(150) + 10

for i in range(pointsnum):
    point = (genCoord(), genCoord())
    rows.append(point)


with open('input.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
