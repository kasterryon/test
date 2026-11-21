class Plants:
    def __init__(self,name,hp,cost):
        self.name=name
        self.hp=hp
        self.cost=cost

    def take_damage(self,damage):
        self.hp-=damage
        if self.hp<=0:
            print(f"{self.name}被吃干净了一个")
        else:
            print(f"{self.name}剩余血量：{self.hp}")

class AttackPlant(Plants):
    def __init__(self,name,hp,cost,damage,attack_text):
        super().__init__(name,hp,cost)
        self.damage=damage
        self.attack_text=attack_text
    def attack(self,zombie):
        print(f"{self.name}{self.attack_text}，造成了{self.damage}点伤害")
        zombie.take_damage(self.damage)

class ResourcePlant(Plants):
    def __init__(self,name,hp,cost,sun_amount,produce):
        super().__init__(name,hp,cost)
        self.sun_amount=sun_amount
        self.produce_text=produce

    def produce_sun(self):
        print(f"{self.name}{self.produce_text}，生产了{self.sun_amount}点阳光")
        return self.sun_amount

class Zombie:
    def __init__(self,name,hp,damage=10):
        self.name=name
        self.hp=hp
        self.damage=damage

    def take_damage(self,damage):
        self.hp-=damage
        if self.hp<=0:
            print(f"{self.name}死了一个")
        else:
            print(f"{self.name}剩余血量: {self.hp}")

    def attack(self, plant):
        print(f"{self.name}啃{plant.name}")
        plant.take_damage(self.damage)


class Pea(AttackPlant):
    def __init__(self):
        super().__init__("豌豆射手",150,100,20,"发射出一颗豌豆")

class PeaSnow(AttackPlant):
    def __init__(self):
        super().__init__("寒冰射手", 100, 175, 20, "发射出一颗冰豌豆")

class Sunflower(ResourcePlant):
    def __init__(self):
        super().__init__("向日葵", 100, 50, 25, "生产了阳光")


if __name__=="__main__":
    sunflower=Sunflower()
    pea=Pea()
    peaSnow=PeaSnow()
    zombie=Zombie("普通僵尸",50)
    print("————资源生产ing————")
    sunflower.produce_sun()

    print("————战斗！！！————")
    while zombie.hp>0:
        pea.attack(zombie)