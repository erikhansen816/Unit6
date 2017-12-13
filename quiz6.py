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

Program 3
dictionary = open('engmix.txt')
number = input('Enter a number between 1 and 22: ')
total = 0
while total <= 1
    for word in dictionary:
        if word != '':
            if len(word) == number:
                total += 1
                print(word)
            