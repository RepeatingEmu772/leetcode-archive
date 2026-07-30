def isValid(s):
    stack = []
    for i in s:
        # print(i)
        if i in ['(', '[', '{']:
            stack.append(i)
        elif i in [')', ']', '}']:
            if len(stack) == 0:
                return False
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("([)]"))
