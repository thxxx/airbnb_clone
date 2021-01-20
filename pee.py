class Dog:
    def __init__(self):
        print("woof")

    def pee(self):
        print("i am powerful")


class Puppy(Dog):
    def pee(self):
        print("Wwaaaaaa")
        super().pee() # 부모클래스의 method


dogg = Puppy()
dogg.pee()