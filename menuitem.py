class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return "{} price: {}" .format(self.name, self.price)


berger= MenuItem("burger",1000)
coke = MenuItem("coke",500)
fries = MenuItem("fries", 800)

print(berger)
print(coke)
print(fries)