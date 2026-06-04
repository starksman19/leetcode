# Design a stack that supports push, pop, top and retrieving the minimum element in constant time.


class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

print(min_stack.getMin())
assert min_stack.getMin() == -3

min_stack.pop()

print(min_stack.top())
assert min_stack.top() == 0

print(min_stack.getMin())
assert min_stack.getMin() == -2
