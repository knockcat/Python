#fact of a number

num = int(input("Enter a number:"))
temp = num
fact = 1;
while(num!=0):
    fact = fact * num
    num = num-1

print('factoraial of',temp, 'is ', fact)
