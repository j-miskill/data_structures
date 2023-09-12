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
        
