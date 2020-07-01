import datetime
import random

date = datetime.datetime(2019,7,30,20,45,21)
f = open("Dates.txt", "w")

pattern = list()
'''
for i in range(50):
    rand = random.randint(-2, 14)
    if rand<9:
        pattern.append(1)
    elif rand<12:
        pattern.append(0)
    elif rand < 14:
        pattern.append(2)
    else:
        pattern.append(3)


print(pattern)
'''

pattern = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 2, 0, 2, 0, 3, 0, 1, 1, 0, 1, 3, 0, 1, 0, 2, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 2, 0, 1, 1, 0, 1, 3, 1, 1, 2, 1, 0, 1, 1]

for i in range(50):
    date += datetime.timedelta(days=1)

    for k in range(pattern[i]):
        if i % 2 == 0:
            date += datetime.timedelta(minutes=(i % 15) * 4, hours=1, seconds=i * 14)
        else:
            date -= datetime.timedelta(minutes=(i % 20) * 3, hours=1, seconds=i * 23)
        print(date.strftime("%a %b %d %X %Y +0530"))
        f.write(date.strftime("%a %b %d %X %Y +0530"))
        f.write('\n')

f.close()
