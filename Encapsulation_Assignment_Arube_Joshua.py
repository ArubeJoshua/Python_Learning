class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def _salary_increment(self):
        check = False
        while not check:
            try:
                increment = float(
                    input("Enter increment percentage (e.g., 0.5, 1, 10)  : ")
                )
                self._salary += self._salary * (increment / 100)
                check = True
            except ValueError:
                print("Wrong input. Please enter a valid increment percentage.")


employees = [Employee("Mike", 250000), Employee("James", 150000)]

print("------------Welcome to salary increment system----------------")
for emp in employees:
    print(emp._name + " with salary", emp._salary)
    emp._salary_increment()
    print("*")
    print(emp._name + "'s new salary is ---->>>>", emp._salary)
    print("------------------------------------------------------------------")
