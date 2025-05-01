
def reverse_string(text):
    return text[::-1]
print(reverse_string('vikas'))

def is_palindrome(num):
    return str(num) ==str(num)[::-1]
print(is_palindrome(121))

def is_anagram(str1, str2):
    return sorted(str1) ==sorted(str2)
print(is_anagram(str1='act',str2='cat'))

def factorial( n):
    if n ==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def largest_numbers(numbers):
    largest =numbers[0]
    for num in numbers:
        if num>largest:
            largest = num
    return largest
print(largest_numbers([1,2,46,43,98,4565,4321,]))

for n in range(1,11):
    if n %2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

x = 7
for i in range(2,x):
    if x%i==0:
        print(x,"is not prime number")
        break
else:
    print(x, "is prime number")

def find_even_odd():
    evenList=[]
    oddList=[]
    for num in range(1,11):
        if n%2==0:
            evenList.append(n)
        else:
            oddList.append(n)
    return evenList ,oddList
even_number, odd_number = find_even_odd()
print('Even numbers',even_number)
print('Odd numbers',odd_number)


a,b = 5,10
a,b = b,a
print(a,b)

print(factorial(5))

k1 = [11,22,33,44,55,66,77,88,99,00]
x=0
while (x<len(k1)):
    print(k1[x],end=",")
    x=x+1

print()
#reverse name
name = "vikas"
print(name[::-1])


#print tuple is sort
t1 = (11,22,33,44,55,66,77,88,99,00)
t2 = list(t1)
t2.sort()
t1=tuple(t2)
print(t1)

def demo():
    print("test")
demo()


