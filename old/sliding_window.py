# 1. Find the maximum sum of a subarray of size k in an array.

array = [2, 1, 5, 1, 3, 2]
k = 3

window_arr = array[:k]

window_sum = sum(window_arr)
max_sum = window_sum

print(window_sum)

for i in range(k, len(array)):
    window_sum = window_sum + array[i] - array[i-k]
    print(window_sum)

# 2. Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

nums = [3,3,4,3,0]
k = 4
# Output: 12.75000

int_window = nums[:k]
int_sum = sum(int_window)

max_sum = int_sum
print(max_sum/4)

for i in range(k, len(nums)):
    int_sum = int_sum + nums[i] - nums[i-k]
    max_sum = max(int_sum, max_sum)

print(max_sum/4)

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

s = "abciiidef"
k = 3

vowels = ['a','e','i','o','u']

int_window = s[:k]
int_vowels = [x for x in int_window if x in vowels]

max_vowels = len(int_vowels)

for i in range(k, len(s)):
    int_window = int_window + s[i]
    int_window = int_window[1:]
    int_vowels = [x for x in int_window if x in vowels]
    max_vowels = max(max_vowels, len(int_vowels))

print(max_vowels)
