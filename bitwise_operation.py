# Program to take 2 values from user and peform all the bitwise operations

a =int(input('Enter -: '))

b = int(input('Enter -: '))

bit_and = a & b

bit_or = a | b

bit_xor = a ^ b

left_s = a<<b

right_s = a>>b

print('Bitwise And of ',a, '&' ,b, 'is :', bit_and)
print('Bitwise Or of ',a, '|' ,b, 'is :' ,bit_or)
print('Bitwise Xor of ',a, '^' ,b, 'is :', bit_xor)
print('Left Shift of ',a, '<<' ,b, ' bytes is :', left_s)
print('Right Shiftt  of ',a, '>>' ,b, 'bytes is :' ,right_s)

