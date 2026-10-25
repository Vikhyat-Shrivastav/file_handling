import csv
with open('blood_relation.csv','r') as file:
    rows=csv.reader(file)
    for row in rows:
        print(row)



json 
SERIALIZATION

import json


student={
    "name":"VIKHYAT",
    "age":20,
    "courses":["Math","Physics","Chemistry"]  
}
json_object=json.dumps(student)
print(json_object)

import json


student = '''{
"name":"VIKHYAT",
"age":20,
"courses":["Math","Physics","Chemistry"]
}'''

json_object=json.loads(student)
print(json_object)
name = input("Enter your name: ")
a= int(input("enter first number: "))
b= int(input("enter second number: "))
if b==0:
    print("division by zero is not possible enter a valid number other than zero")
else:
    print("division is: ",a/b)
num1= 10
num2= "20"
try:
    sum = num1+num2
    print(sum)
except TypeError:

    print('num2 str')


try:
    list =[10,20,30]
    index=int(input("enter index:"))
    print(list[index])
except ValueError:
    print('enter a valid index')
except  IndexError:
    print('enter right index')