# read input file - choose: 
 
# puzzle 1-1
input = open("1-1-input.txt", "r") 
# sums for puzzle 1-2
# input = open("1-2-sums.txt", "r")

# init previous
previous = int(input.readline())

# increase counter
i = 0

# loop over lines in file
for line in input:

  current = int(line)

  if previous < current:
    i += 1

  previous = current

# print answer
print('Distance increased %s times' % (i))