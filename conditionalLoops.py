"""Write a program, which reads heights (inches.) customers into a list and convert these heights to
  1) Nested interactive loop.
 2) List comprehensions
 
 Example: L1: [150,155, 145, 148]
 Output: [68.03, 70.3, 65.77, 67.13]"""

"Taking users response"
user_responce=input("do you want to enter data, to enter data enter Y else N")
"Creating a list to store the input"
inputInInchesList=[]
"applying interactive loop to terminate or run the users response "
while(user_responce!='N'):
    user_input=int(input("enter data in inches"))
    "Adding Users input to the list"
    inputInInchesList.append(user_input)
    user_responce=input("do you want to enter more data, to enter data enter Y else N")
#print(inputInInchesList)
"Converting input value into Cm using list comprehensions"
outputInCm = [x*2.54 for x in inputInInchesList]
print(outputInCm)
