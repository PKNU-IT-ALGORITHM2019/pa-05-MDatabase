class Node:
    def __init__(self, val,n,mean):
        self.val = val
        self.n=n
        self.mean=mean
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val,n,mean):
        self.root = Node(val,n,mean)

    def insert(self, val,n,mean):
        if(self.root is None):
            self.setRoot(val,n,mean)
        else:
            self.insertNode(self.root, val,n,mean)

    def insertNode(self, currentNode, val,n,mean):
        if(val.lower() <= currentNode.val.lower()):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val,n,mean)
            else:
                currentNode.leftChild = Node(val,n,mean)
        elif(val.lower() > currentNode.val.lower()):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val,n,mean)
            else:
                currentNode.rightChild = Node(val,n,mean)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.val:
            deleted = True
            if node.leftChild and node.rightChild:
                # replace the node to the leftmost of node.right
                parent, child = node, node.rightChild
                while child.leftChild is not None:
                    parent, child = child, child.leftChild
                child.leftChild = node.leftChild
                if parent != node:
                    parent.leftChild = child.rightChild
                    child.rightChild = node.rightChild
                node = child
            elif node.leftChild or node.rightChild:
                node = node.leftChild or node.rightChild
            else:
                node = None
        elif key < node.val:
            node.leftChild, deleted = self._delete_value(node.leftChild, key)
        else:
            node.rightChild, deleted = self._delete_value(node.rightChild, key)
        return node, deleted
f=open("shuffled_dict.txt","r",encoding="utf-8")
lines=f.readlines();
bst=BST()
dwords=[] # deleteall에서 읽은 삭제할 단어목록
count=0 #deleteall에서 삭제한 단어의 갯수
for i in range(len(lines)):
    wordtemp=lines[i].split(" (")[0]
    ntemp=lines[i].split(") ")[0].split("(")[1]
    for j in range(1,len(lines[i].split(")"))):
        if j is 1:
            meantemp=lines[i].split(")")[j]
        else :
            meantemp+=lines[i].split(")")[j]
    #node=Node(wordtemp,ntemp,meantemp)
    bst.insert(wordtemp,ntemp,meantemp)

switch=1
while(switch):
    uin=input("$ ").split(" ")
    if uin[0] == "exit":
        switch=0
    elif uin[0] =="add":
        win=input("word : ")
        nin=input("class : ")
        meanin=input("meaning : ")
        bst.insert(win,nin,meanin)
    elif uin[0] =="delete":
        wdel=uin[1]
        bst.delete(wdel)

    elif uin[0] =="deleteall":
        dfname=uin[1]
        df=open(dfname,"r",encoding="utf-8")
        for i in df.readlines():
            dwords.append(i.split("\n")[0])
        for i in dwords:
            if bst.delete(i) is True:
                count+=1
        print(len(dwords),"words were deleted successfully")
        count=0
