from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item


# create black magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

# create white magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 18, 200, 'white')

# create items
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hipotion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'Fully restores HP/MP of one party member', 99999)
megaelixir = Item('MegaElixir', 'elixir', "Fully restores party's HP/MP", 99999)

gerenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)


# instantiate people
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, megaelixir, gerenade]
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

print(bcolors.FAIL + bcolors.BOLD + 'ENEMY ATTACKS!' + bcolors.ENDC)

running = True
while running:
    print(40*'=')
    player.choose_action()

    choice = input('Choose Action: ')
    index = int(choice)-1

    if index == 0:  # attack
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attacked for {dmg} points of damage.')

    elif index == 1:  # magic
        player.choose_magic()
        magic_choice = int(input('Choose Magic: ')) - 1

        # if player enters 0 we go back to menu
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()

        # no magic point
        if current_mp < spell.cost:
            print(bcolors.FAIL + '\nNot Enough MP' + bcolors.ENDC)
            continue

        # deal magic damage/heal
        player.reduce_mp(spell.cost)
        if spell.type == 'white':  # heal
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + f'\n{spell.name} heals {magic_dmg} points of HP' + bcolors.ENDC)
        elif spell.type == 'black':  # damage
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + f'\n{spell.name} deals {magic_dmg} points of damage' + bcolors.ENDC)

    elif index == 2:  # item
        player.choose_item()
        item_choice = int(input('Choose Item: ')) - 1

        # if player enters 0 we go back to menu
        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolors.OKGREEN + f'\n{item.name} heals {item.prop} points of HP' + bcolors.ENDC)

    else:  # invalid choice
        continue

    # enemy attacks
    enemy_choice = 1
    if enemy_choice == 1:  # always true for now
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(f'Enemy attacked for {dmg} points of damage.')

    # print HP
    print(40*'-')
    print(f'{bcolors.FAIL}Enemy HP: {enemy.get_hp()}/{enemy.get_max_hp()}{bcolors.ENDC}\n')
    print(f'{bcolors.OKGREEN}Player HP: {player.get_hp()}/{player.get_max_hp()}{bcolors.ENDC}')
    print(f'{bcolors.OKBLUE}Your MP: {player.get_mp()}/{player.get_max_mp()}{bcolors.ENDC}\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'Enemy has defeated you!' + bcolors.ENDC)
        running = False

