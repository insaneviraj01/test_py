
def is_palindrome(num):
    return str(num) == str(num) [::-1]
print(is_palindrome(121))

def reverse_string(text):
    return text[::-1]
print(reverse_string('vikas'))

def is_factorial(n):
    if n==0 or n==1:
        return 1
    return n*is_factorial(n-1)
print(is_factorial(5))
