#print all the even length words of a string.

str = input("Enter an string :")
for i in range(0,len(str),2):
    print(str[i],end = '')

