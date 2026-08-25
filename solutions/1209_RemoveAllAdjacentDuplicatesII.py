def removeDuplicates(s, k):
    stack = [] # [char, count]

    for ch in s:

        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1 

        else:
            stack.append([ch, 1])
        # print(f"c: {ch}, stack: {stack}")

        if stack[-1][1] == k:
            # print(f"popping {ch}")

            stack.pop()

    return "".join([char*count for char, count in stack])


def removeDuplicates_fat(s, k):
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

