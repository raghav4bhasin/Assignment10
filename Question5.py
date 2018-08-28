'''
Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
'''

import random

lst = []

file = open('samplenew.txt', 'w')

for i in range(10):
    x = str(random.randrange(5000))
    file.write(x)
    file.write('\n')

file.close()
file = open('samplenew.txt', 'r')
data = file.read()
datalst = data.split()

for j in datalst:
    lst.append(int(j))
lst.sort()

file1 = open('samplenew1.txt', 'w')

for y in lst:
    file1.write(str(y))
    file1.write('\n')
    
file1.close()
file1 = open('samplenew1.txt', 'r')
print(file1.read())
    
