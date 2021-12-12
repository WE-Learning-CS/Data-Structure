from __future__                 import annotations
from typing                     import Any, Type
from . circularDoubleLinkedList import *

def __iter__(self) -> DoubleLinkedListIterator:
    return DoubleLinkedListIterator(self.head)

def __reversed__(self) -> DoubleLinkedListReverseIterator:
    return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next
        
    def __iter__(self) -> DoubleLinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        
class DoubleLinkedListReverseIterator:
    
    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev
        
    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        
        else:
            data = self.current.data
            self.current = self.current.prev
            return data