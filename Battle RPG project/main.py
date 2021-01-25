from classes.game import bcolors, Person
from classes.magic import Spell


# create black magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

# create white magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 18, 200, 'white')


# instantiate people
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()

        if current_mp < spell.cost:
            print(bcolors.FAIL + '\nNot Enough MP' + bcolors.ENDC)
            continue

        else:
            player.reduce_mp(spell.cost)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + f'\n{spell.name} deals {str(magic_dmg)} points of damage' + bcolors.ENDC)

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

