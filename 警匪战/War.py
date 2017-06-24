# encoding = 'utf-8'
import threading
import random
import time
# 武器
class Weapon():
    def __init__(self, name, force, blood):
        self.name = name
        self.force = force;
        self.blood = blood
        print('吾乃绝世武器  ' + name + '  吾以尘封商店多年愿追随一位白富美的妹子')


# 所有角色的父类
class Role(threading.Thread):
    def __init__(self, name, blood, weapon=Weapon('蜀山剑', 50, 10000), force=0, baseForce=20):
        threading.Thread.__init__(self)
        self.weapon = weapon
        self.force = force
        self.baseForce = baseForce
        self.blood = blood
        self.name = name
        print('我出生了，我没名字，但是我有一个武器，武器的名字是  ' + weapon.name)

    def setBlood(self, blood):
        self.blood = blood

    def getBlood(self):
        return self.blood

    def run(self):
        pass

    # 指定攻击对象
    def attack(self, role):
        f = self.force
        if f > 10:
            f = f - 10
        hurt = random.randint(f, self.force + 10)
        print(role.name + '我要用  ' + role.weapon.name + '  打你了一下就掉  ' + str(hurt) + '  点血，你怕不怕,怕就投降吗大家都是朋友')
        role.setBlood(role.getBlood() - hurt)
        if role.getBlood() <= 0:
            print(role.name + '哈哈，叫你嚣张挂了吧')

    def setName(self, name):
        self.name = name;

    def getName(self):
        return self.name

    def setWeapon(self, weapon):
        self.weapon = weapon
        self.force = self.baseForce + weapon.force
        print('骚年选择我是对的，吾乃极品武器  ' + weapon.name + '  攻击力' + str(weapon.force))


# 警察
class Policy(Role):
    def __init__(self, blood, name, weapon=Weapon('蜀山剑', 50, 10000), force=0, baseForce=20):
        Role.__init__(self, name, blood, weapon, force)

    def setBlood(self, blood):
        Role.setBlood(blood)

    def run(self):
        while True:
            size = len(robbers)
            index = random.randint(0, size - 1)
            enemy = robbers[index]
            self.attack(enemy)
            time.sleep(1)

    def setName(self, name):
        Role.setName(self, name)
        print('我的名字是: ' + name + ' ,我是笨蛋警察')


# 土匪
class Robber(Role):
    def __init__(self, blood, name, weapon=Weapon('加特林', 50, 10000), force=0, baseForce=20):
        Role.__init__(self, name, blood, weapon, force)
        # def setBlood(self, blood):
        #    Role.setBlood(blood)

    def setName(self, name):
        Role.setName(self, name)
        print('我的名字是: ' + name + ' ,我是聪明的土匪')

    def run(self):
        while True:
            size = len(policys)
            index = random.randint(0, size - 1)
            enemy = robbers[index]
            self.attack(enemy)
            time.sleep(1)


def purchaseWeapon(role, store, index):
    if index < len(store.weapons) and index > 0:
        role.setWeapon(store.weapons[index])
    else:
        print('穷鬼滚蛋，这种渣渣武器我们这种大商场怎么可能卖')


# 商店，出售武器，修复武器
class Store():
    def __init__(self, weapons):
        self.weapons = weapons


weapons = [Weapon('绝世好贱', 123, 12345), Weapon('屠龙刀', 123, 12345), Weapon('方天画戟', 123, 12345)]
policys = [Policy(12344, '李白'), Policy(12344, '杜甫'), Policy(12344, '苏轼')]
robbers = [Robber(123123, '土匪座山雕'), Robber(2131241, '山口组大佬'), Robber(123123, '红星十三妹')]


def main():
    store = Store(weapons)
    for p in policys:
        purchaseWeapon(p, store, random.randint(0, len(weapons)))
        p.start()

    for r in robbers:
        purchaseWeapon(r, store, random.randint(0, len(weapons)))
        r.start()


main()
