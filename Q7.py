
b, i, j, flag, k = 0, 0, 0, 0, 0
lst1 = [(2,'Prime')]
b = int(input("Enter upper bound of the interval : "))
print("Required Dictionary is : ")
for i in range(3, b + 1):
	flag = 1
	for j in range(2, i // 2 + 1):
		if (i % j == 0):
			flag = 0
	if (flag == 1):
		lst2 = [(i,'Prime')]
	else:
		lst2 = [(i,'Not-Prime')]
	lst1.append(lst2)
print(lst1)

