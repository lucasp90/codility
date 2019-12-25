# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    counters = [0]*N
    max_value = 0
    for item in A:
        position = item - 1
        if position < N:
            counters[position] += 1
            max_value = max(counters[position], max_value)
        else:
            counters = [max_value]*N
    return counters