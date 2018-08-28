'''
Q.2- Count the frequency of words in a file
'''

with open('sample.txt','r') as file:
    wd = input("Enter the Character to find: ")
    data = file.read()
    
    num = data.count(wd)
    
    print("Count: ",num)
