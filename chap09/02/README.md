# 이진 검색 트리

![img](https://miro.medium.com/max/1400/1*jBgV9A847f_pHMbO67tcgw.png)

이진 검색 트리는 모든 노드가 다음 조건을 만족해야 한다.

- 왼쪽 서브트리 노드의 키 값은 자신의 노드 키값보다 작아야한다.
- 오른쪽 서브트리 노드의 키 값은 자신의 노드 키 값보다 커야 한다.

### 이진 검색 트리의 특징

- 구조가 단순하다
- 중위 순회의 깊이 우선 검색을 통하여 노드 값을 오름차순으로 얻을 수 있다.
- 이진 검색과 비슷한 방식으로 아주 빠르게 검색할 수 있다.
- 노드를 삽입하기 쉽다.

## 이진 검색 트리 구현하기

### 노드 클래스 Node

``` python
from __future__ import annotations
from typing import Any, Type

class Node:
    '''이진 검색 트리의 노드'''
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key   = key
        self.value = value
        self.left  = left
        self.right = right
        
```

- **key** : 키(임의의 형)을 나타낸다
- **value** : 값(임의의 형)을 나타낸다
- **left** : 왼쪽 자식 노드에 대한 참조(왼쪽 포인터)를 나타낸다
- **right** : 오른쪽 자식 노드에 대한 참조(오른쪽 포인터)를 나타낸다

### 이진 검색 클래스 BinarySearchTree

```python
class BinarySearchTree:
    '''이진 검색 트리'''
    def __init__(self):
        self.root = None # 루트
```

- **root** : 루트에 대한 참조를 유지하는 필드

### 키값으로 노드를 검색하는 search()함수

1. 루트에 주목한다. 여기서 주목하는 노드는 p
2. p가 None이면 검색을 실패하고 종료한다.
3. 검색하는 key와 주목 노드 p의 키를 비교한다.
   1. key == p : 검색을 성공하고 종료
   2. key > p : 주목 노드를 오른쪽 자식 노드로 옮김
   3. key < p : 주목 노드를 왼쪽 자식 노드로 옮김
4. 2번 과정으로 되돌아 간다.

```python
def search(self, key: Any) -> Any:
        '''키가 key인 노드를 검색'''

        p = self.root               # 루트 주목

        while True:
            if p is None:           # 더이상 진행할 수 없으면 
                return None         # 검색 실패
            
            if key == p.key :       # key와 노드 p의 키가 같으면 
                return key.value    # 검색 성공
            
            elif key < p.key :      # key쪽이 작으면
                p = p.left          # 왼쪽 서브 트리에서 검색
            
            else :                  # key 쪽이 크면
                p = p.right         # 오른쪽 서브 트리에서 검색
```



![Crocus](https://t1.daumcdn.net/cfile/tistory/255DB73A57F5EF4C15)

### 검색 성공

위의 사진에서 키 값이 `7`인 노드를 검색하여 성공하는 과정은 다음과 같다.

1. 처음에 주목하는 루트의 키는 8이다. 8은 7보다 크므로 왼쪽 자식 노드를 따라간다.
2. 다음에 주목하는 노드의 키는 3이다. 3은 7보다 작으므로 오른쪽 자식 노드를 따라간다.
3. 다음에 주목하는 노드의 키는 6이다. 6은 7보다 작으므로 오른쪽 자식 노드를 따라간다.
4. 키가 7인 노드에 도달했으므로 검색에 성공한다.

### 검색 실패

위의 사진에서 키 값이 `11`인 노드를 검색하여 실패하는 과정은 다음과 같다.

1. 처음에 주목하는 루트의 키는 8이다. 8은 11보다 작으므로 오른쪽 자식 노드를 따라간다.
2. 다음에 주목하는 노드의 키는 10이다. 10은 11보다 작으므로 오른쪽 자식 노드를 따라간다.
3. 다음에 주목하는 노드의 키는 14이다. 14는 11보다 크므로 왼쪽 자식 노드를 따라간다.
4. 다음에 주목하는 노드의 키는 13이다. 주목 노드는 리프이고 오른쪽 자식 노드는 존재하지 않는다. 더이상 스캔을 할 수 없으므로 검색에 실패한다.

### 노드를 삽입하는 add()함수

노드를 삽입한 뒤에 트리의 형태가 이진 검색 트리의 조건을 유지해야 한다. 
따라서 노드를 삽입할 때에는 검색할 때와 마찬가지로 먼저 삽입할 위치를 찾아낸 뒤에 수행해야 한다.

1. 루트에 주목한다. 여기서 주목하는 노드는 node
2. 삽입하는 key와 주목 node의 키를 비교한다.
   1. key == node : 삽입을 실패하고 종료한다.
   2. key < node 
      1. 왼쪽 자식 노드가 없으면 그 자리에 노드를 삽입하고 종료한다.
      2. 왼쪽 자식 노드가 있으면, 주목 노드를 왼쪽 자식 노드로 옮긴다
   3. key > node 
      1. 오른쪽 자식 노드가 없으면 그 자리에 노드를 삽입하고 종료한다.
      2. 오른쪽 자식 노드가 있으면, 주목 노드를 오른쪽 자식 노드로 옮긴다
3. 2번 과정으로 되돌아간다.

```python
def add(self, key: Any, value: Any) -> Any:
        '''키가 key이고 값이 value인 노드를 삽입'''
        def add_node(node: Node, key: Any, value: Any) -> Any:
            '''node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입'''
            if key == node.key:
                return False        # key가 이진 검색 트리에 이미 존재
            
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
```

![Crocus](https://t1.daumcdn.net/cfile/tistory/255DB73A57F5EF4C15)

### 삽입 성공

위의 사진에서 키 값이 `15`인 노드를 삽입하여 성공하는 과정은 다음과 같다.

1. 삽입할 위치를 찾는다. 추가할 값 15는 14 보다 크고 오른쪽 자식 노드가 존재하지 않으므로 삽입할 위치로 14를 선택한다.
2. 15를 오른쪽 자식 노드로 삽입한다.

### 노드를 삭제하는 remove()함수

노드를 삭제할때는 다음 3가지 경우가 존재한다.

1. 자식 노드가 없는 노드를 삭제하는 경우
2. 자식 노드가 1개인 노드를 삭제하는 경우
3. 자식 노드가 2개인 노드를 삭제하는 경우

### 자식 노드가 없는 노드를 삭제하는 경우

- 삭제할 노드가 부모 노드의 왼쪽 자식인 경우 :  부모의 왼쪽 포인터를 None으로 한다.
- 삭제할 노드가 부모 노드의 오른쪽 자식인 경우 :  부모의 오른쪽 포인터를 None으로 한다.

### 자식 노드가 1개인 노드를 삭제하는 경우

- 삭제할 노드가 부모 노드의 왼쪽 자식인 경우 : 부모의 왼쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트 한다.
- 삭제할 노드가 부모 노드의 오른쪽 자식인 경우 : 부모의 오른쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트 한다.

### 자식 노드가 2개인 노드를 삭제하는 경우

- 삭제할 노드의 왼쪽 서브트리에서 키 값이 가장 큰 노드를 검색한다.
- 검색한 노드를 삭제 위치로 옮긴다. 즉, 검색한 노드의 데이터를 삭제할 노드 위치에 복사한다.
- 옮긴 노드를 삭제한다. 이때 자식 노드의 개수에 따라 다음을 수행한다.
  - 옮긴 노드에 자식이 없으면 : `자식 노드가 없는 노드의 삭제`에 따라 노드를 삭제한다.
  - 옮긴 노드에 자식이 있으면 : `자식 노드가 1개인 노드의 삭제`에 따라 노드를 삭제한다. 

```python
def remove(self, key: Any) -> bool:
        '''키가 key인 노드를 삭제'''
        p             = self.root               # 스캔중인 노드
        parent        = None                    # 스캔 중인 노드의 부모 노드
        is_left_child = True                    # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:                       # 더이상 진행할 수 없으면 
                return False                    # 그 키는 존재하지 않음
            
            if key == p.key:                    # key와 자식 노드 p의 키가 같으면
                break                           # 검색 성공
                
            else:
                parent = p                      # 가지를 내려가기 전에 부모를 설정
                
                if key < p.key:                 # key쪽이 작으면
                    is_left_child = True        # 여기서 내려가는 것은 왼쪽 자식
                    p             = p.left      # 왼쪽 서브트리에서 검색
                
                else:                           # key쪽이 크면
                    is_left_child = False       # 여기서 내려가는 것은 오른쪽 자식
                    p             = p.right     # 오른쪽 서브 트리에서 검색

        if p.left is None:                      # p 왼쪽에 자식이 없으면
            '''자식 노드가 없는 노드를 삭제하는 경우와
							 자식 노드가 1개인 노드를 삭제하는 경우'''
            if p is self.root:
                self.root = p.right
            
            elif is_left_child:
                parent.left = p.right           # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            
            else:
                parent.right = p.right          # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        
        elif p.right is None:                   # p에 오른쪽 자식이 없으면
            if p is self.root: 
                self.root = p.left
            
            elif is_left_child:
                parent.left = p.left            # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            
            else:
                parent.right = p.left           # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴

        else:
          '''자식 노드가 2개인 노드를 삭제하는 경우'''
            parent        = p
            left          = p.left              # 서브트리 안에서 가장 큰 노드
            is_left_child = True 

            while left.right is not None:       # 가장 큰 노드 left를 검색
                parent        = left
                left          = left.right
                is_left_child = False

            p.key   = left.key                  # left의 키를 p로 이동
            p.value = left.value                # left의 데이터를 p로 이동
            
            if is_left_child:
                parent.left = left.left         # left를 삭제
            
            else: 
                parent.right = left.left        # left를 삭제

        return True

```

