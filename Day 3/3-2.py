filename = "3-input.txt"

# read input file
input = open(filename, "r") 

width = 12
size = 1000


# Getting Oxygen rate

# getting all numbers in string format
nums = [str(line[:width]) for line in input]

i = 0

while len(nums) > 1:

  # list of filtered numbers
  filtered = []

  # getting count in i-th bit 
  count = sum(int(num[i]) for num in nums)

  # filtering numbers
  if count > size/2: 
    for num in nums:
      if int(num[i]) == 1:
        filtered.append(num)
  
  if count < size/2: 
    for num in nums:
      if int(num[i]) == 0:
        filtered.append(num)

  if count == size/2: 
    for num in nums:
      if int(num[i]) == 1:
        filtered.append(num)

  i += 1
  nums = filtered 
  size = len(filtered)

oxygen = int(nums[0],2)
print(oxygen, 'is the oxygen rating')

# Resetting input file
input.close()
input = open(filename, "r") 

# Getting CO2 Scrubber rate

# getting all numbers in string format
nums = [str(line[:width]) for line in input]

i = 0

while len(nums) > 1:

  # list of filtered numbers
  filtered = []

  # getting count in i-th bit 
  count = sum(int(num[i]) for num in nums)

  # filtering numbers
  if count > size/2: 
    for num in nums:
      if int(num[i]) == 0:
        filtered.append(num)
  
  if count < size/2: 
    for num in nums:
      if int(num[i]) == 1:
        filtered.append(num)

  if count == size/2: 
    for num in nums:
      if int(num[i]) == 0:
        filtered.append(num)
        
  i += 1
  nums = filtered 
  size = len(filtered)

co2 = int(nums[0],2)
print(co2, 'is the CO2 rating')

answer = oxygen * co2
print(answer)