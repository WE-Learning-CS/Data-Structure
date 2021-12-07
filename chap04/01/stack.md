# stack
## 스택


스택이란?
스택(stack)은 '마른 풀을 쌓은 더미', '겹겹이 쌓음'을 뜻함

빠르다? 왜?
크기를 미리 지정해서 메모리에 고정된 할당 값을 가지고 연산처리를 하기 때문이다.

데이터를 임시 저장할 때 사용하는 자료구조로, 데이터의 입력과 출력 순서는 후입선출(LIFO)방식 혹은 FILO : First In Last Out


> LIFO(last in first out)란 가장 나중에 넣은 데이터를 가정 먼저 꺼낸다는 뜻

![image](https://user-images.githubusercontent.com/78721108/144973917-a5546b25-2f8a-4371-95ea-58a6ffa51957.png)

python에는 stack 모듈이 있다.!

![image](https://user-images.githubusercontent.com/78721108/144974027-4ba00f41-9bf9-453a-8df0-db1925ccf3c5.png)

<b>그런데 이미 파이썬에는 stack을 쓰지 않아도 구현이 되어있다?!</b>

바로 list []

append()
pop()
len()

![image](https://user-images.githubusercontent.com/78721108/144974406-f946e72b-e896-4c21-afb6-863a13a841aa.png)

하지만 클래스로 stack을 만들어 볼 수도 있다.
알고리즘 문제를 풀기위해서는 클래스를 만들어서 사용하기에는 시간도 많이 걸리므로 그저 구조를 파악하기 위해서 만들어 보는것을 추천한다.

![image](https://user-images.githubusercontent.com/78721108/144974604-160b4875-be63-45fd-a991-8701324f26c8.png)


### 덱
![image](https://user-images.githubusercontent.com/78721108/144980675-ade72d46-7e86-4528-b8a9-cf026ac13447.png)
