#program to take a input as string and print all the words starting from s

str = input("Enter an string :")
splitted_string = str.split()
print(splitted_string)

for i in splitted_string:
    if(i[0] == 's' or i[0] == 'S'):
        print(i,end = '\t')
