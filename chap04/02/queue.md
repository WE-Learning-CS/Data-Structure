# Queue | 큐

![](https://blog.kakaocdn.net/dn/Kri2r/btq2u3BF2GD/NXMEc74ZDvXAUA8TfKNNHK/img.png)

큐는 스택과 같이 데이터를 임시 저장하는 자료구조이다. 
스택과는 반대로 `FIFO(First In First Out)`이다. 즉, 먼저 push 된게 먼저 pop 된다.

- **인큐 (enqueue)** : 큐에 데이터를 추가하는 작업
- **디큐 (dequeue)** : 큐에서 데이터를 꺼내는 작업

- **프런트 (front)** : 데이터를 꺼내는 쪽
- **리어 (rear)** : 데이터를 집어넣는 쪽, back이라고도 함

## 장 / 단점

- **장점**
  - 삽입, 삭제가 빠르다
- **단점**
  - 탐색이 비효율 적이다. 다 꺼내보면서 탐색해야 하기 때문.
  - 정책에 따라 가장 위쪽의 원소만 접근이 가능하다.

## 큐를 사용하면 좋은 경우

- 맛집 예약 시스템
- OS 프로세스 스케쥴링 시스템 (Priority Queue)
- 최근에 방문한 사이트 주소 기록 (Dequeue)
- 문서 작성 툴에서 undo 기록 (Dequeue)



-----

## 배열로 큐 구현하기

- enqueue : 데이터를 추가하는 과정
- dequeue : 데이터를 꺼내는 과정
- peek : front에 있는 값을 꺼내지 않고 어떤 값인지만 return

```python
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued   = self.queue[0]
            del self.queue[0]
            
            return dequeued

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
            
        return self.queue[0]
```

### 시간 복잡도

- enqueue : O(1)
- dequeue : O(n)

-----

## 우선순위 큐

인큐 시 데이터에 우선순위를 부여하여 추가하고, 디큐 시 우선순위가 가장 높은 데이터를 꺼내는 방식.

- enqueue : 데이터를 추가하는 과정
- dequeue : 데이터를 꺼내는 과정

```python
# path : chap04/priority_queue.py

from collections import namedtuple

class PriorityQueue:
    Element = namedtuple("element", ["priority", "data"])

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False
    
    def enqueue(self, priority, data):
        return self.queue.append(PriorityQueue.Element(priority, data))

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        data = self.queue[0]
        idx  = 0

        for i in range(1, len(self.queue)):
            if data.priority < self.queue[i].priority:
                data = self.queue[i]
                idx  = i
        
        del self.queue[idx]
        
        return data


```

>**우선순위 큐**
>파이썬에서 우선순위를 부여하는 큐는 heapq 모듈에서 제공한다.
>
>heap에서 data의 인큐는 heapq.heqppush(heap,data) 로 수행하고, 디큐는 heapq.heapop(heap)으로 수행한다.
>
>참고 : https://docs.python.org/ko/3/library/heapq.html

-----

## 링 버퍼로 큐 구현하기

링버퍼 : 배열 맨 끝의 원소 뒤에 맨 앞의 원소가 연결되는 자료 구조

- front : 배열의 맨 앞 원소
- rear : 배열의 맨 끝 원소 

![](https://file.namu.moe/file/eabb47092a1eafff8794941f31821d22a094452bef6646a87c90d039990ffb49)

출처 : https://namu.moe/w/%ED%81%90(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)

기존의 큐는 공간이  꽉 차게 되면 더이상 요소를 추가할 수 없다. 앞쪽에 공간이 남아있다면 동그랗게 연결해 앞쪽으로 추가할 수 있도록 재활용 가능한 큐가 링 버퍼큐(원형 큐)이다.

```python
# path : chap04/fixed_queue.py

from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no       = 0                   # 현재 데이터 개수
        self.front    = 0                   # 맨 앞 원소 커서
        self.rear     = 0                   # 맨 끝 원소 커서
        self.capacity = capacity            # 큐의 크기
        self.que      = [None] * capacity   # 큐의 본체

    def __len__(self) -> int:
        '''큐에 있는 모든 데이터 개수를 반환'''
        return self.no
    
    def isEmpty(self) -> bool:
        '''큐가 비어있는지 판단'''
        return self.no <= 0

    def isFull(self) -> bool:
        '''큐가 가득 차 있는지 판단'''
        return self.no >= self.capacity

    def enqueue(self, x: Any) -> None:
        '''데이터 x를 인큐'''
        if self.isFull():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear += 1
        self.no   += 1

        if self.rear == self.capacity: # 큐가 가득 찰 경우
            self.rear = 0
    
    def dequeue(self) -> Any:
        '''데이터를 디큐'''
        if  self.isEmpty():
            raise FixedQueue.Empty

        x = self.que[self.front]

        self.front +=1
        self.no    -=1

        if self.front == self.capacity: # 큐 배열의 한계를 넘어설경우
            self.front = 0              # front값을 배열 맨 앞 인덱스인 0으로 되돌림

        return x
    
    def peek(self) -> Any:
        '''큐의 맨 앞 데이터를 확인'''
        if  self.isEmpty():
            raise FixedQueue.Empty

        return self.que(self.front)

    def find(self, value: Any) -> Any:
        '''큐에서 value를 찾아 인덱스 반환 (없으면 -1)'''
        for i in range(self.no):
            idx = (i + self.front) % self.capacity

            if self.que[idx] == value:
                return idx

        return -1

    def count(self, value: Any) -> Any:
        '''큐에 있는 value의 개수를 반환'''
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> Any:
        '''큐에 value가 있는지 판단'''
        return self.count(value)

    def clear(self) -> None:
        '''큐 초기화'''
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        '''모든 데이터를 맨 앞부터 맨 끝 순으로 출력'''
        if self.isEmpty():
            print("Queue is Empty")
        
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
                print()
```

- que : 큐의 배열로서 밀어 넣는 데이터를 저장하는 list형 배열
- capacity : 큐의 최대 크기를 나타내는 int 형 정수. 배열 queue 원소 수와 일치한다.
- front, rear : 맨 앞 원소, 맨끝 원소. 
- no : 큐에 쌓여있는 데이터 개수를 나타내는 int형 정수. 변수 front와 rear값이 같을 경우 큐가 비어있는지, 가득 차 있는지 구별하기 위해 필요하다. 큐가 비어있다면 no 는 0이고, 가득 차있다면 no는 capacity 값과 같다.