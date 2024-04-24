class Stack:
    def __init__(self):
        self.stack = []
#-------------check stack is empty or not?
    def is_empty(self):
        return len(self.stack) == 0
#-------------pushed element to the stack
    def push(self, item):
        self.stack.append(item)
#-------------pop last pushed element in stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty!")
            return None
#-------------display last pushed element without pop in stack
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None
#-------------display number of element in stack
    def size(self):
        return len(self.stack)
#-------------display stack content from top to down
    def display(self):
        if not self.is_empty():
            print("Stack contents:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty!")
stack = Stack()

print("Is the stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top of the stack:", stack.top())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack size after popping:", stack.size())

stack.display()