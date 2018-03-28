import random

def newgame():
    inventory = []
    budget = 100

    
    load = input("Do you want to load game? y/n")
    if load == "y":
        with open("save_file.txt","r") as fl:
            if fl:
                with open("save_file.txt","r") as fl:
                    lines = fl.readlines()
                    inventory = lines[1].split(',')
                    del inventory[-1]
                    budget = lines[0]
            else:
                print("You dont have a saved game!")
                newgame()
                

    elif load == "n":
        pass
    else:
        print("Invalid command!")
        newgame()   

    if not inventory:
        print("Your inventory is empty!\n")
    else:
        print(inventory,"\n")    

    print("Tis is how much cash you have right now :" , (budget),"$\n")     

    choice = input("Difficulty :\n[E]: Easy\n[M]: Medium\n[H]: Hard\n\n[C]: Cheat \n[Q]: Quit to Menu \n")
    if  choice == ("e"):
        print("Easy mod is selected (for newcomers)!\n")
    elif choice == ("m"):
        print("Normal mod is selected (for casual gamblers)!\n")
    elif choice == ("h"):
        print("Hard mod selected (only for advanced highrollers and reclusive masterminds)!\n")
    elif choice == ("q"):
        main()  
    elif choice == ("c"):
        code = input("Type in the code bruh!")
        if code == "cool":
            print("You're rich dude!")
            budget = int(budget) + 900
            print("This is how much you have right now: ",budget,"$\n")
        else:
            print("This is not the code man")
            newgame()       
    else:
        print("Invalid command!")
        newgame()

    while True:
                    
        try:    
            bet = int(input("Game starting! How much cash you want to bet?\n"))
        except ValueError:
            print("Invalid command!")
            continue
        
        guess = int(input("Which one contains the red?\n 1    2     3\n[ ]  [ ]   [ ]\n"))

        num = random.randint(1,3)

        print(num)

        if guess == num:
            print("You won!!")
            if choice == ("e"):
                budget = (int(budget) + (bet*2))
            elif choice == ("m"):
                budget = (int(budget) + bet)
            elif choice == ("h"):
                budget = (int(budget) + (bet/2))
            elif choice == ("c"):
                budget = (int(budget) + bet)    
            print("This is how much money you have right now :",budget,"$\n")    
        
        else:
            print("You lost:(")
            budget = (int(budget) - bet)
            print("This is how much money you have right now :",budget,"$\n")

        common_loot_list = ['cat','puppy','slime','shovel','ladder','mushroom','clover','soup square','tram ticket']
        epic_loot_list = ['horn','minigun','lucky charm','natural beard','flame thrower','codecool brooch','tank','battleship','irish dwarf','gold']
        legendary_loot_list = ['dragon','ifinity gloves','magic staff','deathstar','unicorn','supernova','kriptonit','mjolnir','palantir','horcrux']

        wanna_loot_box = input("Want to open a lootbox? y/n\n")

        if wanna_loot_box == "y":
            lootbox = int(input("Which lootbox you chose?\n[1] Common_lootbox [25$]\n[2] Epic_lootbox [100$]\n[3] Legendary_lootbox [200$]\n"))

            if lootbox == 1:
                if budget < 25:
                    print("You cant afford that! Try again in your new game!\n")
                    continue
                else:
                    pass
                loot = common_loot_list[random.randint(0,9)]
                budget = budget - 25
                print ("Congratulations! You've got a\n",loot)
                inventory.append(loot)
            elif lootbox == 2:
                if budget < 100:
                    print("You cant afford that! Try again in your new game!\n")
                    continue
                else:
                    pass
                loot = epic_loot_list[random.randint(0,9)]
                budget = budget - 100
                print ("Congratulations! You've got a\n",loot)
                inventory.append(loot)
            elif lootbox == 3:
                if budget < 200:
                    print("You cant afford that! Try again in your new game!\n")
                    continue
                else:
                    pass
                loot = legendary_loot_list[random.randint(0,9)]
                budget = budget - 200
                print ("Congratulations! You've got a\n",loot)
                inventory.append(loot)
            else:
                print ("Invalid command!")
            print ("Inventory: ", inventory)
        elif wanna_loot_box == "n":
            pass
        else:
            ("This is not a valid option!")
            pass
   
        save = input("Do you want to save? y/n\n")

        if save == ("y"):
            with open("save_file.txt","w") as f:
                f.write(str(budget) + "\n")
                for i in range(0,len(inventory)):
                    f.write("%s," % inventory[i])
            print ("Game saved!")  
        elif save == ("n"):
            pass
        else:
            print("Invalid command!")
            continue
        
        regame = input("Do you want to play again? y/n\n")
        if regame == "y":
            print("New game!")
        elif regame == "n":
            main()    
        else:
            print("Invalid command!")
            main()

        if budget <= 0:
            print("You are out of bucks, Game Over! (returning to main menu)")
            main()     
def info():
    print("Someday you walk in the concrete jungle, and hear some noise.\nYou get a closer look at it and suddenly a gipsy appears and says:\nHere is the red, where is the red, genyó!\nYou breathe slowly, take all your power and say: ZSÁMÓ!\nExperience the best rpg card game of your life;\nExplore the infinite features and collectibles;\nBe welcomed in this magficient world!\n\n[*][*][*]In Pursuit Of The Red[*][*][*]\n")

                
def main():
 choice = input("Hi there! Welcome to the InPursuitOfRed! With numbers you can choose :\n[1] New Game\n[2] Info\n[3] Quit\n")
 if choice == "1":
     newgame()
 elif choice == "2":
     info()
     main()
 elif choice == "3":
     quit()
 else:
     print("This is not a valid command!")
     main()    
main()
