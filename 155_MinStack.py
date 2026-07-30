class MinStack:

    def __init__(self):
        self.stack = [] 
        self.curr_min = float("inf")

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.curr_min = min(self.curr_min, value)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        
        if self.stack == []:
            self.curr_min = float("inf")

        if popped == self.curr_min:
            self.curr_min = min(self.stack)


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min
        
        

s = MinStack()
s.push(5)
s.pop()
s.push(10)
print(s.getMin())
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(5)
# obj.push(-1)
# obj.push(2)
# obj.pop()
# param_3 = obj.top()
# print(param_3)
# param_4 = obj.getMin()
# print(param_4)

# print(obj.stack)