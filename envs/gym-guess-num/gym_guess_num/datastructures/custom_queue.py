import numpy as np

class Node(object):
    def __init__(self, array):
        self.value = array
        self.next = None
        self.prev = None
    

class CustomQueue(object):
    def __init__(self, array_size, max_size=128):
        self.head = None
        self.tail = None
        self.num_elements = 0
        self.array_size = array_size
        self.max_size = max_size
    def push(self, array):
        assert type(array) == np.ndarray, "The array should np.ndarray"
        assert array.shape == (self.array_size,), "Incompatible array shape. Expected array of shape ({},) but got array size of {}".format(self.array_size, array.shape)
        node = Node(array)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            
        else:
            if self.head is None:
                current = self.tail
                while  current.prev is not None:
                    current = current.prev
                self.head = current
            elif self.tail is None:
                current = self.head
                while  current.next is not None:
                    current = current.next
                self.tail = current
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.num_elements+=1
        if self.num_elements> self.max_size:
            self.pop()
    def pop(self):
        if self.head is None and self.tail is None:
            self.num_elements = 0
            return None
        else:
            if self.head is None:
                current = self.tail
                while  current.prev is not None:
                    current = current.prev
                self.head = current
            elif self.tail is None:
                current = self.head
                while  current.next is not None:
                    current = current.next
                self.tail = current
            if self.head.next == None:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.num_elements -= 1
    def to_numpy_array(self):
        output = np.zeros((self.max_size, self.array_size))
        i = 0
        current = self.head
        while current is not None:
            output[i] = current.value
            i+=1
            current = current.next
        return output
            
            
                        
            
        
    