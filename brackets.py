# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

matches = { '{': '}', '[': ']', '(': ')'}

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1
    stack = []
    for c in S:
        if c in '{[(':
            stack.append(c)
        elif c in '}])':
            if len(stack) == 0:
                return 0
            last_char = stack[-1] 
            if matches[last_char] == c:
                stack.pop()
    return 1 if len(stack) == 0 else 0
    
