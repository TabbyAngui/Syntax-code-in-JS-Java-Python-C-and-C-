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
print("THE DIFFERENCE BETWEEN LIST AND DICTIONARY IN PY AS ILLUSTRATED.\n")
print("Below are Jaden's details:")
for key, value in Jaden_dets.items():
    print(f"{key}: {value}")

k = 43
m = 2

# Arithmetic Operators    
print("\n")
print('Addition:', k + m)
print('Substraction:', k - m)
print('Multiplication:', k * m)
print('Division:', k / m)
print('Remainder:', k % m)
print('Power:', k ** m)

# In Python we don't use increment or decrement of one operands, its just tvalue +1 since yknow python tries to simplify everything and using for loops where you are like for k <10 k>5, k++  it simplified stuff, and we gonna see when we reach on the for statement.

# Assignment operators
print("\n")
l = 7
print('Assigning:a = ',l)
l +=7
print('Add: a = a + 7 : ',l)
l -=12
print('Substract: a = a - 12 : ',l)
l *=4
print('Multiply: a = a * 4 : ',l)
l /=2
print('Divide: a = a / 2 : ',l)
l %=3
print('Remainder: a = a % 3 : ',l)
l **=3
print('Power: a = a ** 3 : ',l)

#Comparison operators
print("\n")
print('k = 43, m = 2, k==m is True/False [if == is equal to] : ',k==m)
print('k = 43, m = 2, k!=m is True/False [if != is Not equal to] : ',k!=m)
print('k = 43, m = 2, k>m is True/False [if > is greater than] : ',k>m)
print('k = 43, m = 2, k<m is True/False [if < is lesser than] : ',k<m)
print('k = 43, m = 2, k>=m is True/False [if >= is  greater or equal to] : ',k>=m)
print('k = 43, m = 2, k<=m is True/False [if <= is lesser or equal to] : ',k<=m)

#logical operators
print("\n")
z =  7;

print(z > 2) and (z < 1);
print(z > 5) and (a < 10);
print(z > 2) or (z < 1);
print(z > 5) or (z < 10);
print(not(z > 1));
print(not(z > 10));


# bitwise operators, works on bits...changes numbers to bits then do logical operations
#i.e 5 & 3 :5 = 0101 and 3 = 0011 rules of bit 1 & 1 = 1 , 0 & 1 = 0, 1 & 0 = 0, 0 & 0 = 0
#doing the operation 5 & 3 = 0001 which is 1

print('\n')
print("BITWISE Operatorsperform logic operator in each bit using the AND, NOT, OR, XOR , FOR EXAMPLE and OPERATOR WE KNOW 1 & O = 0 1 & 1 = 1")
print("5 & 3: ", 5 & 3) #BITWISE AND
print("5 | 3: ", 5 | 3) #BITWISE OR
print("5 ^ 3: ", 5 ^ 3) #BITWISE XOR
print(" ~ 5: ", ~ 5 )   #BITWISE NOT
print("5 << 3: ", 5 << 3) #Something about shift but i dontget it HA!
print("5 >> 3: ", 5 >> 3)

#Identity operator, we use "is" if its identical " is not" if its not identical

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# membership operators, check if data is in the said data usinng 'in' and 'not in'.

message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True
# check if 'hello' is present in message string
print('hello' not in message)  # prints True
# check if '1' key is present in dict1
print(1 in dict1)  # prints True
# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

