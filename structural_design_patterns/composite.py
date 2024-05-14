"""
    Composite
    Composite pattern lets clients treat the individual objects in the composite 
    structure uniformly.
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, name:str ,salary:float) -> None: pass
    @abstractmethod
    def getName(self) -> str: pass
    @abstractmethod
    def setSalary(self, salary:float) -> None: pass
    @abstractmethod
    def getSalary(self) -> float: pass
    @abstractmethod
    def getRoles(self) -> list: pass
    

class Developer (Employee):
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        
    def getName(self) -> str:
        return super().getName()
    
    def setSalary(self, salary: float) -> None:
        self.salary = salary
    
    def getSalary(self) -> float:
        return self.salary
    
    def getRoles(self) -> list:
        return super().getRoles()
    

class Designer (Employee):
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        
    def getName(self) -> str:
        return super().getName()
    
    def setSalary(self, salary: float) -> None:
        self.salary = salary
    
    def getSalary(self) -> float:
        return self.salary
    
    def getRoles(self) -> list:
        return super().getRoles()

class Organization:
    def __init__(self) -> None:
        self.employees = []
    
    def addEmployee(self, employee: Employee) -> None:
        self.employees.append(employee)
        
    def getNetSalary(self) -> float:
        total_salary = sum(emp.getSalary() for emp in self.employees)
        return total_salary

if __name__ == "__main__":
    john = Developer("John", 10000)
    jane = Designer("Jane", 12000)

    organization = Organization()
    organization.addEmployee(john)
    organization.addEmployee(jane)
    
    print("Net Salary:", organization.getNetSalary())
