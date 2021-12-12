from __future__ import annotations
from typing     import Any, Type

class Node:
    
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        
        self.data = data
        self.prev = prev or self
        self.next = next or self
        
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = self.current = Node()
        self.no = 0
        
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.head.next is self.head
    
    def search(self, data: Any) -> Any:
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0
    
    def print_current_node(self) -> None:
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)
            
    def print(self) -> None:
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next
            
    def print_reverse(self) -> None:
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev
            
    def next(self) -> bool:
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True
    
    def prev(self) -> bool:
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True
    
    def add(self, data: Any) -> None:
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1
        
    def add_first(self, data: Any) -> None:
        self.current = self.head
        self.add(data)
        
    def add_last(self, data: Any) -> None:
        self.current = self.head.prev
        self.add(data)
        
    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next
                
    def remove(self, p: Node) -> None:
        ptr = self.head.next
        
        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            
            ptr = ptr.next
            
    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()
        
    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()
        
    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0


a = DoubleLinkedList()
a.add('a')
a.add('b')
a.add('c')
a.add('d')
a.add('e')
a.add('f')
a.add('g')
a.add_first('h') # a라는 원형 이중 연결 리스트 생성 및 요소 추가
a.print() # a의 요소 출력
print("-------------------------------------------------")
a.print_current_node() # a의 주목 노드 출력
print('a.no: ', a.no) # a의 총 요소의 수
# print('a.search(): ', a.search("g")) # a에서 특정 값 찾기(주목 노드도 변경)
print('a.head: ', a.head, a.head.data) # a의 head 값
print('a.current: ', a.current.data) # a의 주목 노드의 값
a.next() # a의 주목 노드를 다음 노드로 변경
print('a.current: ', a.current.data) # a의 주목 노드의 값
a.prev() # a의 주목 노드를 이전 노드로 변경
print('a.current: ', a.current.data) # a의 주목 노드의 값
print(a.current.prev.prev.data)
print(a.current.next.next.data)
print("-------------------------------------------------")
a.remove_current_node()
a.remove_first()
a.remove_last()
a.remove(a.current)
a.print()
print("-------------------------------------------------")
a.clear()
a.print()
