def solution(X, A):
    # write your code in Python 3.6
    positions = dict.fromkeys(range(1,X+1), 0)
    covered_positions = 0
    additional_time = 0
    waiting_for_missing_leaf = False
    for time, position in enumerate(A):
        if position <= X:
            positions[position] += 1
            if positions[position] == 1:
                covered_positions += 1
                if waiting_for_missing_leaf:
                    additional_time += time
        if position == X:
            if covered_positions == X:
                return time
            else:
                waiting_for_missing_leaf = True
                additional_time = time
        else:
            if covered_positions == X:
                return additional_time
    return -1