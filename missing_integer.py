# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
MAX_NUMBER = 1000000

def solution(A):
    # write your code in Python 3.6
    num_occurrences = [False] * MAX_NUMBER
    for item in A:
        if item > 0:
            position = item-1
            num_occurrences[position] = True
    for index, found in enumerate(num_occurrences):
        if not found:
            return index+1