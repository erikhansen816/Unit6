#Erik Hansen
#12/11/17
#warmup16.py

firstletter = input('What is the first letter of your name: ')
lastletter = input('What is the first letter of your last name: ')

dictionary = open('engmix.txt')

for i in dictionary:
    if i != '':
        if i.strip()[0] == firstletter and i.strip()[-1] == lastletter:
            print(i.strip())
    
