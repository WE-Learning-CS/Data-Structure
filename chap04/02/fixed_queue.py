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


