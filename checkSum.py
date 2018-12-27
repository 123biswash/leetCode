import sys
for line in sys.stdin:
    a = list(line)
    a.reverse()
    for i in xrange(1,len(a)):
        if i%2 == 0:
            b=str(int(a[i])*2)
            a[i]=str(sum([int(k) for k in list(b)]))
           
    sumI=sum([int(i) for i in a[1:]])
    print(sumI)