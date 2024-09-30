class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.temp=None

    def creation(self):
        num=int(input("Enter the number of nodes:"))
        for i in range(num):
            data=int(input("Enter the data:"))
            newnode=node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode

    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end='->')
            self.temp=temp.next
        print("none")
