s2 = '679'
for i in range(10):
    s = str(i) + s2
    for i in range(5):
        s3 = s + str(i*2)
        num = int(s3)
        print(num)
        if(num%72==0):
            print('answer is = {}'.format(float(num/72)))