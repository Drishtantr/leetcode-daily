# Given an array of integers, return the length of the longest sequence of consecutive increasing numbers.

nums = [1, 2, 2, 3, 4, 5]

current_s = 0
max_s = 0

for i in range(1, len(nums)):
    if(nums[i-1] < nums[i]):
        current_s += 1
        max_s = max(max_s, current_s)
    else:
        current_s = 0

print(max_s)

# Given a binary array nums, return the length of the longest sequence of consecutive 1s.
nums = [1, 1, 0, 1, 1, 1]
max_l = 0
current_l = 0

for num in nums:
    if num == 1:
        current_l +=1
        max_l = max(max_l, current_l)
    if num == 0:
        current_l = 0

print(max_l)
    
# Given a string s and a character c, return the length of the longest sequence of consecutive occurrences of c.
strr = "aaabbbaaaccc"
c = 'a'

current_l = 0
max_l = 0

for s in strr:
    if s == 'a':
        current_l += 1
        max_l = max(max_l, current_l)
    else:
        current_l = 0

print(max_l)


# Given an array of integers, return the length of the longest sequence of consecutive even numbers.

nums = [2, 4, 1, 6, 8, 10, 1, 2]


current_l = []
max_l = []

for n in nums:
    if n % 2 == 0:
        current_l.append(n)
        high_len = max_l > current_l 
        max_l = max_l if high_len else current_l
    else:
        current_l = []

print(max_l)