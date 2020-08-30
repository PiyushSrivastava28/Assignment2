
s = input("Enter the String : ")
l,u = 0,0
for i in s: 
    if (i>='a'and i<='z'): 
        l=l+1                  #counting lower case 
    if (i>='A'and i<='Z'): 
        u=u+1                  #counting upper case 
print('Lower case characters: ',l) 
print('Upper case characters: ',u) 

