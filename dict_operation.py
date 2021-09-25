print('Vishal Joshi')
d = {}

size = int(input("Enter Size of dictionary :"))
while(size>0):
    key = input('Enter key :')
    value = input('Enter Value :')
    d[key] = value
    size = size - 1

s_k = input('enter key to be searched :')
m = d.get(s_k,'Key Not Exist')
print(m)

rem = input('Enter key for the Element to be deleted :')
print('Before Deletion Element in Dictionary is',d)
del d[rem]  #d.pop(rem)  both function return key error if key  is not found

print('After Deletion Element in Dictionary , if valid key is given for deletion',d)
