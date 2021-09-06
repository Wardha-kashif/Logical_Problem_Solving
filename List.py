#practicing List

lst=["wardha",22,'software Enginnering']

#How to access elemts frm a List
print(lst[1])

#Accessing all elements
for i in lst:
    print(i)

#Adding an elements in the list

lst.append("sana")
print(lst)

#Concatenate two lists
lst1=["arif",67,"Electrical Engineer"]
print(lst + lst1)

#Slicing Concept in list
print(lst[1:3])

#if the output you select from starting
print(lst[:2])

#if you want the output till end of the string
print(lst[1:])

#Deleting and removing List Elements
del lst[0]
print(lst)

#if we want to remove by a value
lst.remove(22)
print(lst)

#Popping up the Elements means remove it and you can store this value in seperate variable
# lst2=[]
# lst2=lst.pop(1)
# print(lst2)
lst2=[]
lst2.insert(0,lst.pop(1))
print(lst2)