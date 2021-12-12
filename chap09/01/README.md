# 트리 구조

## 1. 트리 구조 용어
![](https://images.velog.io/images/maxkmh/post/e8b43ee8-4cf2-4f44-94fc-e69c24bc5746/%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9_2.png)

> 〇 : 노드(node)  
 ⎮ : 가지(edge)

- 루트(root)
  - 트리의 가장 위쪽에 있는 노드
  - 루트는 트리에 하나만 존재
  - ex) 위 그림에서 A

- 리프(leaf)
  - 가장 아래쪽에 있는 노드
  - = 단말노드(terminal node), 외부노드(external node)
  - 단순히 물리적으로 가장 밑에 위치한다는 의미가 아니라 가지가 더 이상 뻗어나갈 수 없는 마지막에 위치한 노드
  - ex) 위 그림에서는총 7개 : K, L, F, G, M, I, J


- 비단말노드(non-terminal node)
  - 리프를 제외한 노드
  - = 내부노드(internal node)
  - ex) 위 그림에서 총 6개 : A, B, C, D, E, H

- 자식(child) 
  - 노드와 가지가 연결되었을 때 아래쪽 노드
  - ex) 위 그림에서 A의 자식은 3개, B의 자식은 2개

- 부모(parent)
  - 노드와 가지가 연결되었을 때 가장 위쪽 노드
  - 루트는 부모를 갖지 않음
  - ex) 위 그림에서 B의 부모는 A
  
- 형제(sibling) : 부모가 같은 노드
  - ex) 위 그림에서 H의 형제노드는 I, J

- 조상(ancestor) 
  - 노드에서 위쪽으로 가지를 따라감면서 만나는 모든 노드
  - ex) 위 그림에서 K의 조상 : E, B, A

- 자손(descendant)
  - 노드에서 아래쪽으로 가지를 따라가면서  만나는 모든 노드
  - ex) 위 그림에서 B의 자손 : E, F, K, L

- 레벨(level)
  - 루트에서 떨어져 있는 단계
  - 루트의 레벨은 0
  - 가지가 하나씩 아래로 뻗어 내려갈 때마다 레벨 1씩 증가

- 차수(degree)
  - 각 노드가 갖는 자식의 수
  - n진 트리 : 모든 노드의 차수가 n 이하인 트리

- 높이(height)
  - 루트에서 가장 멀리 있는 리프까지의 거리
  - 리프 레벨의 최댓값


- 서브트리
  - 어떤 노드를 루트로 하고, 그 자손으로 구성된 트리

- 빈 트리()
  - = 널 트리(null tree)
  - 노드와 가지가 전혀 없는 트리

## 2. 순서 트리 & 무순서 트리
### 개념
![](https://images.velog.io/images/maxkmh/post/c21b9f03-f6d4-46a3-ba1b-dd7c7a5a21c6/image.png)
- 순서트리 : 형제 노드의 순서 관계가 있는 트리
- 무순서트리 : 형제 노드의 순서 관계가 없는 트리

### 순서 트리의 검색

1) 너비 우선 검색(breadth-first-search, BFS)  
![](https://images.velog.io/images/maxkmh/post/6495a84a-ec2c-4bbe-bb21-ed89b21fbbab/image.png)  
- 폭 우선 검색, 가로 검색, 수평 검색
- 낮은 레벨부터 왼쪽에서 오른쪽으로 검색 후 다음 레벨로 가는 방법

2) 깊이 우선 검색 (depth-first-search, DFS)  
![](https://images.velog.io/images/maxkmh/post/8c9b4e22-95f6-4526-8c9a-fc93ed5f2fc7/image.png)
- 세로 검색, 수직 검색


## 3.트리 순회 방법 3가지
![](https://images.velog.io/images/maxkmh/post/8bfb5774-9b6b-49ee-8cf8-0db469b56304/image.png)

1) **Inorder (중위 순회)**
- 루트 노드를 시작으로 왼쪽이 먼저 오고 다음은 호출한 노드 그리고 그 노드의 오른쪽이 오는 것
- `Left -> Root -> Right`
- ex) 위 그림에서 : 4, 2, 5, 1, 3

2) **Preorder (전위 순회)**
- 루트 자기 자신 먼저
- `Root -> Left -> Right`
- ex) 위 그림에서 : 1, 2, 4, 5, 3

3) **Postorder (후위 순회)**
- 루트 자기 자신이 나중에
- `Left -> Right -> Root`
- ex) 위 그림에서 : 4, 5, 2, 3, 1

