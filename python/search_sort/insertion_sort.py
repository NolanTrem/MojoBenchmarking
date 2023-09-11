"""
Implementation of the insertion sort based off the zero-based array pseduocode from Wikipedia:
https://en.wikipedia.org/wiki/Insertion_sort
"""

def insertion_sort(A):
    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            # swap A[j] and A[j-1]
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
        i = i + 1
    return A
