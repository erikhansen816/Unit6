#Erik Hansen
#12/8/17
#homework.py


"""
#1
figures out if word is in the dictionary
dictionary = open('engmix.txt')
tf = False
word = input('Enter a word: ')
for words in dictionary:
    if word == words.strip():
        tf = True
if tf == True:
    print(word, 'is in the dictionary')
else:
    print(word,'is not in the dictionary')"""
   
   


 
"""
#2
Prints out the number term in a dictionary
dictionary = open('engmix.txt')
L =[]
for words in dictionary:
    L.append(words.split())

num = int(input('Enter a number: '))
print(L[num-1])"""






"""
#3
prints out a file with exclamation point
dictionary = open('engmix.txt')
fileName = input('Enter a file name: ')
file = open(fileName)
fileLines = []
for line in file:
    fileLines.append(line.strip())
fileLines.reverse()
for item in fileLines:
    print(item+'!')"""
  
  
  
  
    
"""
#4
prints out word with greatest number of given letter
dictionary = open('engmix.txt')
letter = input('Enter a letter: ')
gl = ''
gn = 0
for word in dictionary:
    if letter in word:
        if word.count(letter)>gn:
            gl = word
            gn = word.count(letter)
print(gl)
"""
