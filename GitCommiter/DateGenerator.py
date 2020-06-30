import datetime

date = datetime.datetime(2019,7,1,21,45,21)
f = open("Dates.txt", "w")

for i in range(50):
    date += datetime.timedelta(days=1)
    if i % 2 == 0:
        date += datetime.timedelta(minutes=(i % 15)*4, hours=1, seconds=i*14)
    else:
        date -= datetime.timedelta(minutes=(i % 20)*3, hours=1, seconds=i*23)
    print(date.strftime("%a %b %d %X %Y +0530"))
    f.write(date.strftime("%a %b %d %X %Y +0530"))
    f.write('\n')

f.close()