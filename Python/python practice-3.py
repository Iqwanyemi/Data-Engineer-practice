
1️⃣ Reverse a string without using [::-1]  
python
def reverse_string(s):
    return ''.join(reversed(s))

print(reverse_string("hello"))  # Output: "olleh"


2️⃣ Count frequency of elements in a list  
python
from collections import Counter

data = [1, 2, 2, 3, 3, 3]
counts = Counter(data)
print(counts)  # Output: {3: 3, 2: 2, 1: 1}


3️⃣ Check if two strings are anagrams  
python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True


4️⃣ Find duplicates in a list  
lis =[1,2,2,3,3]
uniq =[]

for i in lis:
  if i not in uniq:
    uniq.append(i)
print(uniq) 


5️⃣ Lambda function to square numbers in a list  
python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]



6. To print middle element in the list:

a=[12,31,34,99,21]
b=int(len(a)/2)
print(a[b])

**output:34
