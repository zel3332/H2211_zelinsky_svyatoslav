import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladnes = 50
        self.progres = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progres += 0.12
        self.gladnes -= 5

    def to_sleep(self):
        print("i will sleep")
        self.gladnes += 3

    def to_shill(self):
        print("rest time")
        self.gladnes += 5
        self.progres -= 0.1

    def is_alive(self):
        if self.progres < -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladnes < 0:
            print("deprssion")
            self.alive = False
        elif self.progres > 5:
            print(" passed externlly...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladnes = {self.gladnes}")
        print(f"progres = {self.progres}")

    def live(self, day):
        day = f"Day {day} of {self.name} live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_shill()
        self.end_of_day()
        self.is_alive()


personage = Student(name="???")

for day in range(365):
    if personage.alive == False:
        break
    personage.live(day)
