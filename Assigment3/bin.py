
import math
def second(n):
    num = str(bin(n))
    count = 0
    num = num[2:]
    print num
    for i in range(len(num)):
        if num[-i] == '0':
            count += 1
        if count == 2:
            print i
            print len(num)-1
            return math.pow(2, i-1)

print second(37)
