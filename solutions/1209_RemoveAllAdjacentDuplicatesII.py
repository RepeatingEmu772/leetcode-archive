def removeDuplicates(s, k):
    stack = []

    for c in s:
        stack.append(c)

        # print(f"c: {c}, stack: {stack}")

        if len(stack) >= k and stack[-k:] == [c] * k:
            # print(f"popping {c}")
            for _ in range(k):
                stack.pop()

    return "".join(stack)

print(removeDuplicates("abcd", 2))
print(removeDuplicates("deeedbbcccbdaa", 3))
print(removeDuplicates("pbbcggttciiippooaais", 2))

