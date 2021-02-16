class Employee:
    company_name ="My King Burger"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        return Employee.company_name + " staff:" + self.name


class Cashier(Employee):

    raise_percentage =  1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0 ):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        if Cashier.burger_price > money_received:
            print("Not enough money")
            return money_received

        else:
            self.number_sold +=1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return  Cashier.company_name + " cashier: " + self.name


# Employee 인스턴스들 생성
employee_1 = Employee("성태호", 7000)
employee_2 = Employee("강영훈", 6500)

# Cashier 인스턴스 생성
cashier = Cashier("김대위", 9000)

# 생성한 모든 직원 인스턴스들을 리스트에 추가
employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier)

# 모든 직원들의 시급 인상
for employee in employee_list:
    employee.raise_pay()


# 모든 직원들의 총 시급 구하기
total_wage = 0


for employee in employee_list:
    total_wage += employee.wage


for employee in employee_list:
    print (employee)


print(total_wage)




