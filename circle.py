class circle:
    def area(self,r,n):
        return n*r**2
    def perimeter(self,r,n):
         return 2*n*r
     
n=3.14
r=int(input("enter the radius:"))
sum_areas=circle()
num=sum_areas.area(n,r)
a=sum_areas.perimeter(n,r)
print(f"The area of the circle is:",num)
print(f"The perimeter of the circle is:",a)

