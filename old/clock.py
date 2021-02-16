class Clock :

    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm =mm
        self.ss =ss

    def tick(self):
        self.ss+=1

    def set(self, hh, mm, ss):
        self.hh = hh
        self.mm =mm
        self.ss =ss
    def __str__(self):
        return str(self.hh).zfill(2) +  ":" + str(self.mm).zfill(2)+ ":" +str(self.ss).zfill(2)


clock = Clock(3,25,44)

print(clock)


clock.set(2,35,11)

print(clock)


for i in range(15):
    clock.tick()

print(clock)