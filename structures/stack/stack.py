

class Stack:
    
    def __init__(self):
        self._stack_size = 0
        self.stack = []

    def push(self, val):
        self._stack_size += 1
        self.stack.append(val)

    def pop(self):
        self._stack_size -= 1
        return self.stack.pop()
    
    def top(self):
        if self._stack_size == 0:
            return None
        else:
            return self.stack[self._stack_size - 1]
        
    def is_empty(self):
        if self._stack_size == 0:
            return True
        else:
            return False
    
    def stack_size(self):
        return self._stack_size
        
    
    def __str__(self):
        return str(self.stack)
