def solution(A):
    # write your code in Python 3.6
    element_count = {}
    for value in A:
        element_count[value] = element_count.get(value, 0) + 1
    unpaired_found = False
    for element, count in element_count.items():
        unpaired_found = count % 2 == 1
        if unpaired_found:
            return element