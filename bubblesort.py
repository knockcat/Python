n=int(input("enter total no of elements:"))
l=[]
for i in range(0,n):
    m=int(input("enter:"))
    l.append(m)
print("the given list is: ",l)
for i in range(0,n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("the sorted list is: ",l)
