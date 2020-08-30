n=int(input("Enter the length of list and then Enter the list "))
for i in range(n):
    lst1=int(input())
l=int(input("Enter the value to search : "))
for i in lst1 :
    if l ==  i :
      print("It exists ")
      exit()
print("It doesnot Exists")
