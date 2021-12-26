""" getting a string/input from the user"""
input_str=input("Enter your string: ")

""" getting first char postion which user whants to delete"""
positiondel1=int(input(f"position of string you whant to delete one character: {input_str}  :"))

"""" slicing , rejoining and assining for the first char deletion"""
input_str=input_str[:positiondel1]+input_str[positiondel1+1:]

""" getting second char postion which user whants to delete"""
positiondel2=int(input(f"position of string you whant to delete one character: {input_str} :"))

"""" slicing , rejoining and assining for the first char deletion"""
input_str=input_str[:positiondel2]+input_str[positiondel2+1:]

print(f"revers of string after to deletions : {input_str[::-1]}")
