class GameChar:

    def  __init__(self, name, hp, atk_power):
        self.name = name
        self.hp = hp
        self.atk_power = atk_power


    def is_alive(self):
        if self.hp <= 0 :
            return False
        elif self.hp >0 :
            return True


    def get_attacked(self,another):
        self.hp = self.hp - another.atk_power



    def attack(self,another):
        another.hp = another.hp - self.atk_power


    def __str__(self):
        if not self.is_alive() :
            return "{} died.".format(self.name)
        else :
            return "{} has {} hp left.".format(self.name, self.hp)


jack = GameChar("Jack",200,30)
kim = GameChar("kim",100,50)

jack.attack(kim)
kim.attack(jack)
jack.attack(kim)
kim.attack(jack)
jack.attack(kim)
kim.attack(jack)
jack.attack(kim)

print(jack)
print(kim)