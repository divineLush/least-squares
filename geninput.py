import csv
from secrets import randbelow


pointsnum = randbelow(150) + 10
rows = [(randbelow(100), randbelow(100)) for i in range(pointsnum)]

with open('input.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
