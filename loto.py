import random
from loto_classes import Player, Keg

def print_card(player_number):
    print(f"====== Карточка игрока {player_number+1} ======")
    line = 0
    for i in range(0, 27):
        if i == 9 or i == 18:
            print("")
        if players[player_number].card.pattern[i]: ### print номер если в шаблоне 1
            key = players[player_number].card.lines[line]
            if players[player_number].card.numbers.get(int(key)):
                print(f" \033[4m{key}\033[0m ",end = "")
            else:
                print(f" {key} ", end="")
            line += 1
        else:
            print("   ",end = "")
    print("")
    print(f"="*31,"\n")

def game_round(end_game):
    print("Раунд", round)
    number = keg.pull_keg()
    print("Номер - ", number)
    for i in range(0, quantity_players):
        print_card(i)
    for i in range(0, quantity_players):
        if players[i].human:
            end_game = round_human(i,number)
        if end_game:
            print(f"\n{i+1} игрок проиграл!\n")
            return True
        if players[i].check(number):
            print(f"\n{i+1} игрок выиграл!\n")
            return True
    return False
def round_human(player_number,number):
    check_number = cross = False
    if players[player_number].card.numbers.get(number) != None:
        check_number = True
    if input(f"{player_number+1} игрок нажмите 'y' чтобы зачеркнуть ") == 'y':
        cross = True
    if cross:
        if check_number:
            players[i].check(number)
            return False
        else:
            return True
    else:
        if check_number:
            return True
    return False
### True - конец игры

players = {}
while True:
    print('1. Определите игроков')
    print('2. Начинаем игру')
    print('3. Выход')

    choice = input('Выберите пункт меню ')

    if choice == '1':
        quantity_players = int(input("Введите количество игроков : "))
        for i in range(0,quantity_players):
            players[i] = Player()
            print(f"{i+1} - игрок. Определите кто будет играть. 0 - человек, 1 - компьютер ",end = "")
            if input() == "1" : players[i].human = False
        for i in range(0,quantity_players):
            print_card(i)
        print("")
    elif choice == '2':
        keg = Keg()
        round = 1
        end_game = False
        while True:
            if game_round(end_game):
                break
            round += 1
    elif choice == '3':
        break
    else:
        print('Неверный пункт меню')

