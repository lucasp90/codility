def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    for _ in range(K):
        A = [A[-1]] + A[:-1]
    return A