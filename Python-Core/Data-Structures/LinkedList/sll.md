## 1. Implementing a Singly Linked List
```python
## Node Class
class Node(object):
        def __init__(self,data):
            self.data = data
            self.next =None


## Linked list
class LinkedList(object):  ## we can remove object in python3+ Because in Python 3, all classes implicitly inherit from object. 
       def __init__(self, head)
                self.head =None  # Pointer to the first Node

```

## 2. Problems 

### 2.1 Length of Linked List
* Given the head of a singly linked list, find the length of the linked list.
```python

def length_of_linkedlist(head):
    # Base Case 
    if head is None:
        return 0

    else:
        count = 0
        current = head 
        while current:
            count +=1
            current = current.next
    return count


# Recursive Approach
def length_recursive(node):
    if not node:          # base case: end of list
        return 0
    return 1 + length_recursive(node.next)

## Simpler, but beware of recursion depth if the list is very long.

if __name__ == "__main__":
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None








