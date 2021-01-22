class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        tempHead = self.head
        while index != 0:
            tempHead = tempHead.next
            if tempHead == None:
                return -1
            index -= 1
        return tempHead.value

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head != None:
            node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        tempHead = self.head

        if tempHead == None:
            MyLinkedList.addAtHead(self, val)
            return

        while tempHead.next != None:
            tempHead = tempHead.next

        node = Node(val)
        tempHead.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            MyLinkedList.addAtHead(self, val)
            return

        tempHead = self.head
        while index > 1:
            if tempHead == None:
                return
            tempHead = tempHead.next
            index -= 1

        node = Node(val)

        if tempHead.next != None:
            node.next = tempHead.next

        tempHead.next = node

    def deleteAtIndex(self, index: int) -> None:
        tempHead = self.head
        if index < 0 or tempHead == None:
            return
        if index == 0 and tempHead != None:
            if tempHead.next == None:
                return
            else:
                self.head = tempHead.next
        while index > 1:
            if tempHead.next == None:
                return
            index -= 1
            tempHead = tempHead.next
        if tempHead.next == None:
            return
        if tempHead.next.next == None:
            tempHead.next = None
            return
        tempHead.next = tempHead.next.next
