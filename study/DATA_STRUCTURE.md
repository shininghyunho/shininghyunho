## 참고

[Interview_Question_for_Beginner](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/DataStructure#personal-recommendation)

# Data Structure

## Array List, Linked List

### Array List

인덱스 단위로 접근. 논리적인 저장 순서와 물리적인 저장 순서가 동일.

 접근 자체는 빅오가 1인데 삽입 삭제는 빅오가 n (재정렬이 필요해서).

#### Array vs Array List

|                       Array                        |      Array List       |
| :------------------------------------------------: | :-------------------: |
|                     크기 고정                      |       크기 동적       |
| primitive type(int,byte,char), object 담을 수 있음 | object만 담을 수 있음 |
|                   제네릭 사용 x                    |     제네릭 사용 o     |
|                 배열 길이 : length                 |  배열 길이 : size()   |
|             element 할당 : assignment              | element 추가 : add()  |



### Linked List

레퍼런스(주소)를 통하여 연결. 한 노드가 다음 노드의 주소를 가지고있음.

삽입 삭제 후 가리키는 주소만 바꿔주면 되서 빅오가 1, 접근은 헤드부터 하나씩 접근해야해서 빅오 n. 마지막 노드(tail)도 저장할 수 있음.



### Question

- Array 기반으로 Linked List 구현 (구현해봐야함)

- ArrayList 기반으로 Linked List 구현 (구현해봐야함)



## Stack, Queue

### Stack

Last In First Out(LIFO), 나중에 삽입한것이 먼저 나옴. DFS 알고리즘에서 사용.

### Queue

First In First Out (FIFO). 먼저 삽인한것이 먼저 나옴. BFS 알고리즘에서 사용. 힙을 이용해 우선순위를 가지는 큐를 구현할 수 있음.

### Question

- Stack을 이용하여 미로찾기 구현 -> DFS
- Queue를 이용하여 Heap 자료구조 구현
- Stack 두 개로 Queue 구현 -> Pop할때 다른쪽 Queue 사용 구현
- Stack으로 괄호 유효성 체크 구현



## Tree

DAG(Directed Acyclic Graph) 중 하나. 노드와 간선으로 이루어져 있음. 계층 구조를 표현하는데 적합한 자료구조.

### Binary Tree

자식이 2개 이하로 이루어진 트리. 자식들도 이진트리여야함.

### Binary Search Tree

본인 노드의 값을 중심으로, 노드 삽입시 본인보다 크면 오른쪽 작으면 왼쪽 노드로 넣어줌.(방향 상관 x) 일반적으로 빅오는 log n. 최악의 경우(모두 자식이 하나일때, 일자로 정렬) 빅오가 n이 됨.(이를 해결하는 것이 Rebalancing ex) Red-Black Tree ). 삽입할때는 루트 노드부터 비교하며 내려가고, 삭제할때는 왼쪽에서 가장 오른쪽(작은 자식들중에 가장 큰 값) 또는 오른쪽에서 가장 왼쪽(큰 자식들 중에 가장 작은 값)과 교체.

### Question

- BST 구현 -> 삽입 삭제 조회 고려
- 트리가 BST인지 확인하는 방법

### Red Black Tree

Red, Black으로만 이루어진 BST. Balance 되어 있어 모든 리프 노드까지의 Black 노드 접근 수가 같다. (최소와 최대가 2배 이하). 그리고 아래 4개의 Rule을 지켜야한다.

비슷한 알고리즘으로는 AVL이 있다. AVL이 더욱 엄격한 균형을 이루고 있어 더 빠른 조회가 가능하다. 대신 RBT는 회전이 거의 이루어지지 않아 AVL보다 빠르게 삽입 제거가 가능하다. 이러한 특성때문에 RBT는 맵, c++의 멀티캐스트, Java treeMap 등 대부분의 언어 라이브러리에서 사용되고 AVL은 더 빠른 검색을 요구하는 데이터베이스에서 사용된다.

#### Rule

1. Root Property : 루트노드는 Black
2. External Property : 모든 External Node는 Black(리프 노드는 빈 노드로 따로 설정)
3. Internal Property : Red 노드의 자식은 무조건 Black. (No Double Red)
4. Depth Property : 모든 리프노드에서 Black Depth는 같다.

기본적으로 BST다 보니 삽입 삭제 모두 BST처럼 하면 된다. 대신 그럴때마다 Rule을 어길 수가 있다. 그러면 그때 조취를 취해준다. 

삽입은 Red 노드로 해준다. 

이때 Double Red가 생길 수 있다. 그러면 2가지 방법 중 하나로 해결한다.

부모의 형제(uncle) 노드가 Black일 경우 -> Restructuring

부모의 형제 노드가 Red일 경우 -> Recoloring

[참고](https://zeddios.tistory.com/237)

[위키피디아](https://ko.wikipedia.org/wiki/%EB%A0%88%EB%93%9C-%EB%B8%94%EB%9E%99_%ED%8A%B8%EB%A6%AC)

[시뮬레이터](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

### Question

- RBT 구현해보기 -> [python](./RedBlackTree.py)

- AVL의 동작 이해와 차이점
