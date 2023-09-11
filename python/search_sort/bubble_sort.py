"""
Implementation of the insertion sort based off the zero-based array pseduocode from Wikipedia:
https://en.wikipedia.org/wiki/Bubble_sort
"""

def bubble_sort(A):
    n = len(A)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if A[i-1] > A[i]:
                # swap A[i-1] and A[i]
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
    return A
