# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    money = 0
    foods = 0
    fur_coat = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'Денег - {}, еды - {}, грязи - {}'.format(
            self.money, self.food, self.dirt)


class Man(House):
    def __init__(self, name):
        super().__init__()
        self.House = home
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happiness)

    def pet_the_cat(self):
        self.fullness += 5


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        self.House.dirt += 5
        # noinspection PyChainedComparisons
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
        elif self.happiness <= 0:
            cprint('{} умер от депрессии'.format(self.name), color='red')
        elif self.House.money <= 350 and self.fullness >= 15:
            self.work()
        elif self.fullness < 15 and self.House.food > 0:
            self.eat()
        elif self.happiness <= 10 and self.fullness >= 10:
            self.gaming()
        elif self.House.dirt > 90:
            self.happiness -= 10

    # noinspection DuplicatedCode,PyStatementEffect
    def eat(self):
        x = randint(5, 30)
        if x < self.House.food:
            self.fullness += x
            self.House.food -= x
            House.foods += x
        else:
            self.fullness += self.House.food
            self.House.food == 0
            House.foods += self.House.food
        cprint('{} поел'.format(self.name), color='blue')

    def work(self):
        self.fullness -= 10
        self.House.money += 150
        House.money += 150
        cprint('{} поработал'.format(self.name), color='blue')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} поиграл'.format(self.name), color='blue')


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
        elif self.happiness <= 0:
            cprint('{} умер от депрессии'.format(self.name), color='red')
        elif self.fullness <= 10 and self.House.food > 0:
            self.eat()
        elif self.House.dirt > 150:
            self.clean_house()
        elif self.House.food < 20 and self.fullness >= 10:
            self.shopping()
        elif self.happiness <= 20 and self.House.money >= 350:
            self.buy_fur_coat()
        elif self.House.dirt > 90:
            self.happiness -= 10

    # noinspection DuplicatedCode,PyStatementEffect
    def eat(self):
        y = randint(5, 30)
        if y < self.House.food:
            self.fullness += y
            self.House.food -= y
            House.foods += y
        else:
            self.fullness += self.House.food
            self.House.food == 0
            House.foods += self.House.food
        cprint('{} поела'.format(self.name), color='blue')

    def shopping(self):
        z = randint(5, 30)
        self.House.food += z
        self.House.money -= z
        self.fullness -= 10
        cprint('{} сходила в магазин'.format(self.name), color='blue')

    def buy_fur_coat(self):
        self.House.money -= 350
        self.happiness += 60
        self.fullness -= 10
        House.fur_coat += 1
        cprint('{} купила шубу'.format(self.name), color='blue')

    def clean_house(self):
        self.House.dirt -= 100
        self.fullness -= 10
        cprint('{} убралась в доме'.format(self.name), color='blue')

    def buy_cat_food(self):
        o = randint(5, 30)
        self.cat_food += o
        self.House.money -= o



home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
cprint('Всего заработано {}'.format(House.money), color='green')
cprint('Всего съедено еды {}'.format(House.foods), color='green')
cprint('Всего куплено шуб {}'.format(House.fur_coat), color='green')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.happiness = None

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
        elif self.fullness <= 10 and self.House.cat_food > 0:
            self.eat()
        elif self.fullness >= 30:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        i = randint(1, 10)
        self.fullness += i * 2
        self.House.cat_food -= i

    def sleep(self):
        self.fullness -= 10

    def soil(self):
        self.fullness -= 10
        self.House.dirt += 5



######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self):
        super().__init__(name=name)
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
        elif self.fullness <= 10 and self.House.food > 0:
            self.eat()
        else:
            self.sleep()

    # noinspection DuplicatedCode
    def eat(self):
        p = randint(5, 10)
        if p < self.House.food:
            self.fullness += p
            self.House.food -= p
            House.foods += p
        else:
            self.fullness += self.House.food
            # noinspection PyStatementEffect
            self.House.food == 0
            House.foods += self.House.food
        cprint('{} поел'.format(self.name), color='blue')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='blue')


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
