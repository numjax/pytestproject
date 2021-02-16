class Clock :

    def __init__(self, hh, mm, ss):

        hour = Counter(24)
        min = Counter(60)
        sec = Counter(60)

        hour.set(hh)
        min.set(mm)
        sec.set(ss)

        self.hh = hour
        self.mm = min
        self.ss = sec



    def tick(self):
        if self.ss.tick() :
            if self.mm.tick() :
                self.hh.tick()



    def set(self, hh, mm, ss):
        self.hh.set(hh)
        self.mm.set(mm)
        self.ss.set(ss)


    def __str__(self):
        return str(self.hh) + ":" + str(self.mm) + ":" + str(self.ss)



class Counter:

    def __init__(self, limit):
        self.val = 0
        self.limit= limit

    def tick(self):
        self.val += 1
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




# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)



# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)