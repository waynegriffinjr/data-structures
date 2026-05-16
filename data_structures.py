from collections import deque


class Node:
    '''A single node in a linked list.'''
    
    def __init__(self, value):
        self.value = value #The data this node holds
        self.next = None  #Reference to the next node (none = end of chain)
        
    def __repr__(self):
        return f"Node ({self.value})"
    
class LinkedList:
    '''A singly linked list.'''
    
    def __init__(self):
        self.head = None #The list starts empty => no nodes yet
        
    def insert_at_beginning(self, value):
        '''Add a new node at the front of the list. 0(1) time.'''
        new_node = Node(value)
        new_node.next = self.head #New node points to the old head
        self.head = new_node #New node becomes the new head
        
    def insert_at_end(self, value):
        '''Add a new node at the end of the list. 0(n) time - must walk to the end'''
        new_node = Node(value)
        if self.head is None: #if the list is empty, new node is the head
            self.head = new_node #New node becomes the new head
            return
        current = self.head
        while current.next:  #Walk to the last node
            current = current.next
        current.next = new_node #Last node now points to the new node
        
    def display(self):
        '''Prints the list in a readable format.'''
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
            
        print(" -> ".join(elements) + " -> None")
        
    def search(self, target):
        '''Finds a clue in the list. Return True/False'''
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False
    
    
    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        current = self.head
        previous = None
        
        while current:
            if current.value == target:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            
            previous = current
            current = current.next
            
        return False
            
    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        py_list = []
        current = self.head
        while current:
            py_list.append(current.value)
            current = current.next
        return py_list
        

    def is_balanced(text):
        """Return True if all brackets in text are properly matched.
        Handles: (), [], {}
        """
        stack = []   #Stack data structure (Last In, First Out - [LIFO])
        pair_match = {')': '(', ']': '[', '}': '{'} #Mapping Dictionary
        
        for ch in text:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack:
                    return False
                if stack.pop() != pair_match[ch]:
                    return False
        return len(stack) == 0
                    
    
# - Queue: Task Processor

class TaskProcessor: #First In, First Out (FIFO)
    
    def __init__ (self, name):
        self.name = name
        self.task_list = deque()
        
    
    def add_task(self, name):
        self.task_list.append(name)
        
    def process_next(self):
        if not self.task_list:
            return None
        return self.task_list.popleft()
        
        




    
    
    
    

    # # Tests:
    # print(is_balanced("()"))           # True
    # print(is_balanced("({[]})"))       # True
    # print(is_balanced("(]"))           # False
    # print(is_balanced("([)]"))         # False
    # print(is_balanced("hello (world)")) # True









        
# ll = LinkedList()
# for val in [10, 20, 30, 40, 50]:
#     ll.insert_at_end(val)

# ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
# print(ll.length())     # 5
# ll.delete(30)
# ll.display()           # 10 -> 20 -> 40 -> 50 -> None
# print(ll.to_list())    # [10, 20, 40, 50]
    
    
    
    
    
    # TEST
    
# my_list = LinkedList()
# my_list.insert_at_beginning(3)        
# my_list.insert_at_beginning(2) 
# my_list.insert_at_beginning(1)

# my_list.insert_at_end(4.6) 

# my_list.display() 


# print(my_list.search(3))      
# print(my_list.search(7)) 


#   STACK: Last In, First Out (LIFO)

# stack = []

# stack.append("page_1") #Visit page 1
# stack.append("page_2") #Visit page 2
# stack.append("page_3") #Visit page 3

# print("Stack:", stack)

# back = stack.pop() #Go back - remove the most recent
# print("Clicked back on page:", back)
# print("Stack now:", stack)

# #Queue is First In, First Out (FIFO)

# queue = deque()

# queue.append("customer_1") #Customer 1 joins line
# queue.append("customer_2") #Customer 2 joins line
# queue.append("customer_3") #Customer 3 joins line

# print("Queue:", list(queue))

# served = queue.popleft() # Dequeue - Serve the first customer

# print("Served:", served).        # 'customer_1' — first in, first out
# print("Queue now:", list(queue)) # deque(['customer_2', 'customer_3'])
