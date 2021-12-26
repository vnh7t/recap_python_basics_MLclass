from Employee import *
"read input file"
file=open("/Users/venkatavarunnelakuditi/Desktop/input.txt",'r')
"making a list of lines from a lines varible"
lines=file.readlines()
emplist=dict()
"converting file into list of line from second line"
for line in lines[1:]:
    "strip the space before and after the string"
    line=line.strip()
    "converting line into list of word"
    words=line.split()
    "check the first word in the line, call proper action"
    if words[0]=='NEW':
        "if new keyword is first in the list then cleate a object"
        if words[6]=='F':
            "creating full time employee"
            emplist[words[1]]=FullTimeEmployee(words[1],words[2]+words[3], words[4],int(words[5]))
        else:
            "creating part time employee"            
            emplist[words[1]]=PartTimeEmployee(words[1],words[2]+words[3], words[4],int(words[5]))
    elif words[0]=='RAISE':
        "if raise keyword is first in the list then check for the attional input and call the function"
        if len(words)>2:
            "if user suppleis raise argement"
            emplist[words[1]].giveRaise(int(words[2]))
        else:
            emplist[words[1]].giveRaise()
    elif words[0]=='PAY':
        "if pay keyword is first, then make payment to all employess"
        for x in emplist.values():
            x.PAY()
    elif words[0]=='FIRE':
        "if fire keyword is first, then make employee fireee"
        emplist[words[1]].FIRE()



"output file to save output"
outfile=open("/Users/venkatavarunnelakuditi/Desktop/output1.txt",'w')
text=""
"writing into the string and coping to file"
"read employee by employee"
for x in emplist.values():
    emp_type=""
    "checking type of the object to find its type"
    if x.__class__ is FullTimeEmployee:
        emp_type="Full Time Employee"
    else:
        emp_type="Part Time Employee"
    "to check employee is currently working or not"
    if x.IsEmployed()==True:
        "writing the output into a text varible"
        text=text+str(x.emp_id) +" : " +x.emp_name +" \t "+x.emp_department+"\t pay earned to date :"+str(x.emp_balance)+"\t current salary: $"+str(x.emp_salary)+"\t employeement type: "+emp_type
    else:
        text=text+str(x.emp_id) +" : " +x.emp_name +" \t "+x.emp_department+"\t employeement type: "+" Not employed with the company."
    text=text+"\n..............\n"
"output is copied to text and text is writed to file"
text=text+"Total number of employees currently in the company is: "+str(Employee.count)+"\n"
"average salary of full time employee"
text=text+"fulltime employee avg sal: "+ Employee.catagoryEmployeeAverageSalary(emplist.values(),FullTimeEmployee)
"average salary of part time employee"
text=text+"\nparttime employee avg sal: "+ Employee.catagoryEmployeeAverageSalary(emplist.values(),PartTimeEmployee)
"writing output to output file"
outfile.write("output: \n"+ text)
