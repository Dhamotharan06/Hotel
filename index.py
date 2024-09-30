
class calculator:
    def add(self,a,b):
        return a + b
    
    def sub(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b


sum_add=calculator()
num=sum_add.add(2,4)
print(f"The addition of 2 and 4 is",num)


sum_sub=calculator()
num=sum_sub.sub(2,4)
print(f"The subraction of 2 and 4 is:",num)

sum_multiply=calculator()
num=sum_multiply.multiply(2,4)
print(f"The multiplication of 2 and 4 is:",num)

sum_div=calculator()
num=sum_div.div(2,4)
print(f"Th divison of 2 and 4 is:",num)