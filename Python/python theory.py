1. what is shallow copy and deep copy
Shallow copy copies only the outer object, while deep copy copies the object and all nested objects recursively.
2. what is lambda fn in py?
  A lambda is an anonymous (nameless) function.
3. what is decorator,iterator and generator?
decorator-A function that modifies another function's behavior without changing its code.
  Iterator is an object that implements __iter__() and __next__() methods.
  An iterator is an object used to access elements one by one.
It implements __iter__() and __next__().
Uses iter() and next() functions.
  A special function that uses yield.Instead of storing all values in memory:it generates values one by one.
A generator is a special type of iterator.
Uses the yield keyword instead of return.
Generates values one at a time, saving memory.
4. diff b/w set,tuple,list and dict?

5.what is py packages and py modules?
Module = single .py file. Package = collection of modules organized in a directory.
6. what is try,except block in py ?
7. what is args and kwargs?

1)What is the difference between List, Set and Dictionary?
==========================================================
2)What is List Comprehension?
List comprehension is a short and efficient way to create a new list in Python using a single line of code.
[expression for item in iterable if condition]
numbers = [x * 2 for x in range(5)]

print(numbers)
==============================================
3)What is Lambda Function?
4) difference between append() and extend() with example
5)What is Exception Handling?
6)What is the difference between map(), filter() and reduce()
7)What is the difference between Shallow Copy and Deep Copy?
8)What is type casting in Python?
9)What is an iterator? and What is a generator function
10) write a code for handling retires using python
import time

for i in range(3):
    try:
        print("Attempt:", i + 1)
        result = 10 / 0
        print("Success")
        break

    except Exception:
        print("Failed, retrying...")
        time.sleep(2)
      ============================================
coding 
1) Reverse a string
========================================
2)Find the second-largest number:
nums = [10, 5, 20, 8, 15]

b = list(set(nums))
b.sort(reverse=True)
print(b[1])

=========================================
3)Check palindrome
s = "madam"

if s == s[::-1]:
  print("palindrome")
else:
  print("no")

===========================================
4)Remove duplicates from a list:
nums = [10, 5, 20, 8, 8,15]
result =[]

for i in nums:
  if i not in result:
    result.append(i)
print(result)
===================================================
5)Find missing number in a list and Find the missing numbers in a sequence:
nums = [1,2,3,5]
result=[]
for i in range(min(nums),max(nums)+1):
  if i not in nums:
    result.append(i)
print(result)
==============================================
6)Count words in a string
s = "I love Python programming"
a = len(s.split())
print(a)
===========================================
7)Find the longest word in a sentence
s = "I love Python programming language"

a = s.split()

b = max(a)
print(b)
