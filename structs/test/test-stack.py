from structs import Stack
import pytest 

class TestStack():

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        
