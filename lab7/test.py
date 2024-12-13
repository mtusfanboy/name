class Employee:
    def __init__(self, id_employee, name, *args):
        self.__id_employee = id_employee
        self.__name = name

    def get_info(self):
        return f"id - {self.__id_employee} name - {self.__name}"

    def __str__(self):
        return f"Employee: {self.get_info()}"


class Manager(Employee):
    def __init__(self, id_employee, name, department, *args):
        super().__init__(id_employee, name, *args)
        if not department:
            raise ValueError("Укажите отдел")
        self.__department = department

    def get_info(self):
        return super().get_info() + f" department - {self.__department}"

    def manage_project(self):
        return f"Manage project - {self.__department}"

    def __str__(self):
        return f"Manager: {self.get_info()}"


class Technical(Employee):
    def __init__(self, id_employee, name, specialization, *args):
        super().__init__(id_employee, name, *args)
        if not specialization:
            raise ValueError("Укажите специальность")
        self.__specialization = specialization

    def get_info(self):
        return super().get_info() + f" specialization - {self.__specialization}"

    def perform_maintenance(self):
        return f"Performing maintenance - {self.__specialization}"

    def __str__(self):
        return f"Technical: {self.get_info()}"


class TechManager(Manager, Technical):
    def __init__(self, id_employee, name, department, specialization):
        super().__init__(id_employee, name, department, specialization)
        self.__team = []

    def add_employee(self, data):
        if not issubclass(data, Employee):
            raise ValueError(
                "Неверный тип данных. Объект должен иметь тип Employee")
        self.__team.append(data)


tm = TechManager(12, "sdf", "12", "programmer")
print(tm)
