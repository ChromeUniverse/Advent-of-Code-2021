from math import floor

# read input file
# input = open("3-alt-input.txt", "r") 
input = open("3-input.txt", "r") 

width = 12
size = 1000

counts = [0] * width
gamma_rate = [0] * width
epsilon_rate = [0] * width

# initial values
# looping over lines in input file
for line in input:
  str_num = list(line)
  for i in range(width):
    char = str_num[i]
    if char != '\n':
      counts[i] += int(char)

print(counts)

# building gamma and epsilon rates
for i in range(width):
  count = counts[i]
  if count < floor(size/2):
    gamma_rate[i] = 1
    epsilon_rate[i] = 0
  else: 
    gamma_rate[i] = 0
    epsilon_rate[i] = 1

print(gamma_rate)
print(epsilon_rate)

# convert rate lists to decimal numbers
def to_dec(rate_list):
  rate_list = [str(i) for i in rate_list] 
  rate_list = ''.join(rate_list)
  rate = int(rate_list, 2)
  return rate

gamma = to_dec(gamma_rate)
epsilon = to_dec(epsilon_rate)

print('Here is gamma', gamma)
print('Here is epsilon', epsilon)

answer = gamma * epsilon
print('Here is answer', answer)
