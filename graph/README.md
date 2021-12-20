# 그래프(graph) 자료구조
노드, 노드와 노드를 연결하는 간선을 하나로 모아놓은 자료구조<br>
서로 다른 개체 혹은 객체의 관계나 경로를 표시하고자 할 때 사용

## 트리와의 비교
트리는 그래프 자료구조의 한 종류이며 그래프는 노드와 노드사이의 간선이 있을 수도 없을 수도 있지만 트리에서는 반드시 간선이 존재한다.
또한 다음과 같은 특징이 있다.<br>
||그래프|트리|
|---|---|---|
|방향성|방향 그래프 혹은 무방향 그래프|방향 그래프|
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|루트 노드가 없음|루트 노드가 존재|
|노드간 관계성|부모 자식 관계 없음|부모 자식 관계 존재|
|모델의 종류|네트워크 모델|계층형 모델|

** 네트워크 모델 : 오브젝트와 이에 대한 관계를 나타내는 유연한 방식으로 이해할 수 있는 데이터베이스 모델<br>
** 계층형 모델 : 반복적인 부모-자식 관계의 정보를 표현하며 부모는 여러 자식을 가질 수 있고, 자식은 단 하나의 부모만 가질 수 있다.

## 그래프 관련 용어
- 정점(vertex) : 데이터가 저장되는 위치를 의미 (= 노드)
- 간선(edge) : 정점과 정점을 연결하는 선이며 노드간의 관계를 나타낸다.
- 인접 정점(adjacent vertex) : 간선에 의해 연결된 정점 (= 인접 노드)
- 정점의 차수(degree) : 하나의 정점에 인접한 정점의 수
- 진입 차수(in-degree) : 방향그래프에서 한 노드에서 외부로 향하는 간선의 수
- 진출 차수(out-degree) : 방향그래프에서 외부에서 들어오는 간선의 수
- 경로 길이(path length) : 경로를 구성하는 데 사용된 간선의 수
- 단순 경로(simple path) : 반복되는 정점이 없는 경로, 같은 간선을 지나지 않는 경로
- 사이클(cycle) : 단순 경로의 시작과 종료 정점이 같은 경우

## 그래프의 종류
### 1. 무방향 그래프, 방향 그래프
<img src="https://www.researchgate.net/profile/Valeria-Fionda/publication/50591619/figure/fig3/AS:667872535773189@1536244629217/a-An-example-of-undirected-graph-and-b-an-example-of-directed-graph.png"><br>
- 무방향 그래프(Undirected Graph)
    - 말 그대로 방향이 없는 간선으로 표현되는 그래프
    - 정점 A, 정점 B를 연결하는 간선은 (A,B)와 같은 형태로 표시된다. (A,B) = (B,A)
- 방향 그래프(Directed Graph)
    - 간선에 방향성이 존재하는 그래프
    - <A,B>형태로 표시하며 이는 A -> B로의 단방향 경로를 의미한다. <A,B> != <B,A>

### 2. 가중치 그래프
<img src="https://i.stack.imgur.com/Mu6VZ.png" width=300><br>
- 가중치 그래프(Weighted Graph)
    - 간선에 비용이나 가중치가 할당된 그래프
    - 네트워크 라고도 한다.

### 3. 연결 그래프, 비연결 그래프
<img src="https://mathworld.wolfram.com/images/eps-gif/ConnectedGraph_1000.gif"><br>
- 연결 그래프(Connected Graph)
    - 무방향 그래프에 있는 모든 정점쌍에 대해서 항상 경로가 존재하는 경우
    - ex) 트리(Tree) : 사이클을 가지지 않는 연결 그래프
- 비연결 그래프(Disconnected Graph)
    - 무방향 그래프에서 특정 정점쌍 사이에 경로가 존재하지 않는 경우

### 4. 완전 그래프
<img src="https://lh5.googleusercontent.com/proxy/pnGdV5vK7wrA3_zpITeoF7r_Y-bRaX9lxGZhNB3aqKE8vbk3eTIuK8Fg1NMu2HF38QNtR6qEmGrWLmLoto8hxf94_pTDuPPBqd0s_I77nbShNM3QNaQ=s0-d"><br>
- 완전 그래프(Complete Graph)
    - 그래프에 속해 있는 모든 정점이 서로 연결되어 있는 그래프

## 그래프의 구현
<img src="https://blog.kakaocdn.net/dn/bg8xDb/btrfIZli044/vONMxjv185henGSPfnaNn1/img.png" width="300" height="300">

<br>

||0|1|2|
|---|---|---|---|
|0|0|7|5|
|1|7|0|INF|
|2|5|INF|0|

### 1. 인접 리스트(Adjacency List)
- 모든 정점에 인접한 정점들을 리스트로 표시하는 방법
```python3
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))
```

### 2. 인접 행렬(Adjacency Matrix)
```python3
INF = 999999999

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
```

## 그래프의 탐색
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4JP62%2FbtrfG1X0DHL%2FVchkNMVrHO30RKD4cu52M0%2Fimg.png" width=500, height=300><br>

### 1. DFS(깊이 우선 탐색)
스택 자료구조를 활용하며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘. 재귀함수를 이용해서 구현할 수 있다.<br><br>

```python3
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)
```
### 2. BFS(너비 우선 탐색)
너비우선탐색이라고 불리며 가까운 노드부터 탐색하는 알고리즘. 큐를 통해 구현한다.
```python3
from collections import deque

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                que.append(i)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
que = deque([])
visited = [False] * 9
bfs(graph, 1, visited)
```