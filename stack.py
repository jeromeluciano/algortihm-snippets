class Stack:
    def __init__(self):
        self.stack = []

    def add(self, element):
        '''
        @classmethod Stack
        @add will add new element at the top of the stack
        '''
        self.stack.append(element)
        return True

    def pop(self):
        '''
        @classmethod Stack
        @pop will remove element at the top of the stack
        '''
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)
stack.add(5)
stack.add(6)

print(stack.peek())
print(stack.pop())
print(stack.peek())