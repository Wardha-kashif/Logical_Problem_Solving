#Starting with the List

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
Vegetable=['onion','potato','chilli']

#adding a single elements to a list
fruits.append("watermelon")
print(fruits)

#Extending the list by adding all the item from the Iterable
fruits.extend(Vegetable)
print(fruits)

#insert(i,x) element is used to add element at a specific position
fruits.insert(3,"peach")
print(fruits)

#list.remove(x)
fruits.remove("orange")
print(fruits)

#pop element in an list
fruits.pop(1)
print(fruits)

#To remove all the items from the list
Vegetable.clear()
print(Vegetable)

#The index() method returns the position at the first occurrence of the specified value.
x = fruits.index("kiwi")
print(fruits)
print(x)

#To calculate the count of specific element  in the list
print(fruits.count("apple"))

# Sorting of the list in ascending and desceding order
fruits.sort()
print(fruits)

# default in ascending
fruits.sort(reverse=True)
print(fruits)

#to reverse the elements of the string
fruits.reverse()
print(fruits)

#to create a shallow copy of the list
fruits_cpy=fruits.copy()
print(fruits_cpy)

#Using List as stack
#Stack is Last in First out(LIFO)
#adding an element in the stack is done by append and to remove last in use pop to remove
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

#Using list as Queues(First in First Out)
from collections import deque
queue=deque([3,4,5])
queue.append(6)
print("Queue\n")
print(queue)
queue.popleft()
print(queue)


#List Comprehensions
# we want to create a list of squares
#by simple Function
squares=[]
for i in range(10):
    squares.append(i ** 2)
print(squares)

#by using list Comprehension
squares=[i**2 for i in range(10)]
print(squares)

array1=['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

arr2=[x for x in array1]
print(arr2)

#make an program that print x,y if x!y
comb=[(x,y) for x in [1,2,3] for y in [5,6,7] if x!=y]
print(comb)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vec2=[x*2 for x in vec]
print(vec2)

# filter the list to exclude negative number
vec3=[x for x in vec2 if x>0]
print(vec3)

# apply a function to all the elements
vec=[abs(x) for x in vec]
print(vec)

#call a method on each elements
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
freshfruit=[x.strip() for x in freshfruit]
print(freshfruit)

# create a list of 2-tuples like (number, square)
square=[(x,x**2) for x in range(i)]
print(square)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

for elem in vec:
    for num in elem:
        print(num)

#Nested List Comprehensions
matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


# #list comprehension will transpose rows and columns
# transpose=[]
# for i in range(4):
#     transpose.append([row[i] for row in matrix])
# print(transpose)

matrix=[
    [1,2,3,4],
    [4,5,6.7],
    [7,8,9,10],
    [10,11,12,13],
]
transposed = []
for i in range(3):
    transposed.append([row[i] for row in matrix])
print(transposed)

# #by list comprehension
x=[[row[i] for row in matrix] for i in range(3)]
print(x)

#The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice).
a=[1,2,3,4,5]
del a[0]
print(a)

#Deleting a slice
del a[2:4]
print(a)


#Tuples and Sequences
#tuples cannot change

#Sets(unique elements, union ,intersection)
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

# letters in a but not in b
print(a-b)

# letters in a or b or both
print(a|b)

#letters in both a and b
print(a & b)

#letters in a or b but not both
print(a ^ b)