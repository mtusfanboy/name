class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"{self.name=}, {self.id=}"


class Manager(Employee):
    def __init__(self, name, id, department, *args, **kwargs):
        super().__init__(name, id, *args, **kwargs)
        self.department = department

    def get_info(self):
        return super().get_info() + f" {self.department=}"

    def manage(self):
        return f"Manager - {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization, *args, **kwargs):
        super().__init__(name, id, *args, **kwargs)
        self.specialization = specialization

    def get_info(self):
        return super().get_info() + f" {self.specialization=}"

    def maintenance(self):
        return f"Maintenance - {self.maintenance}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department=None, specialization=None, *args, **kwargs):
        super().__init__(name, id, department, specialization, *args, **kwargs)
        self.team = []

    def add_employee(self, data):
        self.team.append(data)

    def get_team_info(self):
        return self.team


emp = TechManager("Azbek", 1, "IT", "Tester")

print(emp.get_info())

emp.add_employee(Employee("Jzamshut", 2))
emp.add_employee(Manager("Ashot😎", 3, "Uborshik🪣"))

for i in emp.get_team_info():
    print(i.get_info())
