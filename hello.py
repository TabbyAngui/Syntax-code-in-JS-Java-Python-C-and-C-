print ("Hello from Python")
name = input("Your name?")
print(f"Hello{name}!")
x = 24;
print(f"Tabby are you {x} years old?")
#declaring every type of variable:. integer, decimal,character and string.

Grade = 'A';
Student = "Jaden";
Class = 8;
Avemarks = 79.8;
Clusterpoint = 4.35;
print(f"Did you know {Student} of class {Class} got a {Grade} of {Avemarks} which is a cluster point of: {Clusterpoint}!")

# printing boolean
# true or false
is_pass = True
print(is_pass)
#printing null

fail = None
print(fail)

# Printing a list, can be a set of strings, nmbers,characters or one that includes all
# For integers we use (), for char we use[] for a mixture of strings we use{}

vowels = ['a','e','i','o','u']
print (vowels)
alphabets = {"A : Apple", "B :Boy", "C:Cat"}
print (alphabets)
Numbers = (1,2,3,3.4,4.54)
print (Numbers)

# The details above of Jayden could be printed in a list

Jaden_dets = {" Name" : "Jaden "," Class" : "8 "," Grade" : "A "," Avemarks" : "79.8 "," Clusterpoints" : "4.35 "}
print(f"Below are Jaden's details\n : {Jaden_dets}")

# The output prints itself as a list, but if you want to print as name...then value, there is a concept in py called dictionaries.
# Dictionary works as a dictionary, where there is a key value and a value or data is assigned to it i.e x = {"Key": "Value"}
# Repeating that to Jaden_dets
# the function for specifies that in the list of items in Jaden_dets, print the key and the value only.
print("THE DIFFERENCE BETWEEN LIST AND DICTIONARY IN PY AS ILLUSTRATED.")
print("Below are Jaden's details:")
for key, value in Jaden_dets.items():
    print(f"{key}: {value}")
