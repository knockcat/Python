row = int(input('Number of rows : '))

k = 1

for i in range(0,row+1):
    for j in range(1,i+1):
        print(k,end=' ')
        k = k+1
    print('\n')
