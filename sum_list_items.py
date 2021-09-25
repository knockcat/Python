#Program to initialize item in list and then display the sum of items

l = [76,34,12,54]

sum = 0

for i in l:
    print(i,end = ' ')
    sum  = sum + i

print('\nSum of above list items is : ',sum)
