from abc import ABC, abstractclassmethod


class Department:
    # Department class: Stores department name and code
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    # Employee class: A abstract class for inheritance

    # Constants for our Employees
    WORKLOAD = 8
    PERCENTAGE_BONUS = 0.15

    def __init__(self, code, name, salary, department):
        """
        Employee class constructor:
            - Employee code {int}
            - Name {string}
            - Salary {float}
            - Department (Protected) {department class}
        """
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractclassmethod
    def calc_bonus(self):
        # Computes the bonus for the month - Abstract method
        pass

    @classmethod
    def get_hours(cls):
        # Returns work hours - Class method
        return cls.WORKLOAD

    def get_department(self):
        # Returns Department name
        return self.__department.name

    def set_department(self, departament_name):
        # Changes department name if needed
        self.__department.name = departament_name


class Manager(Employee):
    def __init__(self, code, name, salary):
        """
        Manager class constructor (Inherits from Employee):
            - Employee code {int}
            - Name {string}
            - Salary {float}
            - Department (Protected) {department class}
        """
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        # Computes Bonus - Uses the Employee class method
        return self.salary * Employee.PERCENTAGE_BONUS


class Seller(Employee):
    def __init__(self, code, name, salary):
        """
        Seller class constructor (Inherits from Employee):
            - Employee code {int}
            - Name {string}
            - Salary {float}
            - Department (Protected) {department class}
        """
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        # Computes Bonus - Uses the Employee class method
        return self.__sales * Employee.PERCENTAGE_BONUS

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        # Adding a new sale to the total
        self.__sales += sale
