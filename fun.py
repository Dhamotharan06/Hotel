class ListADT:

    def __init__(self):
        self.data = []
    def append(self, value):
        self.data.append(value)
    def insert(self, index, value):
        self.data.insert(index, value)
    def remove(self, value):
        self.data.remove(value)
    def pop(self, index=None):
        return self.data.pop(index)
    def index(self, value):
        return self.data.index(value)
mylist=ListADT()
choice=int(input("Enter your choice:"))
if choice==1:
    value=int(input("Enter value to append:"))
    mylist.append(value)
    