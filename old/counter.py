class Counter:

    def __init__(self, limit):
        self.val = 0
        self.limit= limit

    def tick(self):
        self.val +=1
        if self.val >= self.limit :
            self.val = 0
            return True
        else:
            return False

    def set (self, new_val):
        if 0<new_val < self.limit :
            self.val = new_val
        else:
            self.val=0


    def __str__(self):
        return str(self.val).zfill(2)

counter = Counter (30)

print ("1 to 5")
for i in range(5):
    counter.tick()
    print(counter)

print("set to 0")
counter.set(0)
print(counter)

print("set to 27")
counter.set(27)
print(counter)


print ("30 to 0")
for i in range(5):
    counter.tick()
    print(counter)

print("set to 77")
counter.set(77)
print(counter)

