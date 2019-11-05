# Implementing Singly Linked List from Scratch in Python


class Node:
    '''
    Class Node will store our data and memory address of Next node
    We will insert this node to the linked list
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverseList(self):
        '''
        Traversing through every item of the Linked List

        '''
        if self.head is None:                   # Only situation head will be none is when List is empty
            print ("Linked List is Empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, end = "->")
                temp = temp.next


    def insertAtBegining(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self,value):
        newNode = Node(value)
        if(self.head is None): #this means list is empty
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next

            temp.next = newNode

    def insertAfter(self,x,value):
        '''

        :param x: Data after which you want to insert
        :param value: value you want to insert
        '''
        if(self.head is None):
            print("List is Empty : insertAfter Failed")
            return

        temp = self.head
        while(temp is not None):
            if(temp.value == x):
                newNode = Node(value)
                newNode.next = temp.next
                temp.next = newNode
                return
            elif(temp.next is None):
                print(f"{x} is not present in list")
                return
            else:
                temp = temp.next

    def insertBefore(self,x,value):
        if (self.head is None):
            print("List is Empty : insertBefore Failed")
            return
        if(self.head.value == x):
            newNode = Node(value)
            newNode.next = self.head.next
            self.head = newNode
            return
        temp = self.head
        while(temp.next is not None):
            if(temp.next.value == x):
                newNode = Node(value)
                newNode.next = temp.next
                temp.next = newNode
                return
            temp=temp.next



    def insertAtIndex(self,index,value):
        if index == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            while(index != 1):
                temp = temp.next
                index-=1

            if(temp == None):
                print("Index out of bound")
            else:
                newNode = Node(value)
                newNode.next = temp.next
                temp.next = newNode





list = LinkedList()

list.insertAtEnd(10)
list.insertAtEnd(20)
list.insertAtEnd(40)
list.insertBefore(40,30)
list.insertAtIndex(4,50)

list.traverseList()
