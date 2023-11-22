# Stack Notes

A stack is a list data structure that follows a pattern for putting and pulling from the list. Items are appended to the end of the list and then are either pulled from the front (first in, first out) or pulled from the rear (first in, last out). 

### What methods do we need to implement a stack?

```python
stack.empty()  # checks if the stack is empty
stack.size()   # returns length of stack
stack.top()    # returns the first element 
stack.push()   # puts an element on the stack
stack.pop()    # pulls the first element from stack
```


### What are stacks used for?

My ideas:
1. Ordering of jobs that need to be done. 
2. Ordering processes that a computer should do. 
3. Arranging elements that need to be processed. 
4. Making a sandwich (a burger)
5. Holding previous values while new values are processed.

Other ideas:
1. Undo and redo functions on a computer (keeps track)
2. Reverse the elements of a list!
3. Backtracking algorithms
4. Used in compiler designs


### How can a stack be implemented in Python? 

1. With a `list`
2. With `collections.deque`
3. With `queue.LifoQueue`

### How will I implement? 

I will be implementing a stack from the ground up. 

