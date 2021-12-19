# 힙(Heap)

- 이진 트리(binary tree)의 한 종류이며 이진 힙(binary 힙)이라고도 부른다.
- 데이터 원소들의 순서를 교묘하게 표현한 트리이다.
- 데이터의 정렬에도 이용할 수 있으며 데이터를 정렬하는 알고리즘을 힙 정렬(heap sort)라고도 부른다.

## Max heap & Min heap

![이진트리 노드탐색, 파이썬 Heapq 모듈](https://media.vlpt.us/images/godiva7319/post/81b6ff9c-f9c9-4076-80b7-e9c598a36776/img.png)

출처 : https://kakunblog.tistory.com/11

힙에는 최대 힙(max heap)과, 최소 힙(min heap)이 있다. 원소의 순서 기준이 내림차순이냐, 오름차순이냐에 따라 달라지고 완전히 대칭이다. 

### Max heap

- 루트 노드가 항상 최댓값을 가진다.

- 완전 이진 트리이다. 때문에 노드의 추가와 삭제는 배열의 맨 마지막 원소에서만 일어난다.

- 최대 힙 내의 임의의 노드를 루트로 하는 서브 트리또한 최대 힙이다.

  

### 장점

- 완전 이진 트리(complete binary tree)제약 때문에, n개의 노드로 이루어진 최대 힙의 높이(깊이)는 `log(n) + 1`로 정해진다.
- 이 성질으로 데이터 원소의 삽입/삭제 연산의 실행 시간은 언제나 `log(n)` 에 비례한다.
- 어떤 최대 힙이 존재할 때, 이 힙으로부터 반복적으로 루트 노드를 삭제하면서 데이터 원소들을 꺼내면 루트 노드에 들어있는 키가 힙 내에서 최대임이 보장되어 있으므로 데이터를 내림차순으로 정렬할 수 있고, 이 정렬에 소요되는 시간 또한 `log(n)`이다.

### 단점

- 이진 탐색 트리(binary search tree)에서는 원소들이 완전히 크기 순서대로 정렬되어 있었으나, 최대 힙은 완전 크기 순서대로 정렬되어 있지는 않다.
- 이진 탐색 트리는 루트 노드로부터 시작하여 특정 원소를 빠르게 검색할 수 있으나, 최대 힙은 탐색 연산을 제공 할 수 없다.

## 최대 힙에 원소 삽입

1. 트리의 마지막 자리에 새로운 원소를 임시로 저장한다.
2. 부모 노드와 키 값을 비교하여 크다면 위로 이동시킨다.

```python
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data) -1 # 마지막 인덱스
        
        while index != 1:
            parentNode = index // 2
            
            '''
            마지막 인덱스의 값이 부모 노드보다 크다면 위치를 바꾸어준다.
            인덱스에 부모 노드의 값을 넣어 인덱스가 1이 아닐때까지 반복한다.
            '''
            if self.data[parentNode] < self.data[index]:
                self.data[parentNode], self.data[index] = self.data[index], self.data[parentNode]
                index = parentNode
            
            else:
                break
```

## 최대 힙에서 원소의 삭제

- 원소 삭제는 항상 루트 노드에서 이루어진다. (최댓값을 순서대로 뽑아내야 하므로)
- 루트 노드를 삭제하고 나면 트리의 구조를 다시 정리해야 한다.
- 노드의 삭제 또한 맨 마지막 노드에서 일어난다.

1. 루트 노드의 데이터를 꺼낸다(원소들 중 최댓값)
2. 맨 마지막 노드의 원소를 루트 노드의 자리에 임시로 집어넣는다.
3. 마지막 노드를 제거한 다음에 루트 자리에 임시로 들어간 노드의 올바른 자리를 찾아준다.

```python
    def remove(self):
    		# 힙이 비어있지 않을때
        if len(self.data) > 1: 
        		# 루트노드와 마지막 노드의 위치를 바꾸어 준다
            self.data[1], self.data[-1] = self.data[-1], self.data[1] 
            # 마지막 노드를 지워준다
            data = self.data.pop(-1) 

        else:
            data = None

        return data
```

```python
def maxHeapify(self, i):
  			# 왼쪽 자식의 인덱스 계산
        left  = i * 2
      	# 오른쪽 자식의 인덱스 계산
        right = i * 2 + 1
        # 작은 값의 인덱스를 가지는 값으로 초기화
        smallest = i
        
        # 왼쪽 자식이 존재하면 왼쪽 자식의 키 값이 무엇보다 더 큰지를 판단
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            # 조건이 만족한다면 smallest는 왼쪽 자식의 인덱스로 교체된다.
            smallest = left
        # 오른쪽 자식이 존재하면 오른쪽 자식의 키 값이 무엇보다 더 큰지를 판단
        if right < len(self.data) and self.data[right] > self.data[smallest]:
          	# 조건이 만족한다면 smallest는 오른쪽 자식의 인덱스로 교체된다.
            smallest = right
        

        if smallest != i:
            # 현재 노드와 최댓값 노드(왼쪽 혹은 오른쪽 자식)를 교체한다
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
           	# 재귀적 호출을 통해 최대 힙의 성지를 만족할때까지 트리를 정렬한다.
            self.maxHeapify(smallest)
```



## 최대 / 최소 힙의 응용

- 우선 순위 큐(priority queue)
  - Enqueue 할 때 `느슨한 정렬`을 이루고 있도록 함 O(log n)
  - Dequeue 할 때 최댓값을 순서대로 추출 O(long n)

- 힙 정렬(heap sort)
  - 정렬되지 않은 원소들을 아무 순서로나 최대 힙에 삽입 O(log n)
  - 삽입이 끝나면, 힙이 비게 될 때 까지 하나씩 삭제 O(log n)
  - 원소들이 삭제된 순서가 원소들의 정렬 순서
  - 정렬 알고리즘의 복잡도 O(log n)

``` python
def heapSort(unsorted):
        H = MaxHeap()
        for item in unsorted:
            H.insert(item)

        sorted = []
        
        # 정렬되지 않은 값들이 정렬된다.
        d = H.remove()

        while d:
            sorted.append(d)
            d = H.remove()

        return sorted
```

