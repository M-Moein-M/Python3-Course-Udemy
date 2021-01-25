from classes.game import bcolors, Person


magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
         {'name': 'Thunder', 'cost': 10, 'dmg': 80},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

print(bcolors.FAIL + bcolors.BOLD + 'ENEMY ATTACKS!' + bcolors.ENDC)

running = True
while running:
    print(40*'=')
    player.choose_action()

    choice = input('Choose Action: ')
    index = int(choice)-1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attacked for {dmg} points of damage. Enemy HP: {enemy.get_hp()}')

    # enemy attacks
    enemy_choice = 1
    if enemy_choice == 1:  # always true for now
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(f'Enemy attacked for {dmg} points of damage. Player HP: {player.get_hp()}')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'Enemy has defeated you!' + bcolors.ENDC)
        running = False

