# read input file
input = open("2-1-input.txt", "r") 

# initial values
y = 0   # depth
x = 0   # horizontal position

# looping over lines in input file
for line in input:
  command, value = line.split(' ')
  value = int(value)
  if command == 'forward':
    x += value
  if command == 'down':
    y += value
  if command == 'up':
    y -= value
    
# compute answer and print it
answer = x * y
print(answer)