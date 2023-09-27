from stack import Stack
import pytest 

class TestStack():

    def test_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s is not None
        
    def test_top(self):
        s = Stack()
        s.push(1)
        s.push(2)
        output = s.top()
        assert output == 2
        assert s.stack_size() == 2
    
    def test_pop(self):
        s = Stack()

        s.push(1)
        s.push(2)
        output = s.pop()
        
        assert output == 2
        assert s.stack_size() == 1

    def test_is_empty(self):
        s = Stack()
        assert(s.is_empty() == True)

        
