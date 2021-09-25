l = []

x = int(input("Enter Value for x : "))
y = int(input("Enter Value for y : "))

l.append(x)
l.append(y)

t = tuple(l)

print ('x before swaping is :',x,'y before swaping is :',y)

x,y = t[1] ,t[0]

print ('x after swaping is :',x,'y after swaping is :',y)







'''
a=tuple()

a=int(input("enter the value:--->"))
b=tuple()

b=int(input("enter the value:--->"))
print("Value of a and b before swap is ",a,b)

a, b = b,a

print("Value of a and b after swap is ",a,b)
'''
