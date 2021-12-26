"parent class"
class Employee:
    "class varible to keep track employee count"
    count=0
    "constructor to initialize new object and private method is triggerd init"
    def __init__(self,id, name, department, salary, balance=0, isEmployed=True):
        self.emp_id=id
        self.emp_name=name
        self.emp_department=department
        self.emp_salary=salary
        self.emp_balance=balance
        self.isEmployed=isEmployed
        "call for private method"
        self.__employeeCount()
    
    "private method to do increament class varible count"
    def __employeeCount(self):
        Employee.count=Employee.count+1
    
    "method to pay salary after checking the employee working status"
    def PAY(self):
        "function call to make sure employee is exiting or not"
        if self.IsEmployed:
            "balance increased by one month salary"
            self.emp_balance=self.emp_balance+self.emp_salary

    "method to Fire an employee and set salary to zero"
    def FIRE(self):
        "changing employee status"
        self.isEmployed=False
        "setting payrate to 0"
        self.emp_salary=0
        "reducing employee count"
        Employee.count=Employee.count-1
    
    "function to check employeed or not, and return boolen value"
    def IsEmployed(self):
        return self.isEmployed
    
    "static method to calculate avg salarys by department wise, here i am using __class__ to check type of object"
    @staticmethod
    def catagoryEmployeeAverageSalary(li,searchString):
        temp=0
        lt=[x for x in li if x.__class__ is searchString]
        "calculating average"
        for x in lt:
            temp=x.emp_salary+temp
        return str(temp/len(lt))


"child full_time employee class inherit employee behavior"
class FullTimeEmployee(Employee):
    "implementing constructor"
    def __init__(self,id, name, department, salary, balance=0 ,isEmployed=True):
        "intiating parent class constructer"
        Employee.__init__(self,id, name, department, salary, balance=0, isEmployed=True)
    "raise to increase salary by 10% default or by user input"
    def giveRaise(self,salraise=10):
        "increasing salary by 10 percent"
        self.emp_salary=self.emp_salary+self.emp_salary*salraise/100
    



"child part_time employee class inherit employee behavior"
class PartTimeEmployee(Employee):
    "constuctor to create parttime employee"
    def __init__(self,id, name, department, salary, balance=0,isEmployed=True):
        "intiating parent class constructer"
        Employee.__init__(self,id, name, department, salary, balance=0, isEmployed=True)
        
    "raise to increase salary by 5% default or by user input"
    def giveRaise(self, salraise=5):
        "increasing salary by 5 percent"
        self.emp_salary=self.emp_salary+self.emp_salary*salraise/100

