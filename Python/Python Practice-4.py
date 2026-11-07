1. To find the second largest value in the list:
lst = [10, 20, 30, 50, 50]

second_highest = sorted(set(lst))[-2]

print(second_highest)
** output: 30
==============================
2. To reverse a list using 2 pointer approach:

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


arr1 = [3, 4, 5, 6, 7, 8]

print(reverse(arr1))
========================
