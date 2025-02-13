# 1. Write a Python function to reverse a string.

name = "apple"

print('reverse', name[::-1])

# 2. Count the number of vowels in a given string.

name = "apple"

vowels = [x for x in name if x in ["a","e","i","o","u"]]

print(f'total vowels in {name} is {len(vowels)}')

# 3. Check if a string is a palindrome.
strr =  "apple"

print("Palindrome" if strr == strr[::-1] else "not Palindrome")

# 4. Convert all characters in a string to uppercase.

strr = "apple"
print(strr.upper())

# 5. Replace all spaces in a string with underscores.

strr = "this is an example string"
all_un = ["_" if x == " " else x for x in strr]

print(''.join(all_un))

# 11. Extract the first 5 characters of a string.

strr = "extractfirstfivechars"

print(strr[:5])

# 2.6 Format a string to include two variables: name and age. (Example: "My name is {name}, and I am {age} years old.")

name = "Drishtant"

age = 26

example = f'My name is {name}, and I am {age} years old.'

print(example)


# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


candies = [12,1,12]
extraCandies = 10
# Output: [true,false,true]

max_org = max(candies)

test_res = [True if x + extraCandies >= max_org else False for x in candies]

print(test_res)

# Flowerbed
flowerbed = [1,0,0,0,0,0,1]
n = 2
# Output: true
c = 0
for i in range(len(flowerbed)):
    print(i)
    if flowerbed[i] == 0:
        empty_left = i==0 or flowerbed[i-1] == 0
        empty_right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

        if empty_left and empty_right:
            c += 1
            flowerbed[i] = 1

print(n <= c)

# Reverse vowel in a string

s = "IceCreAm"

# Output: "AceCreIm"

vowels = ['a','e','i','o','u']

store_v = [ x for x in s if x.lower() in vowels]
s = ["_" if x.lower() in vowels else x for x in s]
print(store_v)
store_v = store_v[::-1]
print(store_v)
print(s)

index = 0

for i in range(len(s)):
    if s[i] == "_":
        s[i] = store_v[index]
        index += 1
    
print(''.join(s))



