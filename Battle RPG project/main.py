from classes.game import bcolors, Person


magic = [{'name': 'Fire', 'cost': 10, 'dmg': 100},
         {'name': 'Thunder', 'cost': 10, 'dmg': 124},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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

        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()

        if current_mp < cost:
            print(bcolors.FAIL + '\nNot Enough MP' + bcolors.ENDC)
            continue

        else:
            player.reduce_mp(cost)
            magic_dmg = player.generate_spell_damage(magic_choice)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + f'\n{spell} deals {str(magic_dmg)} points of damage' + bcolors.ENDC)

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

