#program to return touple of count of vowels and consonant in the entered string
str = input("Enter String :-")

def numvowel(str):
    cnt = 0
    vowel= []
    consonant = []
    vow = 0
    cons = 0
    for i in str:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'o' or i == 'O' or i == 'u' or i == 'U' or i == 'i' or i=='I' :
            vow+=1
            vowel.append(i)
        else:
            if (i>='A' and i<='z'   and (i != 'a' or i  !=  'A' or i  !=  'e' or i  !=  'E' or i !=  'o' or i  !=  'O' or i  !=  'u' or i  != 'U' or i  !=  'i' or i != 'I')) :
                cons+=1
                consonant.append(i)

    vt = tuple(vowel)
    ct = tuple(consonant)
    print('Touple of Vowels ',vt)
    print('Touple of Consonants ',ct)
    t = (vow,cons) #Number of vowels and consonant
    return t

t = numvowel(str)
print(t)
  



'''

str = input("Enter String :-")

def numvowel(str):
    cnt = 0
    vowel= []
    consonant = []
    for i in str:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'o' or i == 'O' or i == 'u' or i == 'U' or i == 'i' or i=='I' :
            vowel.append(i)
        else:
            if (i>='A' and i<='z'   and (i != 'a' or i  !=  'A' or i  !=  'e' or i  !=  'E' or i !=  'o' or i  !=  'O' or i  !=  'u' or i  != 'U' or i  !=  'i' or i != 'I')) :
                consonant.append(i)

    vt = tuple(vowel)
    ct = tuple(consonant)
    print('Touple of Vowels ',vt)
    print('Touple of Consonants ',ct)

numvowel(str)

'''
