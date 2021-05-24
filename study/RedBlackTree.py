"""
Red Black Tree
Insert 구현되어있음.
TODO : Delete

시뮬레이터 : https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
위키피디아 : https://ko.wikipedia.org/wiki/%EB%A0%88%EB%93%9C-%EB%B8%94%EB%9E%99_%ED%8A%B8%EB%A6%AC
"""
from enum import Enum

class Color(Enum):
    RED=1
    BLACK=2

class Node():
    def __init__(self,data,color=Color.RED):
        self.data=data
        self.parent=self.left=self.right=None
        self.color=color
    def getNIL(self):
        return Node(None,Color.BLACK)

class RBT():
    def __init__(self):
        self.root=None
    def findGrandparent(self,node):
        if node==None:
            return None
        elif node.parent:
            return node.parent.parent
        else:
            return None
    def findUncle(self,node):
        if node==None:
            return None
        grandparent = self.findGrandparent(node)
        if grandparent:
            if grandparent.left == node.parent:
                return grandparent.right
            else:
                return grandparent.left
        else:
            return None
    def insertNIL(self,node):
        if node==None:
            return None
        leftNIL=node.getNIL()
        rightNIL=node.getNIL()
        node.left=leftNIL
        leftNIL.parent=node
        node.right=rightNIL
        rightNIL.parent=node
    def insert(self,node):
        # NIL 삽입
        self.insertNIL(node)
        # BST 과정 진행
        self.BST_insert(node)
        # RBT 과정 진행
        self.RBT_insert(node)

    def BST_insert(self,node):
        # 루트 노드일때
        if self.root == None:
            self.root = node
        else:
            # 넣을 자리를 찾아감
            tmp = self.root
            while tmp.data != None:
                if node.data < tmp.data:
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            # 해당 자리에 넣어줌
            node.parent = tmp.parent
            if tmp.parent.left == tmp:
                tmp.parent.left = node
            else:
                tmp.parent.right = node

    def RBT_insert(self,node):
        # 루트 노드일때
        if node.parent == None:
            node.color = Color.BLACK
            return None

        # 부모노드가 Black 일때
        if node.parent.color==Color.BLACK:
            return None

        # Recoloring
        grand=self.findGrandparent(node)
        uncle=self.findUncle(node)
        if uncle!=None and uncle.color==Color.RED:
           node.parent.color=Color.BLACK
           uncle.color=Color.BLACK
           grand.color=Color.RED
           # grandparent 재귀호출
           self.RBT_insert(grand)
           return None

        # Restructuring 1 (꺽인 모양 -> 일자 모양)
        # node 가 오른쪽 자식이고 부모가 왼쪽 자식일때
        if node == node.parent.right and node.parent==grand.left:
            # rotate left
            self.rotate_left(node.parent)
            # node 변경
            node=node.left
        # node 가 왼쪽 자식이고 부모가 오른쪽 자식일때
        if node == node.parent.left and node.parent==grand.right:
            # rotate right
            self.rotate_right(node.parent)
            # node 변경
            node = node.left
        # node가 변경되었으니 관계 재설정
        grand = self.findGrandparent(node)

        # Restructuring 2 (일자 모양 -> Restructuring)
        node.parent.color=Color.BLACK
        grand.color=Color.RED
        if node == node.parent.left:
            self.rotate_right(grand)
        else:
            self.rotate_left(grand)

        # root 재설정
        self.adjustRoot(grand)


    def rotate_left(self,node):
        child=node.right
        parent=node.parent

        # 자식 부모 재설정
        if child.left!=None:
            child.left.parent=node

        node.right=child.left
        node.parent=child
        child.left=node
        child.parent=parent

        # 부모 재설정
        if parent!=None:
            if parent.left==node:
                parent.left=child
            else:
                parent.right=child

    def rotate_right(self, node):
        child = node.left
        parent = node.parent

        # 자식 부모 재설정
        if child.right != None:
            child.right.parent = node

        node.left = child.right
        node.parent = child
        child.right = node
        child.parent = parent

        # 부모 재설정
        if parent != None:
            if parent.right == node:
                parent.right = child
            else:
                parent.left = child

    def adjustRoot(self,node):
        tmp=node
        while tmp.parent!=None:
            tmp=tmp.parent
        self.root=tmp

    def printDate(self,data):
        print("find data : ",data)
        cnt=0
        if self.root==None:
            print("Empty Tree")
            return None
        tmp=self.root
        while tmp.data!=None:
            cnt+=1
            if tmp.data==data:
                print('#',cnt," : ",tmp.data," ",tmp.color," find!")
                return None
            elif data<tmp.data:
                print('#',cnt," : ",tmp.data," ",tmp.color," go left")
                tmp=tmp.left
            else:
                print('#',cnt, " : ", tmp.data," ",tmp.color," go right")
                tmp = tmp.right
        print("can't find data")

# main
rbt=RBT()

for i in range(10):
    rbt.insert(Node(i))

rbt.printDate(6)