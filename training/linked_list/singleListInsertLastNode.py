class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.Next
            lastNode.next = newNode

    def printLinkedList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

node1 = Node('vijay')
node2 = Node('vicky')

linkedList = LinkedList()
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.printLinkedList()