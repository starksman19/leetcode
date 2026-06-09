# LeetCode: https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val_list or self.min_val_list[-1] >= val:
            self.min_val_list.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_val_list[-1] == val:
            self.min_val_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val_list[-1]


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
