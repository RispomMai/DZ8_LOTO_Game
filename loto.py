import random
from loto_classes import Player, Card,  Keg
N = 2
players = {}


def print_card(player_number):
    print(f"====== Карточка игрока {player_number} ======")
    stroka = list(players[player_number].card.numbers.keys())
    s1 = stroka[0:5]
    s1.sort()
    s2 = stroka[5:10]
    s2.sort()
    s3 = stroka[10:15]
    s3.sort()
    stroka = s1 + s2 +s3
    iii = 0
    for i in range(0, 27):
        if i == 9 or i == 18:
            print("")
        if players[player_number].card.pattern[i]:
            key = stroka[iii] ###       key = list(players[player_number].card.numbers)[ii]
            if players[player_number].card.numbers.get(int(key)):
                print(f" \033[4m{key}\033[0m ",end = "")
            else:
                print(f" {key} ", end="")
            iii += 1
        else:
            print("   ",end = "")
    print("")
    print(f"="*31,"\n")


while True:
    print('1. Определите игроков')
    print('2. начинаем игру')
    print('3. выход')

    choice = input('Выберите пункт меню ')

    if choice == '1':
        quantity_players = int(input("Введите количество игроков : "))
        for i in range(0,quantity_players):
            players[i] = Player()
            print(f"{i} - игрок. Определите кто будет играть. 0 - человек, 1 - компьютер",end = "")
            if input() == "0" : players[i].human = False
        for i in range(0,quantity_players):
            print_card(i)
        print("")
    elif choice == '2':
        keg = Keg()
        raund = 1
        while True:
            print("Раунд",raund)
            number = keg.pull_keg()
            print("Номер - ",number)
            for i in range(0, quantity_players):
                print_card(i)
                if players[i].check(number):
                    print(f"{i} игрок выиграл")
                    break
            if players[i].check(number):
                break
            raund += 1


    elif choice == '3':
        break
    else:
        print('Неверный пункт меню')
"""
            if(players[i].human):
                print(i, " игрок - человек")
            else:
                print(i, " игрок - компьютер")

"""
