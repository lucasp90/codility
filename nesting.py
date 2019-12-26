# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1
    stack = []
    for c in S:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 0
            last_char = stack[-1] 
            if last_char == '(':
                stack.pop()
    return 1 if len(stack) == 0 else 0
    