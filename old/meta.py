#1. palindrome two pointer

def palindrome_normal(s):
    s = "tab a cat"

    s = s.lower().replace(" ", "")
    s = list(s)
    s = [x for x in s if x.isalpha()]

    rev = s[::-1]

    return (s == rev)

def palindrome_two_pointers(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l +=1
        while l < r and not s[r].isalnum():
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True

print(palindrome_two_pointers('ma?dam?'))
        