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
player_items = [{'item': potion, 'quantity': 5},
                {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5},
                {'item': elixir, 'quantity': 5},
                {'item': megaelixir, 'quantity': 5},
                {'item': gerenade, 'quantity': 1}]

player = Person('Valos', 460, 65, 60, 34, player_spells, player_items)
player2 = Person('Nick', 500, 65, 60, 34, player_spells, player_items)
player3 = Person('Robot', 880, 65, 60, 34, player_spells, player_items)
players = [player, player2, player3]

enemy = Person('Enemy', 1900, 65, 45, 25, [], [])

running = True
while running:
    print(40*'=', '\n\n')
    # print HP and MP for players
    for player in players:
        print(f'{bcolors.OKGREEN}{player.get_stats()}{bcolors.ENDC}')

    # print HP and MP for enemy
    print(f'{bcolors.FAIL}{enemy.get_stats()}{bcolors.ENDC}\n')

    for player in players:
        player.choose_action()

        choice = input('Choose Action: ')
        if not choice.isnumeric():
            continue
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

            item = player.get_item(item_choice)

            # reduce quantity by one
            if not player.use_item(item_choice):
                print(f'{bcolors.FAIL}\nYou already used all of this item...{bcolors.ENDC}')
                continue

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + f'\n{item.name} heals {item.prop} points of HP' + bcolors.ENDC)

            elif item.type == 'elixir':
                if item.name == 'MegaElixir':
                    for p in players:  # fully restore all of party members HP/MP
                        p.heal(p.get_max_hp())
                        p.add_mp(p.get_max_mp())

                    print(f'{bcolors.OKGREEN}\n{item.name} fully restores HP/MP for all party members{bcolors.ENDC}')

                elif item.name == 'Elixir':
                    player.heal(player.get_max_hp())  # fully heal player
                    player.add_mp(player.get_max_mp())  # fully restore mp
                    print(f'{bcolors.OKGREEN}\n{item.name} fully restores HP/MP{bcolors.ENDC}')

            elif item.type == 'attack':
                enemy.take_damage(item.prop)
                print(f'{bcolors.FAIL}\n{item.name} deals {item.prop} points of damage{bcolors.ENDC}')

        else:  # invalid choice
            continue

        # enemy attacks
        enemy_choice = 1
        if enemy_choice == 1:  # always true for now
            dmg = enemy.generate_damage()
            player.take_damage(dmg)
            print(f'Enemy attacked for {dmg} points of damage.')

        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
            running = False
        elif player.get_hp() == 0:
            print(bcolors.FAIL + 'Enemy has defeated you!' + bcolors.ENDC)
            running = False

