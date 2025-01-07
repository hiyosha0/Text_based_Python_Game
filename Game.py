#Author: Hiyosha Vinupama
#Student-ID - 74004786
#Date: 2021-07-01

import random

#input validations are here 
def stringVal():
    print("string validation")

#This function will handle players progress until he/she reaches to the beach from the sea
def seaToBeach():
    stamina = 100
    health =100
    print(''' Sunday, the 22nd of december, 2024 [7.00 AM]
              ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
              your plane has crashed ✈️
              Now you are in the middle of the sea
              Try to survive and stay alive....  
              Note:
                  *⚠️ read instructions carefully!
              ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖''')
    start = input("press 's' to start  ")
    if start =="s":
        print('''
              +--------------------------------------------------------------+
              now grab your survival backpack 🛍️
              +--------------------------------------------------------------+
              This backpack includes various tools to survive in the island
              ''')
        print()

        resBackPack = input("Do you want to grab the backpack? y/n ")
        if resBackPack =="y":
            print('''You have grabed the back pack
              +--------------------------------------------------------------+
              | items in your backpack                                       |
              +--------------------------------------------------------------+
              1-bottle of water
              1-transmitter 
              1-flashlight
              1-compass
              1-survival-Gun
              1-survival-knife
              +--------------------------------------------------------------+
               you can see an island far from you !
               Now you have two paths to swim to the beach of a island!
               1. south route
               2. west route
              +--------------------------------------------------------------+
            
            
              ''')
            res = input("which path do you want to take? [1/2]")
            if res =="1":
             print('''you took the south route
                +--------------------------------------------------------------+
                watch out ! you are in the sea 🦈
                +--------------------------------------------------------------+
                you faced a shark 🦈 attack! [-10 health, -10 stamina]
                +--------------------------------------------------------------+
                you survived and reached to the beach 🏖️
                
                    
                ''')
            

            elif res =="2":
                print('''you took the west route
                +--------------------------------------------------------------+
                watch out ! you are in the sea 🦈
                +--------------------------------------------------------------+
                no attacks ! [stamina 100, health 100]
                +--------------------------------------------------------------+
                you survived and reached to the beach 🏖️
                ''')
            else:
                print("respond not found")
            if res =="1":
             stamina = stamina - 10
             health = health - 10
            elif res =="2":
             stamina = stamina-5
             health = health
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("your stamina is ⚔️",stamina)
            print("your health is ❤️‍🩹", health)
        else:
            
            print(''' 
             --------------------------------------------------
             You were Attacked by a shark!🦈
            ----------------------------------------------------
                 
                ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
                ▒█░▄▄ █▄▄█ █░▀░█ █▀▀ 　 █░░█ ░█▄█░ █▀▀ █▄▄▀ 
                ▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
            ''')
            return None, None, None
    else:
        print('''          Try Next Time !
        +----------------------------------------------------+
        |                 Survival island!                   |
        +----------------------------------------------------+
              ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
              ▒█░▄▄ █▄▄█ █░▀░█ █▀▀ 　 █░░█ ░█▄█░ █▀▀ █▄▄▀ 
              ▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
        
        ''')    
             
        
    
    
        
    return health, stamina, start
    

# function 02 this will handle the game until the player reaches to the jungle after chalanges
def beachToJungle(health, stamina,start ):
     print('''now you can have two options.
                +--------------------------------------------------------------+
                you can either rest or keep going.
                +--------------------------------------------------------------+
                press r to rest [resting can +5 stamina]
                press g to keep going
                    
                ''')
     rest = input("do you want to rest or keep going?[r/g] :")
     if rest =="r":
          print(''' 
                you rested and entering the jungle🍀🦁!
                ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
                 ''')
          print("your stamina is ⚔️",stamina)
          print("your health is ❤️‍🩹", health)
          print(''' 
          +--------------------------------------------------------------+
          now you have to choose your path to pass the jungle 🍀🦁
          ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
          1. go from the south 
          2.go from the north
          ''')

          stamina = stamina + 5
          print("your stamina is ⚔️",stamina)
          print("your health is ❤️‍🩹", health)
     elif rest =="g":
          print(''' 
                you are entering the jungle🍀🦁!
                ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
                 ''')
          print("your stamina is ⚔️",stamina)
          print("your health is ❤️‍🩹", health)
          print(''' 
          +--------------------------------------------------------------+
          now you have to choose your path to pass the jungle 🍀🦁
          ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
          1. go from the south 
          2.go from the north
          ''')
     pathChoice= input("which path do you want to choose?[1/2]")
     if pathChoice =="1":
          lionHealth =100
          print(''' 
          you are entering to jungle from the south🍀🦁
          ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
          ''')
          print("your stamina is ⚔️",stamina)
          print("your health is ❤️‍🩹", health)
          print()
          print(''' 
          +--------------------------------------------------------------+
          Danger ⚠️ ! Wild Lion is appering !
          +--------------------------------------------------------------+
          you have to fight ⚔️ to survive !
          +--------------------------------------------------------------+
          you have 1-survival gun and 1-survival knife
          +--------------------------------------------------------------+
          ''')
          gun = input(" do you want to shot with gun [y/n]   ")
          if gun == "y":
            lionHealth = lionHealth - 30
            print("you shot the lion with your gun 🔫")
            print("lion's health is now ❤️‍🩹", lionHealth)
            
            print('''
            ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            Danger ⚠️ ! Wild Lion has seen you 👀 !
            ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            you have to fight ⚔️ to survive !
            
            ''')
            
          def menu():
            print("Fight Menu appearing ⚔️")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print()
            print("1. Shot  with gun [-20 lion's health] [-5 of your stamina] [-5 your health] ")
            print("2. Attack with  knife  [-25 lion's health] [-10 your health] [-20 stamina]  ")
            print("3. run away [-80] of your health [-50] your stamina ")
            print("4. ninja-Kick with leg [-15 lion's health] -[20 your health] -[20 your stamina] ")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print()
            choice = int(input("Enter your attack 🗡️ !")) 
            print()
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            return choice
          count = 1
          while lionHealth > 1 and stamina >= 1:
            
            choice = menu()
            if choice == 1:
                lionHealth = lionHealth - 20
                stamina = stamina - 5
                
                print("Lion's health is now ❤️‍🩹 : ",lionHealth)
                print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                print()
                print("Your stamina is ⚔️ : ",stamina)
                print("Your health is ❤️‍🩹 : ",health)
             
            elif choice ==2:
                lionHealth = lionHealth - 25
                health = health - 10
                stamina = stamina - 10
                
                print("Lion's health is now ❤️‍🩹 : ",lionHealth)
                print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                print()
                print("Your stamina is ⚔️ : ",stamina)
                print("Your health is ❤️‍🩹 : ",health)
            elif choice ==3:
                lionHealth = lionHealth
                stamina = stamina - 50
                health = health - 80
                
                print("Lion's health is now ❤️‍🩹 : ",lionHealth)
                print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                print()
                print("Your stamina is ⚔️ : ",stamina)
                print("Your health is ❤️‍🩹 : ",health)
            elif choice ==4:
                lionHealth = lionHealth -15
                stamina = stamina -20
                health = health -20
                
                print("Lion's health is now ❤️‍🩹 : ",lionHealth)
                print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                print()
                print("Your stamina is ⚔️ : ",stamina)  
                print("Your health is ❤️‍🩹 : ",health)


            
            count =count+1

          print("+-----------------------------------------+")
          print()
          print(''' 
                      +--------------------------------------------------------------+
                      Wooh ! you won the battle ⚔️ 🗡️
                      +--------------------------------------------------------------+
                      you are entering the river 🏞️
                      +--------------------------------------------------------------+
                      ''')
          print()

          print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
          print("you are entering the river ")

          print("your stamina is ⚔️",stamina)
          print("your health is ❤️‍🩹", health)
          if stamina and health <0:
              print("➖➖➖➖➖➖➖➖➖➖➖💀➖➖➖➖➖➖➖➖➖➖➖➖➖")
              print()
              print("Game over,lost the battle ☠️⚔️ ")
              print()
              print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
          
     if pathChoice == '2': 
         print('''
         You are entering the jungle from the north 🍀🦁
         ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
         ''')     
         print("your stamina is ⚔️",stamina)
         print("your health is ❤️‍🩹", health)
         print(''' 
         +--------------------------------------------------------------+
           |        you found a Door with a mysterious puzzel🧩      |
         +--------------------------------------------------------------+ 
                you have to crack the puzzel to open the door 🔓
         +--------------------------------------------------------------+
                 use combination  of 3 below to crack the puzzel
                            [@, #, $, %, !, ?]
         +---------------------------------------------------------------+
         you have to input 3 random symbols and one number to open the door 🔓
               eg: $#%
         +----------------------------------------------------------------+
          💀 each wrong guess will reduce your health❤️‍🩹 and stamina⚔️ level.
         ''')
         print()

         
         password = input("Enter your guess: ")
         
         while password != "#$%":
             password = input("Enter your guess:- ")
             health = health - 10
             stamina = stamina - 10
             print("+------------------------------------+")
             print("your stamina is ⚔️",stamina)
             print("your health is ❤️‍🩹", health)
             print()
             if health and stamina <0:
                 print('''          Try Next Time!
                 +----------------------------------------------------+
                 ||                 Survival island!                 ||
                 +----------------------------------------------------+
                      ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
                      ▒█░▄▄ █▄▄█ █░▀░█ █▀▀ 　 █░░█ ░█▄█░ █▀▀ █▄▄▀ 
                      ▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
                 +----------------------------------------------------+
                 ''') 
             print()
             
         print(''' 
            +--------------------------------------------------------------+
                You have successfully cracked the puzzel 🧩
               ''')
         print()
              
        
     return start, stamina, health

#function-03
def jungleToRiver(start, stamina, health):
    print()
    print(''' 
    +--------------------------------------------------------------+
                    you are entering the river 🏞️
    +--------------------------------------------------------------+
          There are two different paths to cross the river
    +--------------------------------------------------------------+
    Please be carefull who you trust in this crutiual time !
    +--------------------------------------------------------------+
    ''')
    print("your stamina is ⚔️",stamina)
    print("your health is ❤️‍🩹",health)
    print()
    print('''
    +--------------------------------------------------------------+
    You met another lost pilot named "DAVE" who have also crossed the jungle🧑‍✈️.
    +--------------------------------------------------------------+
    Dave asks you to join with him and use his boat to cross the river
    ''')
    print()
    trust = input("Do you want to join with Dave and go in PATH 1 👀 ?[y/n]")
    print()
    if trust == "y":
        print(''' 
        +--------------------Path - 01 ---------------------------+
        You have joined with Dave 🧑‍✈️
        +--------------------------------------------------------------+
        Oops! Dave was a fraud and he has stolen your backpack 🎒
        +--------------------------------------------------------------+
        Dave has left you alone in the river 🏞️
         ''')
        print()
        print(''' 
        +--------------------------------------------------------------+
        DANGER ⚠️! Wild Crocodile is appering 🐊☠️! 
        +--------------------------------------------------------------+
        You have no tools to fight 🔫 the crocodile 🐊☠️
       ''')
        print()

        deadAction = input("press 'r' to run away from the crocodile 🐊☠️ ")
        
        if deadAction == "r":
            count =1
            while stamina >0:
                stamina = stamina - 10
                
                print("your stamina is ⚔️",stamina)
                count = count +1
                break
        return None, None, None
            
        
        
        

        
    if trust == "n":
        
        
        print( ''' 
        +------------------------ Path - 02 ---------------------------+
              
                    You have not joined with Dave 🧑‍✈️
        +--------------------------------------------------------------+
                    You discoverd an abandoned boat 🛶 
        +_______________________________________________________________+
              ''')   
        boatStart = input("press 's' to start the boat 🛶 ")
        if boatStart == "s":
            health = health
            stamina = stamina - 20
            print( ''' 
            +--------------------------------------------------------------+
            | You crosses the river and reaching to the mountain 🏔️     |
            +--------------------------------------------------------------+
            |           It's evening and the sun is setting 🌇             |
            +--------------------------------------------------------------+
            ''')
            print()
            print("your stamina is ⚔️", stamina)
            print("your health is ❤️‍🩹", health)
            print()
    
    return start, stamina, health

#function-04
def riverToMountain(stamina, health, start):
    if stamina == None:
        print(''' Game Over ☠️🏝️ ! ''')
        return None, None, None  # Ensure it returns a tuple
    else:
     print(''' 
           +--------------------------------------------------------------+
           Danger ⚠️ it is getting dark 🌇, you have to rest until its morning.
           +--------------------------------------------------------------+
           |   Now you have to fish🎣 and buld a camp to rest 🏕️               |
           ''')
     print()
     fish = input("press 'r' to  and fish 🎣 and get some foods ")
     print()
     if fish == "r":
         health = health +5
         stamina = stamina +5
         print()
         print("your stamina is ⚔️",stamina)
         print("your health is ❤️‍🩹", health)
     print()
     raft = input("press 'b' to build a camp 🏕️ ")
     if raft == "b":
         health = health +10
         stamina = stamina +10
         print()
         print(''' 
         +--------------------------------------------------------------+
           |  You have built a camp 🏕️ and rested until morning 🌇    |
         +--------------------------------------------------------------+
                    Get ready for the next adventure 🏔️
         ''')

        
         print()
         print("your stamina is ⚔️",stamina)
         print("your health is ❤️‍🩹", health)



    


     return  stamina, health, start

#function-05
def moutainToEscape(stamina, health, start):
    if stamina == None:
        print(''' Game Over ☠️🏝️ ! ''')
        return None, None, None  # Ensure it returns a tuple
    else:
        print(''' 
            +--------------------------------------------------------------+
            |                You are climbing the mountain 🏔️              |
            +--------------------------------------------------------------+
            ⚠️ Danger !, there will be danger at the top of the mountain 🏔️
            +--------------------------------------------------------------+
                  you have to use items carefully in your backpack 🎒
            +--------------------------------------------------------------+
                 Make your decissions wisely to escape from the island 🏝️
      ''')
    
    
    def menu (choice):
        print("----------------- Item List -----------------")
        print("1. Flashlight")
        print("2. Survival Knife")
        print("3. Survival Gun")
        print("4. Compass")
        print("5. Transmitter")
        print("-----------------------------")
        choice = int(input(choice))
        return choice
    print()
    
    choice01 = menu("what will you choose to find directions? ")
    if choice01 == 4:
        print(''' 
        +--------------------------------------------------------------+
        You have used the compass to find the directions 🧭
        +--------------------------------------------------------------+
        you are following  3 meters to south and 5 meters to north 🏝️
        ''')
        print()
        choice02 = menu("you need to cut the trees to make a bridge, what will you choose? ")
        if choice02 == 2:
            print(''' 
            +--------------------------------------------------------------+
            You have used the survival knife to cut the trees 🌲🌲
            +--------------------------------------------------------------+
            you have made a bridge and crossed the mountain 🏔️
            ''')
            stamina = stamina -10
            health = health -10
            
            print()
            choice03 = menu("you need catch helicopter signal to escape, what will you choose? ")
            if choice03 == 5:
                print(''' 
                +--------------------------------------------------------------+
                 WOOH ! you recieved a signal from a survival helicopter📡
                +--------------------------------------------------------------+
                Now reply to the signal after decoding it to escape from the island 🏝️
                ''')
                print()
                print("+-----------------------------------------+")
                print(''' 
                        || Transmiter ||
                  |-------------------------
                  |       🔼 signal sent    
                  |------------------------- 
                  |     signal recieved 🔽  
                  |------------------------- 
                  |       %^#$*()))))@#
                  ''')
                print()
                print(''' 
                +--------------------------------------------------------------+
                decode the signal guessing numbers from 1-4
                +--------------------------------------------------------------+
                Each wrong guess will reduce your health and stamina
                        ''')

                print()
                print("+----------------------------------------------+")
                print("your stamina is ⚔️",stamina)
                print("your health is ❤️‍🩹", health)
                list1 = [1, 2, 3, 4, 5]


                
                guess = random.choice(list1)
                user_input = int(input("Enter your guess: "))

                while user_input != guess:
                    user_input = int(input("Enter your guess: "))
                    health = health - 10
                    stamina = stamina - 10
                    print('+---------------------------------------------+')
                    print("your stamina is ⚔️",stamina)
                    print("your health is ❤️‍🩹", health)
                    print('+---------------------------------------------+')
                    print("wrong signal guess, Try again")
                print(guess)
                print(''' 
                +--------------------------------------------------------------+
                        You have successfully decoded the signal 📡
                +--------------------------------------------------------------+
                        signal - hello we are coming to rescue you 🚁
                +--------------------------------------------------------------+
                |                   Congratulations!                           |
                +--------------------------------------------------------------+
                               ░██╗░░░░░░░██╗██╗███╗░░██╗
                               ░██║░░██╗░░██║██║████╗░██║
                               ░╚██╗████╗██╔╝██║██╔██╗██║
                               ░░████╔═████║░██║██║╚████║
                               ░░╚██╔╝░╚██╔╝░██║██║░╚███║
                               ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
                |--------------------------------------------------------------|
                
                ''')                
            else:
                print(''' 
                +--------------------------------------------------------------+
                You have used the wrong tool to catch the signal 📡
                +--------------------------------------------------------------+
                +--------------------------------------------------------------+
                                  GAME OVER ☠️🏝️ ! ''')
                  
                
            
        else:
            print(''' 
            +--------------------------------------------------------------+
            You have used the wrong tool to cut the trees 🌲🌲
            +--------------------------------------------------------------+
            +--------------------------------------------------------------+
                              GAME OVER ☠️🏝️ !
            ''')
            
    else:
        print(''' 
        +--------------------------------------------------------------+
              YOU HAVE LOST THE WAY TO ESCAPE FROM THE ISLAND 🏝️
        +--------------------------------------------------------------+
                              GAME OVER ☠️🏝️ !
         ''')
        
        return  stamina, health, start     
    
    
#here is the welcome message for the player 
print('''➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖🟦➖➖🟦➖🟩🟩🟩🟩➖🟪➖➖➖🟧➖➖➖➖🟥🟥➖➖
➖🟦➖➖🟦➖🟩➖➖➖➖🟪➖➖➖🟧➖➖➖🟥➖➖🟥➖
➖🟦➖➖🟦➖🟩➖➖➖➖🟪➖➖➖🟧➖➖➖🟥➖➖🟥➖
➖🟦🟦🟦🟦➖🟩🟩🟩➖➖🟪➖➖➖🟧➖➖➖🟥➖➖🟥➖
➖🟦➖➖🟦➖🟩➖➖➖➖🟪➖➖➖🟧➖➖➖🟥➖➖🟥➖
➖🟦➖➖🟦➖🟩➖➖➖➖🟪➖➖➖🟧➖➖➖🟥➖➖🟥➖
➖🟦➖➖🟦➖🟩🟩🟩🟩➖🟪🟪🟪➖🟧🟧🟧➖➖🟥🟥➖➖      
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 Welcome to the survival island! 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
''')



def main():
     
    stamina_from_sea, health_from_sea, start = seaToBeach()
    if start == "s":
        stamina_from_jungle, health_from_jungle, start = beachToJungle(stamina_from_sea, health_from_sea, start)
        start, stamina_from_jungle, health_from_jungle = jungleToRiver(stamina_from_jungle, health_from_jungle, start)
        start, stamina_from_river, health_from_river = riverToMountain( stamina_from_jungle, health_from_jungle, start )
        moutainToEscape(start, stamina_from_river, health_from_river)
        
    else:
        # Initialize variables if start is not "s"
        stamina_from_jungle = stamina_from_sea
        health_from_jungle = health_from_sea
        stamina_from_river = stamina_from_jungle
        health_from_river = health_from_jungle

#This is the main function 
main()
