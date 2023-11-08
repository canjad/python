

class Person:
    def __init__(self,name=""):
        self.name=name
    def work(self,money):
        print(self.name,"工作挣了",money)
    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)
zwj=Person("张无忌")
zm=Person("赵敏")
zwj.work(5000)
zm.work(10000)
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"玉女心经")