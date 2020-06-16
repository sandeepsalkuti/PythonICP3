class Employee:                                         #Parent class
    countemp=0
    ls=[]                                               #defining empty list to add each income salary
    def __init__(self,name,family,salary,department):    #default constructor
        self.name=name
        self.family=family
        self.salary=salary
        self.ls.append(salary)
        self.department=department
    def avrg(self):
        sumcount=0
        Employee.countemp =Employee.countemp + 1        #incrementing employee count each time method gets executed
        for sal in self.ls:
            sumcount=sumcount + sal
        avrg=sumcount/Employee.countemp                 #counting average of salaries
        print("salary is",avrg)
class Fulltimeemployee(Employee):                        #child class inherits parent class
    def __init__(self,name,family,salary,department):
        super().__init__(name,family,salary,department)   #using super method inheriting parent class constructor
    def avrg(self):
        super().avrg()
a=Employee("sandeep","four",3000,"IT")                     #creating instance to parent class and passing values
a.avrg()                                                   #calling method of parent class
b=Fulltimeemployee("san","four",8000,"IT")                 #creating instance to child class and passing values
b.avrg()                                                   #calling method of child class which inherits from parent class



