class Employee:

    company_name = "My King Burger"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name  = name
        self.wage = wage

    def raise_pay(self):
        self.wage *= self.raise_percentage

    def __str__(self):
        return Employee.company_name + " staff: " +self.name

class DeliveryMan(Employee):

    def __init__(self, name, wage, on_standby):
        super().__init__(name,wage)
        self.on_standby = on_standby


    def delivery (self, address):
        if self.on_standby :
            print("Go to " + address)
            self.on_standby= False
        else:
            print("On delivery")

    def back(self ):
        self.on_standby = True
        print ("Returned from the delivery.")


    def __str__(self):
        return super().company_name + " Delivery Man: " + self.name


terry = DeliveryMan("Terry", 7000, True)

terry.raise_pay()
print(terry.wage)


terry.delivery("9696 Shirley")
terry.delivery("9697 Shirley")

terry.back()

terry.delivery("9697 Shirley")

print(terry)

print(DeliveryMan.mro())