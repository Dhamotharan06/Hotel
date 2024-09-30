class node:
    def _init_(self,val):
        self.val=val
        self.next=None
head=node(10)
def insert_at_front(head,val):
    if head==None:
        head=node(val)
        return head
    else:
        ne=node(val)
        ne.next=head
        head=ne
        return head
head=insert_at_front(head,20)
def traversal(head):
    root=head
    while root:
        print(root.val,"->",end="")
        root=root.next
        print("head")
traversal(head)