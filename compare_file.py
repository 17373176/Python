# compare file1.txt file2.txt

file_list = []

print("Input your file number, then enter \"enter\" key: ")
fileNum = int(input())
for i in range(1, fileNum + 1):
    file_list.append(open("outFile" + str(i) + ".txt").readlines())

fileout = open("compareFile.txt", "w+")

flag = 0
for i in range(0, fileNum - 1):
    for j in range(i + 1, fileNum):
        row = 0
        for line_i, line_j in zip(file_list[i], file_list[j]):
            row += 1
            if not line_i == line_j:
                col = 0
                for char_i, char_j in zip(line_i, line_j):
                    col += 1
                    if not char_i == char_j:
                        flag = 1
                        fileout.write("The difference of file %d and file %d in row: %d , col: %d\n" % (i + 1, j + 1, row, col))

if flag == 0:
    fileout.write("equals!\n")

print("Succeed!\n")
print("Please enter \"enter\" key to close!\n")
input()
