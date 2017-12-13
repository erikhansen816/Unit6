#Erik Hansen
#12/13/17
#quiz6.py

"""Program 1
dictionary = open('engmix.txt')

for word in dictionary:
    if word != '':
        if word.count('c') == 3 and word.count('p') == 2:
            print(word.strip())
"""        

"""Program 2
dictionary = open('engmix.txt')
total = 0
for word in dictionary:
    if word != '':
        if word.strip()[0] == 'r':
            total += 1
print(total)
"""

"""Program 3
dictionary = open('engmix.txt')
number = int(input('Enter a number between 1 and 21: '))
for word in dictionary:
    if word != '':
        if len(word) == number+1:
            print(word)
            break
"""

"""Program 4
dictionary = open('engmix.txt')
letter = input('Enter a letter: ')
total = 0
for word in dictionary:
    if word != '':
        if letter not in word:
            total += 1
print(total)"""

"""Program 5
dictionary = open('engmix.txt')
L = []
for word in dictionary:
    if word != '':
        L.append(word.strip())
leng = len(L)
print(L[leng//2])"""