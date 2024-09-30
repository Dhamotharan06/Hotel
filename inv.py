def selection_sort(li):
    for i in range(len(li)):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]
        

n = int(input("Enter the number of elements: "))
li = []
for i in range(n):
    x = int(input("Enter a number: "))
    li.append(x)

print("Original List:", li)
selection_sort(li)
print("Sorted array:", li)



        

        