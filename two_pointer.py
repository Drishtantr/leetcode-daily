# You are given a sorted list of integers and a target sum. Determine if there exists a pair of numbers in the list that adds up to the target sum.

# Example:
# Input:

listt = [1, 2, 3, 4, 6]
t = 6

left = 0
right = len(listt) - 1

c = 0
while left < right:
    summ = listt[left] + listt[right]
    if summ == t:
        c = summ
    if summ < t:
        left +=1
    else:
        right -= 1

print(c)

# You are given a string. Reverse the string in-place using the two-pointer technique.

# Input:
# "hello"

# Output:
# "olleh"

ip = "hello"

ip = list(ip)

left = 0
right = len(ip) - 1
ip_old = ''.join(ip)

while left < right:
    ip[left], ip[right] = ip[right], ip[left]
    left += 1
    right -=1

print(''.join(ip), ip_old)

# Remove duplicates from a sorted array and return the length of the modified array.

arr = [1, 1, 2, 2, 3, 4, 4]
new_arr = []
left = 0
right = len(arr) - 1

while left < right:
    if arr[left] not in new_arr:
        print(True)
        new_arr.append(arr[left])
    if arr[right] not in new_arr:
        print(False)
        new_arr.append(arr[right])
    left +=1
    right -= 1

print(new_arr, len(new_arr))

# Find all pairs in a sorted array that have a difference equal to k.
array = [1, 3, 5, 7, 9]
k = 2

# [(1, 3), (3, 5), (5, 7), (7, 9)]

left = 0
right = len(array) - 1
pairs = []

while left < right:
    diff = arr[right] - arr[left]
    print(f"diff arr[right] - arr[left]")
    if diff == k:
        pairs.append((arr[right], arr[left]))
        right -=1
        left +=1

print(pairs)




