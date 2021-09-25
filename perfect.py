#perfect number
i = 1
s = 0
num = int(input("Enter a number-> "))

while(i<num):
    if(num % i == 0):
        s = s + i
    i += 1

if(num == s):
    print(num,'is a perfect number')
else:
    print(num,'is not a perfect number')
