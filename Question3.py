'''
Write a Python program to copy the contents of a file to another file
'''

file1 = open('Sample.txt', 'r')
data = file1.read()

file2 = open('sample1.txt', 'w')
file2.write(data)

file1.close()
file2.close()
