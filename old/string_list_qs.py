# 1. Convert a comma-separated string into a list of strings.

st = "This, is, a, comma, separated, string,"

stlist = st.split(" ")

stlist = map(lambda x: x[:-1] if x[-1] == "," else x, stlist)

print(list(stlist))

# 2. Convert a list of strings into a single string, separated by spaces.

liststr = ['This', 'is', 'a', 'comma', 'separated', 'string']

print(" ".join(liststr))

# 6. Remove all words shorter than 3 characters from a sentence.

test = "This is a test string with words shorter than 3 chars"

listtest = test.split(" ")

listtest = filter(lambda x: len(x) >= 3, listtest)

print(" ".join(listtest))

# 16. Remove all punctuation from a string and split it into a list of words.

punctuation = [",","?","!"]

sent = "This is a test, with punctuation! Does it work?"


without = filter(lambda x: x not in punctuation, sent)
print("".join(without))

# 12. Replace the third word in a sentence with another word.

test = "This test string with words shorter than chars"

listtest = test.split(" ")

listtest[2] = "replaced"

print(" ".join(listtest))

# 31. Write a function that takes a string as input and returns a dictionary where keys are characters and values are their frequencies in the string.
strr = "dddeeffff"

counter = {}

for s in strr:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1
    
print(f"Count {counter}")

# 32. Given two dictionaries, merge them into one. If a key exists in both dictionaries, add their values together.

# dic1 = {'a': 2, 'b': 2, 'c': 4, 'd': 1}
# dic2 = {'d': 3, 'e': 2, 'f': 4}

# for key, value in dic2.items():
#     if key not in di

# print(dict(zip(dic1, dic2)))


# Split a string into a list of words.