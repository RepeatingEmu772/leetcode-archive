def evalRPN(tokens):

    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)
 
            elif token == "*":
                stack.append(a * b)

            else:
                stack.append(int(a / b))

    return stack[-1]

print(evalRPN(["2"]))
print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


