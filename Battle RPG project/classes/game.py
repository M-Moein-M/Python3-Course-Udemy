import random
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.items = items
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def add_mp(self, mp):
        self.mp += mp
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0

    def get_item(self, index):
        return self.items[index]['item']

    def use_item(self, index):  # reduce item quantity by one and return True. Return False if item quantity was 0
        if self.items[index]['quantity'] == 0:
            return False
        else:
            self.items[index]['quantity'] -= 1
            return True

    # actions
    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + '\nACTIONS' + bcolors.ENDC)
        for item in self.actions:
            print(f'\t{i}. {item}')
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + '\nMAGIC' + bcolors.ENDC + '(enter 0 to go back to menu)')
        for spell in self.magic:
            print(f'\t{i}. {spell.name}(cost: {spell.cost})')
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + '\nITEMS' + bcolors.ENDC + '(enter 0 to go back to menu)')
        for item in self.items:
            item, quantity = item['item'], item['quantity']
            print(f'\t{i}. {item.name}(x{quantity}): {item.description}')
            i += 1

    def get_stats(self):
        inspace = 20  # line initial space
        hp_bars = 25
        mp_bars = 15

        p_hp_bars = math.ceil(self.get_hp()/self.get_max_hp()*hp_bars)  # number of player hp bars to show
        p_mp_bars = math.ceil(self.get_mp()/self.get_max_mp()*mp_bars)  # number of player mp bars to show

        return f"{bcolors.BOLD}{self.name[:inspace]}" \
            f"{(inspace-len(self.name))*' ' if len(self.name) < inspace else ''}" \
            f"  {self.get_hp()}/{self.get_max_hp()} |{p_hp_bars*'█'}" \
            f"{(hp_bars-p_hp_bars)*' '}|" \
            f"  {self.get_mp()}/{self.get_max_mp()} |{p_mp_bars*'█'}" \
            f"{(mp_bars-p_mp_bars)*' '}|"
