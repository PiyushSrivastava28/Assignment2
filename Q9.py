import sys
n =int(sys.argv[1])
f1 ,f2 = 0, 1
print(n)
if (n < 1):
    exit()
for x in range(0, n):
    print(f2, end = " ")
    f1 ,f2 = f2 ,f1 + f2
