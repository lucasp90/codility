# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count = {}
    max_value = len(A)
    for value in A:
        count[value] = count.get(value, 0) + 1
        if count[value] > 1 or value > max_value:
            return 0
    return 1
