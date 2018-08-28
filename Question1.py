'''
Q.1- Write a Python program to read n lines of a file
'''

n = int(input("Enter number of lines to read."))

with open ('sample.txt', 'r') as file:
    for x in range (n):
        print(file.readline())
