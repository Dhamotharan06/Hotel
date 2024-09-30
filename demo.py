array=[34,54,67,89,45]
search=int(input("Enter a search element:"))
for i in range(len(array)):
      flag=0
      if(array[i]==search):
        flag=1
        break
if(flag==1):
    print("Element found")
else:
    print("element not found")






