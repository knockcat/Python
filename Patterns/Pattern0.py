s = "hello"
l = len(s)

for i in range(l):
    for j  in range(l-i):
        print(s[j], end = '')
    print('\n')
    
