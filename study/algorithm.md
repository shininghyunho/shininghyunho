
# 자주 나오는 유형
- 그리디
- 구현
- DFS/BFS
- 정렬
- 이진 탐색
- 다이나믹 프로그래밍
- 최단 경로
- 그래프 이론

## 그리디
현재 상황에서 지금 당장 좋은 것만 고르는 방법

### 문제들
- 뒤집기(백준) [문제](https://www.acmicpc.net/problem/1439) [내풀이](https://blog.naver.com/chlgusgh3315/222188063564)
- 무지의 먹방(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/42891) [내풀이](https://blog.naver.com/chlgusgh3315/222188615364)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=33)

## 구현
아이디어를 코드로 바꾸는 유형
코딩 피지컬 요구
### 문제들
- 럭키 스트레이트(백준) [문제](https://www.acmicpc.net/problem/18406) [내풀이](https://blog.naver.com/chlgusgh3315/222189648218)
- 문자열 압축(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60057) [내풀이](https://blog.naver.com/chlgusgh3315/222191678176)
- 자물쇠와 열쇠(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60059) [내풀이](https://blog.naver.com/chlgusgh3315/222197290258)
- 뱀(삼성, 백준) [문제](https://www.acmicpc.net/problem/3190) [내풀이](https://blog.naver.com/chlgusgh3315/222197290258)
- 기둥과 보(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60061) [내풀이](https://blog.naver.com/chlgusgh3315/222199827681)
- 치킨 배달(삼성, 백준) [문제](https://www.acmicpc.net/problem/15686) [내풀이](https://blog.naver.com/chlgusgh3315/222199913689)
- 외벽 점검(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60062) [내풀이](https://blog.naver.com/chlgusgh3315/222200744104)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=102)

## DFS, BFS
완전 탐색하는 방법
> DFS(깊이 우선 탐색) - stack 사용, 자식 노드 먼저 탐색, 끝까지 갔다옴.
* 재귀 함수 형태로 호출
* 예시
```
def dfs(y,x,num):
    if num==3:
        if check():
            print("YES")
            exit()
        else:
            return

    for i in range(y,n):
        for j in range(n):
            if i<=y and j<=x:
                continue
            if data[i][j]=='X':
                data[i][j]='O'
                dfs(i,j,num+1)
                data[i][j]='X'

for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            data[i][j]='O'
            dfs(i, j, 1)
            data[i][j]='X'

```
> BFS(너비 우선 탐색) - queue 사용, 같은 레벨 먼저 탐색, 모든 경우 체크하며 감.
- python 구현시 deque 라이브러리 사용
- 예시
```
from collections import deque
queue=deque()
queue.append([0,0])
cnt=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]

def bfs(y,x,start):
    visited[y][x]=start
    queue.append([y,x])
    while queue:
        qy,qx=queue.popleft()
        for i in range(4):
            my=qy+dy[i]
            mx=qx+dx[i]
            if my<0 or my>=n or mx<0 or mx>=m:
                continue
            if data[my][mx]==1 and visited[my][mx]==0:
                visited[my][mx]=visited[qy][qx]+1
                queue.append([my,mx])
            if my==n-1 and mx==m-1:
                return
bfs(0,0,1)

```
### 문제들
- 특정 거리의 도시 찾기(백준) [문제](https://www.acmicpc.net/problem/18352) [내풀이](https://blog.naver.com/chlgusgh3315/222201094087)
- 연구소(삼성, 백준) [문제](https://www.acmicpc.net/problem/14502) [내풀이](https://blog.naver.com/chlgusgh3315/222201805889)
- 경쟁적 전염(백준) [문제](https://www.acmicpc.net/problem/18405) [내풀이](https://blog.naver.com/chlgusgh3315/222201902383)
- 괄호 변환(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60058) [내풀이](https://blog.naver.com/chlgusgh3315/222206499448)
- 연산자 끼워넣기(백준) [문제](https://www.acmicpc.net/problem/14888) [내풀이](https://blog.naver.com/chlgusgh3315/222206585839)
- 감시 피하기(백준)  [문제](https://www.acmicpc.net/problem/18428) [내풀이](https://blog.naver.com/chlgusgh3315/222207289860)
- 인구 이동(삼성, 백준) [문제](https://www.acmicpc.net/problem/16234) 틀림(시간초과)
- 블록 이동하기(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/60063) [내풀이](https://blog.naver.com/chlgusgh3315/222211242932)
- 백준 문제 모음 [DFS](https://www.acmicpc.net/problemset?sort=ac_desc&algo=126) [BFS](https://www.acmicpc.net/problemset?sort=ac_desc&algo=126)

## 정렬
단순히 라이브러리를 쓰면 되는 문제도 있고
각 정렬을 구현해볼줄 알아야함.
### 선택 정렬
> 선택정렬은 처음부터 끝까지 훑으며 가장 작은 원소를 **선택**해서 바꾸며 올라가는 알고리즘이다. 빅오는 N^2.
```
#임의의 배열
array=[4,5,0,1,9,7,6]

for i in range(len(array)):
    min_idx=i
    for j in range(i+1,len(array)):
        if array[min_idx]>array[j]:
            min_idx=j
    array[i],array[min_idx]=array[min_idx],array[i]
print(array)
```
### 삽입 정렬
> 삽입 정렬은 정렬된 배열에 원소를 **삽입**하여 정렬하는 방법이다. 빅오는 N^2. 정렬이 거의 되어있다면 빅오가 N에 가깝다.
```
#임의의 배열
array=[4,5,0,1,9,7,6]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j-1],array[j]=array[j],array[j-1]
        else:
            break
print(array)
```

### 퀵 정렬
> 피벗을 하나정하고(맨앞 원소)
피벗보다 왼쪽은 다 작고 오른쪽은 다 크게 만듦.
나머지 왼쪽과 오른쪽을 다시 퀵 정렬을 시킴. 빅오는 NlogN. 이미 정렬되어있다면 N^2가 된다.
```
#임의의 배열
array=[4,5,0,1,9,7,6]

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[pivot],array[right]=array[right],array[pivot]
        else:
            array[left],array[right]=array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
```

### 계수 정렬
> 계수정렬은 계수를 저장하는 방법이다. 즉 몇번 나왔는지만 체크한다.
dfs 구현할때 visited를 생각하면 될거같다. 빅오는 N+K다 K는 가장 큰 원소값이다. 약 100만이 넘어가면 비효율적이라고 한다. 그리고 저장된 정보를 확인은 따로 N번해줘야한다.
```
#임의의 배열
array=[4,5,0,1,9,7,6]

count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1

# 정렬된 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
```
### 문제들
- 국영수(백준) [문제](https://www.acmicpc.net/problem/10825) [내풀이](https://blog.naver.com/chlgusgh3315/222213041569)
- 안테나(백준) [문제](https://www.acmicpc.net/problem/18310) [내풀이](https://blog.naver.com/chlgusgh3315/222213049655)
- 실패율(카카오, 프로그래머스) [문제](https://programmers.co.kr/learn/courses/30/lessons/42889) [내풀이](https://blog.naver.com/chlgusgh3315/222213094241)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=97)

## 이진 탐색
 > 값이 정렬되어있을때 빠르게 탐색할 수 있음.
- 절반씩 탐색하므로 빅오는 log N
- 예제
```
def binary_search(array,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if mid==array[mid]:
        global result
        result=mid
        return None
    if mid>array[mid]:
        binary_search(array,mid+1,end)
    else:
        binary_search(array,start,mid-1)

```
- 라이브러리 사용하면 간편하게도 쓸 수 있다.
```
from bisect import bisect_left

arr_n.sort()
for i in range(len(arr_m)):
    res=bisect_left(arr_n,arr_m[i])
    if res<len(arr_n) and arr_n[res]==arr_m[i]:
        print(1)
    else:
        print(0)
```

### 문제들
- 공유기(백준) [문제](https://www.acmicpc.net/problem/2110) [내풀이](https://blog.naver.com/chlgusgh3315/222214760288)
- 가사 검색(백준) [문제](https://blog.naver.com/chlgusgh3315/222214760288) [내풀이](https://blog.naver.com/chlgusgh3315/222215092966)
- 수 찾기(백준) [문제](https://www.acmicpc.net/problem/1920) [내풀이](https://blog.naver.com/chlgusgh3315/222215159482)
- 나무 자르기(백준) [문제](https://www.acmicpc.net/problem/2805) [내풀이](https://blog.naver.com/chlgusgh3315/222215210337)
- 랜선 자르기(백준) [문제](https://www.acmicpc.net/problem/1654) [내풀이](https://blog.naver.com/chlgusgh3315/222215460736)

## DP
다이나믹 프로그램으로 풀 수 있는 문제는
1. 큰 문제를 작은 문제로 분할할 수 있고(분할정복)
2. 작은 문제가 반복적으로 사용될때.

재귀와 반복문으로 풀수있는데 반복문이 힙영역을 쓰지않아 메모리 초과를 막을수있다.
재귀로 풀면 탑다운 방식이고 반복문을 사용한다면 바텀업 방식이라고 볼수있다.
그래서 먼저 바텀업으로 시도해보자.
계산한 결과를 저장하는 테이블을 dp 테이블이라고 한단다.

- 예제 코드
```
n=int(input())

dt=[0]*30001
# 초기값 mem[1]=0
for i in range(2,n+1):
    dt[i]=dt[i-1]+1
    if i%2==0:
        dt[i]=min(dt[i],dt[i//2]+1)
    if i%3==0:
        dt[i]=min(dt[i],dt[i//3]+1)
    if i%5==0:
        dt[i]=min(dt[i],dt[i//5]+1)
print(dt[n])
```
### 문제들
- 정수 삼각형(백준) [문제](https://www.acmicpc.net/problem/1932) [내풀이](https://blog.naver.com/chlgusgh3315/222216147223)
- 퇴사(백준0 [문제](https://www.acmicpc.net/problem/14501) [내풀이](https://blog.naver.com/chlgusgh3315/222216214557)
- 가장 긴 증가하는 부분 수열(백준) [문제](https://www.acmicpc.net/problem/11053) [내풀이](https://blog.naver.com/chlgusgh3315/222216285910)
- 병사 배치하기(백준) [문제](https://www.acmicpc.net/problem/18353) [내풀이](https://blog.naver.com/chlgusgh3315/222216288203)
- 편집거리(백준) [문제](https://www.acmicpc.net/problem/7620) (아직 안풀어봄)
- 파도반 수열(백준) [문제](https://www.acmicpc.net/problem/9461) [내풀이](https://blog.naver.com/chlgusgh3315/222218231251)
- 스티커(백준) [문제](https://www.acmicpc.net/problem/9465) [내풀이](https://blog.naver.com/chlgusgh3315/222218242509)
- 오르막 수(백준) [문제](https://www.acmicpc.net/problem/11057) [내풀이](https://blog.naver.com/chlgusgh3315/222218293600)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=25)

## 최단 경로
## 다익스트라
> 한점에서 다른 점들까지의 최소 거리
> 
시작 노드에서 다른 노드까지의 거리를 찾고
최단 거리 노드를 방문하며 시작 노드로부터의 경로를 최소화.
모든 노드를 방문할때까지 반복.

노드중 가장 짧은 거리를 찾을때 모든 노드를 탐색하는것이 아닌 우선순위 큐를 사용하면 logV번으로 줄일 수 있다. 총 시간복잡도는 ElogV다
```
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

# 노드 n개, 간선 m개
n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    # a에서 b로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    # (거리,노드)
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 최단 거리 꺼내기
        dist,now=heapq.heappop(q)
        # 처리되었다면 패스
        if distance[now]<dist:
            continue
        for d in graph[now]:
            cost=dist+d[1]
            # 경유하는게 더 짧다면
            if cost<distance[d[0]]:
                distance[d[0]]=cost
                heapq.heappush(q,(cost,d[0]))
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
```
### 플로이드 워셜
모든 경로의 최단거리가 n*n 매트릭스에 저장된다.
노드 n번을 거치는데 각 단계마다 n^2^번 연산을 해야하므로 전체 빅오는   n^3^가 된다.
```
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
# 대각선 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

# 선분 정보
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        print(graph[a][b],end=' ')
    print()
```

### 문제들
- 플로이드(백준) [문제](https://www.acmicpc.net/problem/11404) [내풀이](https://blog.naver.com/chlgusgh3315/222219288385)
- 최단 경로(백준) [문제](https://www.acmicpc.net/problem/1753) [내풀이](https://blog.naver.com/chlgusgh3315/222219404919)
- 최소비용 구하기(백준) [문제](https://www.acmicpc.net/problem/1916) [내풀이](https://blog.naver.com/chlgusgh3315/222219418477)
- 알고스팟(백준) [문제](https://www.acmicpc.net/problem/1261) [내풀이](https://blog.naver.com/chlgusgh3315/222220454567)
- 파티(백준) [문제](https://www.acmicpc.net/problem/1238) [내풀이](https://blog.naver.com/chlgusgh3315/222220490436)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=22)

## 그래프
> union-find(크루스칼 알고리즘), 위상 정렬
### union-find
그래프에서 서로소 집합을 구하고 싶을때 사용하는 알고리즘
```
def find(parent,x):
    if parent[x]!=x:
        return find(parent,parent[x])
    return parent[x] // x로하면 단계마다 경로를 알 수 있음.

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(v+1):
    parent[i]=i

for _ in range(e):
    a,b=map(int,input().split())
    union(parent,a,b)

print("union result")
for i in range(1,v+1):
    print(find(parent,i),end=' ')
```
트리가 깊어지면 rank 개념을 넣어서 더 높이가 작은게 아래로 가게 넣어줘야함
```
rank = [0] * (n + 1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    # 높이가 낮은걸 아래로
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1

```

### 크루스칼 알고리즘
신장트리 - 모든 노드가 연결되면서 사이클을 이루지 않는 그래프
최소신장트리 - 신장트리중에 간선의 합이 최소인 신장트리

크루스칼 알고리즘 - 간선을 오름차순으로 정렬하고 간선의 부모가 다르면 union. 간선의 합이 최소인 최소신장트리 생성됨.
```
def find(parent,x):
    if parent[x]!=x:
        return find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[a]=b
    else:
        parent[b]=a

v,e=map(int,input().split())
parent=[0]*(v+1)
for i in range(v+1):
    parent[i]=i

edges=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()

res=0
for edge in edges:
    c,a,b=edge
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        res+=c
print(res)
```
### 위상 정렬
수업을 듣다보면 선수강해야하는 수업이 있다.
알고리즘 수업을 듣기위해서는 자료구조와 c언어를 먼저 수강해야한다.
다시 소프트웨어공학을 듣기위해서는 알고리즘을 선수강해야한다.
그렇다면 수강 순서는 자료구조 -> c언어 -> 알고리즘 -> 소프트웨어공학 순서가 될것이다.(자료구조와 c언어 순서무관)
이렇듯 방향 그래프에서 방향을 거스르지 않고 나열하는것을 위상정렬이라고 한다.

​

구현
각 노드에서 입력차원수를 indegree라고 하고 indegree가 0인 노드를 큐에 넣는다.
큐에서 하나씩 꺼내며 연결된 방향 노드의 indegree를 줄이고 0이되면 큐에 넣어준다.
큐에서 나오는 순서가 위상정렬에 결과가 된다.
모든 노드가 포함되기전에 큐가 비게되면 사이클이 존재한다는 뜻이다.
```
from collections import deque
v,e=map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q=deque()
    result=[]
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node]-=1
            if indegree[node]==0:
                q.append(node)
    return result
res=topology_sort()
for r in res:
    print(r,end=' ')
```

### 문제들
- 도시 분할 계획 [문제](https://www.acmicpc.net/problem/1647) [내풀이](https://blog.naver.com/chlgusgh3315/222227627333)
- 행성 터널 [문제](https://www.acmicpc.net/problem/2887) [내풀이](https://blog.naver.com/chlgusgh3315/222228089760)
- 순열 사이클 [문제](https://www.acmicpc.net/problem/10451) [내풀이](https://blog.naver.com/chlgusgh3315/222275490865)
- 백준 문제 모음 [링크](https://www.acmicpc.net/problemset?sort=ac_desc&algo=49)

## 기타
### python 입력 시간 문제시
```
import sys
input=sys.stdin.readline
```
### python 재귀 호출 제한 풀기
```
import sys
sys.setrecursionlimit(20000) # 다른수도됨
```
### 빈출 유형
코딩테스트 공부순서

백준 상단 문제메뉴 - 알고리즘 분류

#### 기본
1. 문자열
2. 정렬
3.	스택
4.	큐
5.	우선순위큐(힙)
6.	Set, Map
7.	이분탐색
8.	DFS(깊이 우선 탐색)
9.	BFS(너비 우선 탐색)
10. 백트래킹
11.	시뮬레이션, 구현 (삼성 기출의 대부분)
12.	그리디(탐욕법)
13.	누적합
14.	분할정복
15.	투포인터(두 포인터)
16.	위상정렬
17.	DP

#### 심화
18.	다익스트라
19.	플로이드 와샬
20.	벨만 포드
21.	유니온-파인드 (Disjoint set)
22.	MST(최소 스패닝 트리), 크루스칼
23.	세그먼트 트리
24.	트라이
