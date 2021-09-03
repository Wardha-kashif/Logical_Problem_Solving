# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("hello world")

#This is a comment
#This is the Basic Print Statement
print("Wardha Kashif")

#Variable initailization
a=5
b="Wardha"

print(a)
print(b)
print(type(a))
print(type(b))
# Change the type
c=str(a)
print(type(a))

#Python is Case Sensitive
# varible name Cannot start with number and contain alphabets,underscore,0_9

# String can be access as Array
print(b[0])


#looping through String
for x in b:
    print(x)

#For checking the length of Array
print(len(b))

#Checking particular Element in string
string="sana is sara's friend"
print("sana" in string)
print("asma" in string)

#Slicing in String
string1="Hello World"
print(string1[2:7])

#get from starting to position 5

print(string1[:5])

#Capitalize

b="Sana"
print(b.upper())
print(b.lower())

# Removing white spaces from beginning and end of the String
print(b.split())

#Replace a String

print(b.replace("S","J"))

#spliiting a String

print(string1.split(","))

#Concatenation in String
d="Wardha"
e="Kashif"
f=d + " "  + e
print(f)


#Format
age=22
a="wardha age is  {}"
print(a.format(age))

#To give Double Quote
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print(10 > 9)
print(10 == 9)
print(10 < 9)


print(2**3)

#List
mylist = ["apple", "banana", "cherry"]
print(mylist)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Looping through the list
list1=["wardha","Kashif"]
for x in list1:
    print(x)

#Calculating the range
x = range(3, 6)
for n in x:
  print(n)

#List Append
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Sorting the List
a=["apple","orange","banana"]
print(a.sort())

#Descending order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Creating A Tuple

a=("a","b","c");


#Creating a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

dict={
    "brand":"Ford"
}
dict["model"]="Mustang"
print(dict)

a=5
b=10
if a>b:
    print("a is greater")
else:
    print("b is Greater")


#Taking input from Users

a=input("Enter user input")
print(a)


