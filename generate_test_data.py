# generate random test data

import random

fileout = open("generate_test_data.txt", "w+")

nodeNum = random.randint(1, 20)
intNum = random.randint(1, 500)
writeNum = random.randint(1, 10)

i = writeNum
while i > 0:
    fileout.write(random.choice(["PATH_ADD", "PATH_REMOVE"]))
    j = nodeNum
    while j > 0:
        fileout.write(" %d" % random.randint(-125, 125))
        j -= 1
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["IS_NODE_CONNECTED", "CONTAINS_EDGE", "SHORTEST_PATH_LENGTH", "LEAST_TICKET_PRICE", "LEAST_TRANSFER_COUNT", "LEAST_UNPLEASANT_VALUE"]))
    j = 2
    while j > 0:
        fileout.write(" %d" % random.randint(-125, 125))
        j -= 1
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["CONTAINS_NODE", "DISTINCT_NODE_COUNT", "CONNECTED_BLOCK_COUNT"]))
    fileout.write(" %d" % random.randint(-125, 125))
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["PATH_REMOVE_BY_ID"]))
    fileout.write(" %d" % random.randint(1, 200))
    fileout.write("\n")
    i -= 1

i = writeNum
while i > 0:
    fileout.write(random.choice(["PATH_ADD", "PATH_REMOVE"]))
    j = nodeNum
    while j > 0:
        fileout.write(" %d" % random.randint(-125, 125))
        j -= 1
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["IS_NODE_CONNECTED", "CONTAINS_EDGE", "SHORTEST_PATH_LENGTH", "LEAST_TICKET_PRICE", "LEAST_TRANSFER_COUNT", "LEAST_UNPLEASANT_VALUE"]))
    j = 2
    while j > 0:
        fileout.write(" %d" % random.randint(-125, 125))
        j -= 1
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["CONTAINS_NODE", "DISTINCT_NODE_COUNT", "CONNECTED_BLOCK_COUNT"]))
    fileout.write(" %d" % random.randint(-125, 125))
    fileout.write("\n")
    i -= 1

i = intNum/5
while i > 0:
    fileout.write(random.choice(["PATH_REMOVE_BY_ID"]))
    fileout.write(" %d" % random.randint(1, 200))
    fileout.write("\n")
    i -= 1

print("Succeed!\n")
print("Please enter \"enter\" key to close!\n")
input()
