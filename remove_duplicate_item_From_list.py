#accept value from user in the list and print the list after removing all the duplicate items

n  = int(input("Number of values you want to enter :"))
l = []
l1=[]

for i in range(0,n):
    m = int(input('Enter element :'))
    l.append(m)

for i in l:
    if i not in l1:
        l1.append(i)
      
print('list before deleting duplicated items if exists : ',l)          

print('list after deleting duplicated items if exists : ',l1)

    
'''
#accept value from user in the list and print the list after removing all the duplicate items

n  = int(input("Number of values you want to enter :"))
l = []

for i in range(0,n):
    m = int(input('Enter element :'))
    l.append(m)

print('Given list is : ' , l)

for i in range(0,n):
    for j in range(i+1,n):
        if(l[i] == l[j]):
            l.pop(j)

print('list after deleting duplicated items if exists : ',l)
'''
