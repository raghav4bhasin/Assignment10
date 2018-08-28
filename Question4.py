'''
Q.4- Combine each line from first file with the corresponding line in second file

'''


with open('sample.txt') as file1, open('sample1.txt') as file2 ,open('new.txt','w') as file3:
    for i, j in zip(file1, file2):
        file3.write(i+j)
