from random import randint
from time import sleep
import os

round = 1
score1 = 0
score2 = 0

dice1 = """ 
    ╔═════════╗
    ║         ║
    ║    ■    ║
    ║         ║
    ╚═════════╝
"""
dice2 = """ 
    ╔═════════╗
    ║      ■  ║
    ║         ║
    ║  ■      ║
    ╚═════════╝
"""
dice3 = """ 
    ╔═════════╗
    ║      ■  ║
    ║    ■    ║
    ║  ■      ║
    ╚═════════╝
"""
dice4 = """ 
    ╔═════════╗
    ║  ■   ■  ║
    ║         ║
    ║  ■   ■  ║
    ╚═════════╝
"""
dice5 = """ 
    ╔═════════╗
    ║  ■   ■  ║
    ║    ■    ║
    ║  ■   ■  ║
    ╚═════════╝
"""
dice6 = """ 
    ╔═════════╗
    ║  ■   ■  ║
    ║  ■   ■  ║
    ║  ■   ■  ║
    ╚═════════╝
"""
kruze1 = """
      ╔══════╗   
     ║        ║              
    ║          ║
    ║          ║
    ║          ║
    ╚══════════╝
                   
"""
kruze2 = """


      ╔══════╗   
     ║        ║              
    ║          ║
    ║          ║
    ║          ║
    ╚══════════╝
"""
a = True
while a:
    print('''
    ___                                                       
    (  _`\  _                                                  
    | | ) |(_)   ___    __        __     _ _   ___ ___     __  
    | | | )| | /'___) /'__`\    /'_ `\ /'_` )/' _ ` _ `\ /'__`\\
    | |_) || |( (___ (  ___/   ( (_) |( (_| || ( ) ( ) |(  ___/
    (____/'(_)`\____)`\____)   `\__  |`\__,_)(_) (_) (_)`\____)
                            ( )_) |                         
                                \___/'                         
        ''')
    skaits = int(input('''
Ja gribat vienu spēletāju, tad ievadiet: 1
Ja gribat divus spēletājus, tad ievadiet: 2
Ja gribat iziet, uzspežiet enter

ievadiet spēletaju skaitu:
'''))
    if skaits == 1:
        print("Viena spēletāja režims")
        a = False
    elif skaits == 2:
        print("Divu spēletāja režims")
        a = False
    else:
        print("kļūda, nepareizi ievadīts simbols")
        sleep(1)
    os.system("cls")


while True:
    print(round,"raunds!")
    os.system("pause")
    dice = randint(1,6)
    for x in range(7):
        print(kruze1)
        sleep(0.2)
        os.system("cls")
        print(kruze2)
        sleep(0.2)
        os.system("cls")
    if dice == 1:
        print(dice1)
    elif dice == 2:
        print(dice2)
    elif dice == 3:
        print(dice3)
    elif dice == 4:
        print(dice4)
    elif dice == 5:
        print(dice5)
    elif dice == 6:
        print(dice6)
    player1 = dice


    if skaits == 1:
        os.system("cls")
        print("Dators met kauliņus")
        sleep(2)
    else:
        os.system("pause")
        
    dice = randint(1,6)
    for x in range(7):
        print(kruze1)
        sleep(0.2)
        os.system("cls")
        print(kruze2)
        sleep(0.2)
        os.system("cls")
    if dice == 1:
        print(dice1)
    elif dice == 2:
        print(dice2)
    elif dice == 3:
        print(dice3)
    elif dice == 4:
        print(dice4)
    elif dice == 5:
        print(dice5)
    elif dice == 6:
        print(dice6)
    player2 = dice

    if player1 > player2:
        round = round + 1
        score1 = score1 + 1
        print("šaja raunda uzvareja 1.spēletajs")
    elif player1 < player2:
        round = round + 1
        score2 = score2 + 1
        print("šaja raunda uzvareja 2.spēletajs")
    else:
        print("Neizķirst, raunds sāksies no jauna")

    print(score1,":",score2)
    sleep(2)
    os.system("cls")
    if score1 == 2:
        break
    elif score2 == 2:
        break

if score1 > score2:
    print("Uzvareja 1.spēletajs")
else:
    print("Uzvareja 2.spēletajs")


# Krūzes animacija
""""

for x in range(7):
    print(kruze1)
    sleep(0.2)
    os.system("cls")
    print(kruze2)
    sleep(0.2)
    os.system("cls")
"""
    
# Veidošana un kauliņu izvadišana

"""
dice = randint(1,6)
if dice == 1:
    print(dice1)
elif dice == 2:
    print(dice2)
elif dice == 3:
    print(dice3)
elif dice == 4:
    print(dice4)
elif dice == 5:
    print(dice5)
elif dice == 6:
    print(dice6)
"""
input()