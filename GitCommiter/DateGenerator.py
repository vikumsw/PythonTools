import datetime


def genDates(year, month, day):
    date = datetime.datetime(year, month, day, 20, 45, 21)
    f = open("Dates.txt", "w")

    pattern = list()

    pattern = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1,
               0, 2, 0, 1, 1, 0, 1, 0, 1, 0, 2, 0, 0, 1, 1]

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


def read_dates(dateList):
    f = open("Dates.txt", "r")
    for x in f:
        dateList.append(x.rstrip())
    f.close()