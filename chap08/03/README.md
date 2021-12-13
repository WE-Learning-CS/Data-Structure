## 커서를 이용한 연결 리스트

- 포인터를 이용한 연결 리스트는 '노드를 삽입/삭제할 때 데이터를 이동하지 않고 처리'하는 특징이 있었습니다.
- 하지만 노드를 삽입/삭제할 때마다 내부에서 노드용 인스턴스를 생성하고 소멸합니다.
- 만약 데이터 수가 크게 바뀌지 않고 데이터 수의 최대값 예측이 가능하다면,
- 커서를 이용한 연결 리스트를 사용하여 효율적으로 운용할 수 있습니다.

-----

![image](https://user-images.githubusercontent.com/87896537/145716722-bf8b3f61-2c8c-4ea6-9ca7-885f71d06c4a.png)

*커서 : 다음 노드가 들어있는 요소의 인덱스 값

-----

![image](https://user-images.githubusercontent.com/87896537/145716773-283991c8-438b-4854-ae82-7e4b165af6a1.png)

-----

![image](https://user-images.githubusercontent.com/87896537/145716948-0e774725-151a-4546-a2fe-611485bc3075.png)

-----

## 프리 리스트

- 위 프로그램에서 삭제된 레코드 그룹을 관리할 때 사용하는 연결 리스트입니다.

-----

![image](https://user-images.githubusercontent.com/87896537/145719190-9518822e-a4c9-45ad-a3a5-11db76de531f.png)

-----

![image](https://user-images.githubusercontent.com/87896537/145719194-54791d4c-6285-4d7c-a20c-1957c217c60f.png)

-----

![image](https://user-images.githubusercontent.com/87896537/145719201-ceaebb48-4cd6-4cad-9397-af370ab8e5e5.png)