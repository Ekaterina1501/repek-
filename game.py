import random

class Warrior:
    name = ""
    hp = 0
    att = 0
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(100, 150)
        self.att = random.randint(20, 30)
    def hitpoint(self):
        return self.hp
    def attack(self):
        return self.att
    def getdamage(self, damage):
        if self.hp - damage > 0:
            self.hp -= damage
            return '{} получил {} урона. Осталось {} здоровья.'.format(self.name, damage, self.hp)
        else:
            self.hp = 0
            return '{} получил {} урона и погиб.'.format(self.name, damage)

class WarriorWithShield(Warrior):
    defense = 0
    def __init__(self, name):
        Warrior.__init__(self, name)
        defense = random.randint(5, 10)
    def getdamage(self, damage):
        if self.hp - damage + self.defense > 0:
            self.hp = self.hp - damage + self.defense
            return '{} получил {} урона. Осталось {} здоровья.'.format(self.name, damage, self.hp )
        else:
            self.hp = 0
            return '{} получил {} урона и погиб.'.format(self.name, damage)

class ExpertWarrior(Warrior):
    wer = 0
    def __init__(self, name):
        Warrior.__init__(self, name)
        self.wer = random.random()
    def attack(self):
        if self.wer <= 0.2:
            return self.att * 2
        else:
            return self.att

hero1 = Warrior('Igor')
hero2 = WarriorWithShield('Petya')
hero3 = ExpertWarrior('Kolya')

print('Урон первого воина: ', hero1.attack() )
print('Урон второго воина: ', hero2.attack() )
print('Урон третьего воина: ', hero3.attack() )

#2 бой между двумя войнами
while True:
    if hero2.hitpoint() <= 0:
        print(hero1.name, 'победил')
        break
    hero2.getdamage(hero1.attack())
    if hero1.hitpoint() <= 0:
        print(hero2.name, 'победил')
        break
    hero1.getdamage(hero2.attack())

#3 бой между армиями
army1 = [hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10] = \
    [Warrior("Один"), Warrior("Два"), Warrior("Три"), Warrior("Четыре"), WarriorWithShield("Пять"),
     WarriorWithShield("Шесть"), WarriorWithShield("Семь"), WarriorWithShield("Восемь"), ExpertWarrior("Девять"),
     ExpertWarrior("Десять")]
army2 = [hero11, hero12, hero13, hero14, hero15, hero16, hero17, hero18, hero19, hero20] = \
    [Warrior("Одиннадцать"), Warrior("Двенадцать"), Warrior("Тринадцать"), Warrior("Четырнадцать"),
     WarriorWithShield("Пятнадцать"), WarriorWithShield("Шестнадцать"), WarriorWithShield("Семнадцать"),
     WarriorWithShield("Восемнадцать"), ExpertWarrior("Девятнадцать"), ExpertWarrior("Двадцать")]

k = 1
while True:
    if army1 == []:
        print('Вторая армия победила')
        break
    elif army2 == []:
        print('Первая армия победила')
        break
    else:
        sl1 = random.randint(0, len(army1)-1)
        sl2 = random.randint(0, len(army2)-1)
        while True:
            if k % 2 == 0:
                army1[sl1].getdamage(army2[sl2].attack())
                if army1[sl1].hitpoint() <= 0:
                    del army1[sl1]
                    break
                army2[sl2].getdamage(army1[sl1].attack())
                if army2[sl2].hitpoint() <= 0:
                    del army2[sl2]
                    break
            else:
                army2[sl2].getdamage(army1[sl1].attack())
                if army2[sl2].hitpoint() <= 0:
                    del army2[sl2]
                    break
                army1[sl1].getdamage(army2[sl2].attack())
                if army1[sl1].hitpoint() <= 0:
                    del army1[sl1]
                    break
    k+=1