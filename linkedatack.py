class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def _init_(self):
        self.top = None
        self.temp = None

    def push(self,data):
        newnode = Node(data)
        if(self.top is None):
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode 

    def pop(self):
        if(self.top is None):
            print("Underflow")
        else:    
            self.temp = self.top
            self.top = self.top.next
            del(self.temp) 

    def peek(self):
        print(self.top.data)
    def display(self):
        self.temp = self.top
        while(self.temp is not None):
            print(self.temp.data)
            self.temp = self.temp.next
s = Stack()
n = int(input("Enter the number of nodes :"))  
for i in range(n):
    data = int(input("enter the data :"))
s.push()  
s.pop() 
s.peek()                  
s.display()


if __name__=="main":
    expr=input("Enter the expression")
    size=int(input("enter the size"))
    bs=BalancingOffSymbol(size)
    valid=bs.checkexpression(expr)
    if valid:
        print("balance")
    else:
        print("imbalanace")