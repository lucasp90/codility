# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    expected_sum = 0
    real_sum = -len(A)
    for index, value in enumerate(A):
        expected_sum += (index + 1)
        real_sum += value
    return expected_sum - real_sum
