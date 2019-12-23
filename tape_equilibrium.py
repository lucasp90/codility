import sys
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    total = sum(A)
    min_diff = sys.maxsize
    part_left = 0
    part_right = max
    for item in A[:-1]:
        part_left += item
        part_right = total-part_left
        min_diff = min(min_diff, abs(part_left - part_right))
    return min_diff
