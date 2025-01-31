# Problem: Write a recursive function to compute the factorial of a number n (n! = n * (n-1) * ... * 1).
# Example: factorial(5) -> 120

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(5))

# Write a function to find the sum of digits of a positive integer using recursion.

# sumOfDigits(123) -> 6

def sumOfDigits(num):
    if num == 0:
        return 0
    dig = num % 10
    num = num//10
    return dig + sumOfDigits(num)

print(sumOfDigits(214))


# Write a function to print numbers from 1 to n using recursion.
# Example: printNumbers(5) -> 1 2 3 4 5

def printNumbers(num):
    if num == 0:
        return 1
    printNumbers(num - 1)
    print(num)

printNumbers(5)

# Problem: Write a recursive function to reverse a string.
# Example: reverseString("hello") -> "olleh"

def reverseString(strr):
    if strr == "":
        return ""
    last_ele = strr[-1]
    strr = strr[:len(strr) - 1]
    return last_ele + reverseString(strr)

print(reverseString("hello"))


# Write a function to find the nth Fibonacci number using recursion.
# Example: fibonacci(5) -> 5 (Sequence: 0, 1, 1, 2, 3, 5)

def fibo(num):
    if num <= 0:
        return 0
    return fibo(num-1) + fibo(num-2)

print(fibo(7))


# Write a recursive function to check if a string is a palindrome.
# Example: isPalindrome("radar") -> True

def palin(strr):
    if strr == "":
        return ""
    last_ele = strr[-1]
    strr = strr[:len(strr) - 1]
    return last_ele + reverseString(strr)

print(palin("hello"))