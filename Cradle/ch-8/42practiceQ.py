class Employee:
    def __init__(self, role, departmment, salary):
        self.role = role
        self.department = departmment
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)
        print("department=", self.department)
        print("salary=", self.salary)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name, age)
        super().__init__("Engineer", "IT",  "75,000")

# e1 = Employee("accountant", "finance", "60,000")
# e1.showDetails()
engg1 = Engineer("Tony", 29)
engg1.showDetails()

# make this shit print name and age as well