# - *- coding: utf- 8 - *-

class Employee:
    COMPANY_NAME = "Acme Inc."

    def __init__(self,name, wage):
        self.name = name
        self.wage = wage

    def __str__(self):
        return "Hello my name is {}. I work at {}.".format(self.name, Employee.COMPANY_NAME)

class Cashier(Employee):

    def __init__(self,name, wage, sold_cnt):
        super().__init__(name, wage)
        self.sold_cnt = sold_cnt

    def __str__(self):
        return self.name + " sold " + str(self.sold_cnt)

    def got_order(self):
        self.sold_cnt += 1

class Manager(Employee):
    pass

class Delivery(Employee):

    def __init__(self, name, wage, standby):
        # self.name = name
        # self.wage = wage
        #super 를 사용해서 변경해 보자
        super().__init__(name, wage)
        self.standby = standby

    def delivery_start(self, address):
        if self.standby:
            print ("Go to " + address)
            self.standby = False

        else:
            print ("Can not start the delivery.")

    def delivery_end(self):
        self.standby = True
        print( self.name + " finished the delivery")

    def __str__(self):
        if self.standby:
            return self.name + " is on the delivery."
        else:
            return self.name + " can start the delivery."


class DeliveryCashier(Cashier, Delivery):

    def __init__(self, name, wage, standby, sold_cnt):
        Employee.__init__(self, name, wage)
        self.standby = standby
        self.sold_cnt = sold_cnt

    def __str__(self):
        return Delivery.__str__(self)

deliverycashier1 = DeliveryCashier("Tom", 1500, True, 0)

deliverycashier1.got_order()
deliverycashier1.delivery_start("1212 Penn ave.")
deliverycashier1.delivery_end()

print(deliverycashier1)

print(DeliveryCashier.mro())




