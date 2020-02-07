list=[]
list1=[]
n= int(input("enter the number of students:"))
for i in range(0,n):
    a=int(input())
    list.append(a)
print(list)


for j in list:
    kg=(j * 0.45)
    list1.append(kg)
print("the list in kgs is:")
print(list1)


