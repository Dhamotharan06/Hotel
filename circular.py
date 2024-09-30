""" class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.temp=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the data for nodes:"))
            newnode=Node2(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                newnode.prev=self.temp
                self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end="->")
            self.temp=self.temp.next
linkedlist=DLL()
linkedlist.creation()
linkedlist.display()
 """
class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.temp=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the data for nodes:"))
            newnode=Node2(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                newnode.prev=self.temp
                self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end="->")
            self.temp=self.temp.next
    def insertatbegin(self):
        data=int(input("Enter the number:"))
        newnode=Node2(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def insertAtEnd(self):
        data=int(input("Enter the data:"))
        newnode=Node2(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
    def deletionAtEnd(self):
        data=int(input("Enter a data:"))
        
linkedlist=DLL()
linkedlist.creation()
linkedlist.display()
linkedlist.insertatbegin()
linkedlist.display()
linkedlist.insertAtEnd()
linkedlist.display()