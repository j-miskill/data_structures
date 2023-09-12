

class Stack:
    
    def __init__(self):
        self.size = 0
        self.stack = []

    def push(self, val):
        self.size += 1
        self.stack.append(val)

    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def top(self):
        if self.size == 0:
            return None
        else:
            return self.stack[self.size - 1]
        
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def size(self):
        return self.size
    
    def __str__(self):
        return str(self.stack)
