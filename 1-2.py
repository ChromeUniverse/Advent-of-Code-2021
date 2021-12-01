input = open("1-1-input.txt", "r")

nums = []
sums = []

# load numbers from input file into list
for num in input:
  nums.append(int(num))

# calculate sums of 3s
for i in range(len(nums)-2):
  sum = nums[i] + nums[i+1] + nums[i+2]
  sums.append(sum)

# print resulting sums
for sum in sums:
  print(sum)

# convert list of ints into list of strs
sums_str = [str(num) for num in sums]

# write sums to file
output = open('1-2-sums.txt', 'w')
output.write('\n'.join(sums_str))
output.close()


