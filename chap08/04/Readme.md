# 원형 이중 연결 리스트(Circular Double Linked List)

원형 이중 연결 리스트는 원형 리스트와 이중 연결 리스트가 합쳐진 형태를 말합니다.
- 원형 리스트는 리스트의 꼬리노드가 다시 머리노드를 가리키는 모양을 하고있으며,
- 이중 연결 리스트는 각 노드의 뒷 노드에 뿐 아니라 앞 노드에 대한 포인터도 가지고 있는 연결 리스트를 말합니다.

즉 원형 이중 연결 리스트는 머리와 꼬리노드가 서로 연결되어있으면서 앞, 뒤 노드에 대한 포인터를 모두 가지고있는 형태를 말하는 것입니다.
<br><br>

## 원형 이중 연결 리스트의 구조
![img](https://media.geeksforgeeks.org/wp-content/uploads/Circular-doubly-linked-list.png) 
<br>
- data : 현재 노드의 데이터에 대한 참조
- prev : 이전 노드에 대한 참조
- next : 다음 노드에 대한 참조
- head : 리스트의 머리 노드에 대한 참조
- no : 리스트 노드의 수
- current : 주목 노드에 대한 참조
<br><br>

## 원형 이중 연결 리스트 구현
```python
from __future__ import annotations
from typing import Any, Type

class Node:
    
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    
    def __init__(self) -> None:
        self.head = self.current = Node()
        self.no = 0
```
원형 이중 연결 리스트 클래스의 생성자를 통해 객체를 생성하면 노드 클래스를 인스턴스화하여 head에 담는것을 볼 수 있습니다.

또한 노드의 삽입과 삭제를 원활하게 할 수 있도록 head라는 더미 노드를 가집니다.
<br><br>

## 원형 이중 연결 리스트의 메소드
### 1. \_\_init__()
- 빈 원형 이중 연결 리스트를 생성
### 2. \_\_len__()
- 리스트에 등록된 데이터의 수를 반환
### 3. is_empty()
- 리스트가 비어있는지를 검사하는 메소드
- head노드(더미노드)만 존재한다면 True를 그렇지 않다면 False를 반환한다.
- 판단의 기준은 head노드가 참조하는 대상이 head인지 다른 노드인지를 확인
### 4. search()
- 인수로 주어진 데이터와 값이 같은 노드를 선형 검색하는 함수
- head노드(더미노드)를 제외하고 그 다음 노드부터 검색한다. 즉 검색의 시작점은(head.next)
- 검색된 데이터를 반환하며 추가로 주목 노드또한 변경된다.
### 5. \_\_contains__()
- 리스트에 데이터와 같은 값이 있는지 판단하는 함수, 존재하면 True, 아니면 False 반환
### 6. print_current_node()
- 주목 노드의 데이터 current.data를 출력
### 7. print()
- 리스트에 있는 모든 노드를 순서대로 출력하는 함수
### 8. print_reverse()
- 리스트에 있는 모든 노드를 역순으로 출력하는 함수
### 9. next()
- 주목 노드를 한 칸 뒤로 이동시키는 함수, 리스트가 비어있지 않고 뒤에 노드가 존재할 경우만 이동, 주목 노드가 이동하면 True 아니면 False 반환
### 10. prev()
- 주목 노드를 한 칸 앞으로 이동시키는 함수, 리스트가 비어있지 않고 앞에 노드가 존재할 경우만 이동, 주목 노드가 이동하면 True 아니면 False 반환
### 11. add()
- 주목 노드 뒤에 노드를 추가하는 함수
### 12. add_first()
- head노드 바로 뒤에 노드를 추가하는 함수
### 13. add_last()
- 마지막에 노드를 추가하는 함수
### 14. remove_current_node()
- 주목 노드를 삭제하는 함수, 더미노드를 삭제할 수 없기 때문에 리스트가 비어있는지를 확인하고 비어있으면 삭제 처리를 수행한다.
### 15. remove()
- 임의의 노드 p(p가 참조하는 노드)를 삭제하는 함수, 리스트가 비어있지 않고 인수로 주어진 노드 p가 존재하는 경우에만 수행한다.
### 16. remove_first()
- 역시 head노드를 삭제할 수 없기 때문에 head.next노드를 삭제한다.
- 주목 포인터 current가 참조하는 곳을 head.next로 업데이트한 후 remove_current_node()를 수행한다.
### 17. remove_last()
- 마지막 노드를 삭제하는 함수
- remove_first()와 같은 방식으로 주목 포인터가 참조하는 노드를 head.prev로 업데이트한 후 remove_current_node()를 수행한다.
### 18, clear()
- head노드 이외의 모든 노드를 삭제하는 함수
- 리스트가 빌 때까지 remove_first()를 반복한다.
- 삭제 후 주목 포인터 current가 참조하는 곳을 head노드로 업데이트된다.