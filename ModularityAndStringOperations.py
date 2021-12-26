"""Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
fullname function that should return the (full name).
o For example:
▪ First_name = “Ahmed”, last_name = “Albishri”
▪ Full_name = “Ahmed Albishri”
o Write function named “string_alternative” that returns every other char in the full_name string.
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for this program and call it from
main function."""

"function to append ints parameters"
def nameAppend(first_name, last_name):
    "string concatination"
    return first_name+" "+last_name


"function to trim string alternative char, using flag logic"
def string_alternative(name):
    output_string=""
    flag=0
    for x in name:
        "used flag to step concatination"
        if flag==0:
            output_string=output_string+x
            flag=1
        else:
            flag=0
            continue
    return output_string

"function to trim string alternative char by using slice"
def string_alternative2(name):
    "slicing the string with one step "
    output_string=name[::2]
    return output_string

def main():
    "passing the string to append"
    name=nameAppend("varun","nelakuditi")
    "callin string_alternative2 to append the strings"
    altered_string=string_alternative2(name)
    print(altered_string)
main()
