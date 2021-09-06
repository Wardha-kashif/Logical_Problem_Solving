#Dictionary Practice

#How to create Dictionary
Student={
   "Name":"wardha",
   "Age":22,
   "Quliafication":"Software Engineer"
}
print(Student)

#To pick information from a dictionary
print(Student["Age"])

#Adding a new pair to Dictionary
Student["Gender"]="Female"
print(Student)

#Looping through a dictionary values
for each_value in Student.values():
   print(each_value)

#Looping through a dictionary keys
for each_key in Student.keys():
   print(each_key)

#Looping through both keys and values
for each_key,each_values in Student.items():
   print("The Student " + each_key + " is " + str(each_values))

# # Make a programInitialize dictionary and later add value
# Employee={}
#
# user_input=input("Enter a User input")
# for user in user_input:

#Working on List of dictinaries
#we can create dictinary inside the lsit but following this approach will not let us allow to delte a Customer
#so the best approach for this is use the dictinary within dictinary


#Creating a dictinary within dictionary
Employee={
1:
   {
"Name":"Sana",
"age":"23",
"Designation":"Engineer"
   },
2:
 {
"Name":"Ali",
"age":"24",
"Designation":"ElectricalEngineer"
 },
3:
 {
"Name":"Sobia",
"age":"34",
"Designation":"HR"
  },

}

#How to acccess Elements within Dictionary

print(Employee[2])

#how to access element from a Child elements

print(Employee[2]["Name"])
