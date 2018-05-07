nm = list(map(int,input().split()))
if (nm[0]*nm[1])%2 > 0:
    total = int((nm[0]*nm[1]/2) - 0.5)
else:
    total = int(nm[0]*nm[1]/2)
print(total)
