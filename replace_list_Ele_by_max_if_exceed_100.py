# Program to store integers in a list , if the integer is exceeding 100 then string 'MAX' should be stored

size = int(input('Enter size : '))
l = []

for i in range(0,size):
    num = int(input('Enter Integer :'))
    if num> 100:
          l.append('MAX')
    else:
         l.append(num)
         
print('List is : ',l)
   


