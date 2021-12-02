# read input
input = open("2-1-input.txt", "r") 

# initial values
a = 0   # aim
y = 0   # depth
x = 0   # horizontal position

# looping over lines in input file
for line in input:
  command, value = line.split(' ')
  value = int(value)
  if command == 'forward':
    x += value
    y += a * value
  if command == 'down':
    a += value
  if command == 'up':
    a -= value

# compute answer and print it
answer = x * y
print(answer)