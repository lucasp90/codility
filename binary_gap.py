def solution(N):
    # write your code in Python 3.6
    binary = to_binary(N)
    started = False
    max_gap = 0
    current_gap = 0
    for i in range(len(binary)):
        if not started:
            started = binary[i] == '1'
        else:
            if binary[i] == '1':
                max_gap = max(current_gap, max_gap)
                current_gap = 0
            else:
                current_gap += 1
    return max_gap    

def to_binary(n):
    """
    Converts a given positive number to its representation as a binary string
    """
    binary = ''
    partial_m = n
    while partial_m > 0:
        binary = str(partial_m % 2) + binary
        partial_m = partial_m // 2
    print(binary)
    return binary