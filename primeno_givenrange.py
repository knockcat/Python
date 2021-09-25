#prime number upto a given range
num = 1
ran = int(input("Enter Range :"))
print("prime and compsite number in given range are")
for i in range(1,ran+1):
    if(i>1):
       for j in range(2,i):
           if(i%j == 0):
               break
       else:
             print(i)


'''
start = 11
end = 25
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
    
'''
