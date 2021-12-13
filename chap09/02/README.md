# 이진 트리

![img](https://miro.medium.com/max/1400/1*abunFFnReygaqVt93xNr2A.png)



노드가 `왼쪽 자식`과 `오른쪽 자식`만을 갖는 트리를 이진트리라고 한다.
이때 두 자식 가운데 하나 또는 둘 다 존재하지 않는 노드가 있어도 상관 없다.

### 이진 트리의 특징

- 왼쪽 자식과 오른쪽 자식을 구분한다.
- 노드는 최대 두개의 하위 노드(자식)을 가질 수 있다.
- 왼쪽 자식 노드는 부모 노드보다 값이 적어야 한다.
- 오른쪽 자식 노드는 부모 노드보다 값이 커야한다.

### 이진 트리의 시간 복잡도

이진트리는 일반적으로 빠른 검색을 위해서 사용된다. 
정렬이 된 array가 `O(N)`인 반면 이진 트리는 `O(log n)`이다.



## 완전 이진 트리

![Sideways traversal of a Complete Binary Tree - GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20200218123136/Side-Ways-Traversal-Input.png)

출처 : https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fsideways-traversal-of-a-complete-binary-tree%2F&psig=AOvVaw2N98jwXHjMMX1KOQfXp-f1&ust=1639311918888000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCKDrgfze2_QCFQAAAAAdAAAAABAM

루트부터 아래쪽 레벨로 노드가 가득 차 있고, 같은 레벨 안에서 왼쪽부터 오른쪽으로 노드가 채워져 있는 이진 트리를 완전 이진 트리(complete binary tree)라고 한다.

높이가 k인 완전 이진 트리가 가질 수 있는 노드의 수는 최대 `2^k+1 - 1`개 이므로 n개의 노드를 저장할 수 있는 완전 이진 트리의 높이는 `log n`이다.

### 완전 이진 트리의 노드를 채우는 법

- 마지막 레벨을 제외하고 모든 레벨에 노드가 가득 차 있다.
- 마지막 레벨에 한해서 왼쪽부터 오른쪽으로 노드를 채우되, 반드시 끝까지 채우지 않아도 된다.

## 균형 검색 트리



![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7c3461a0-00b0-43a2-8437-630fdcc4bdfd%2FTime-Complexity-of-Binary-Search-Tree-Worst-Case.png?table=block&id=09e18f9b-4ecc-4ed9-84ec-235435412870&spaceId=4b97eaca-7938-4c43-b27c-a0c55795a841&width=800&userId=9d75a55a-6e05-4e9f-8a9f-16cf4817ef81&cache=v2)

이진 검색트리는 위 사진 처럼키의 오름차순으로 노드가 삽입되면 트리의 높이가 깊어지는 단점이 있다.(데이터가 이미 정렬되어 있는 경우)
이럴 경우 선형 리스트 처럼 되어 빠른 검색을 할 수 없어 시간 복잡도가 `O(n)`이 나올 수 있다. 

이를 방지하고자 높이를 `O(log n)`으로 제한하여 고안된 검색 트리를 균형 검색 트리라고 하고 다음과 같은 종류가 있다.

- AVL 트리(AVL tree)
- 레드 - 블랙 트리 (red-black tree) 

### 레드 - 블랙 트리(RBtree)

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc3abb5ed-074c-4fce-963a-57d0b280cc12%2FRed-black_tree_example.svg.png?table=block&id=6dbf83a4-bde9-4e04-8526-213a200b9824&spaceId=4b97eaca-7938-4c43-b27c-a0c55795a841&userId=9d75a55a-6e05-4e9f-8a9f-16cf4817ef81&cache=v2)

레드 - 블랙 트리는 항상 다음 규칙을 준수해야 한다.

1. 모든 노드는 `레드` 이거나 `블랙` 이어야 한다.
2. 루트 노드는 항상 `블랙`이어야 한다.
3. 리프 노드도 항상 `블랙`이어야 한다.
4. `레드` 노드는 연달아 나올 수 없다.
   1. `레드` 노드의 부모는 항상 `블랙` 노드여야하고, 자식 노드들도 `블랙` 노드여야 한다.
      1. `블랙` 노드의 자식은 `블랙`일 수 있다.
5. 루트 노드와 모든 리프 노드 사이에 존재하는 `블랙` 노드의 수는 모두 동일하다.

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
def add(self, key: Any, value: Any) -> bool:
        '''키가 key이고 값이 value인 노드를 삽입'''
        def add_node(node: Node, key: Any, value: Any) -> None:
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

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True

        else:
            return add_node(self.root, key, value)
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

