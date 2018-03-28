def savegame(user_name,budget,inventory):
    with open("%s_save_file.txt" %user_name,"w") as f:
        f.write(str(budget)+ "\n")
        for i in range(0,len(inventory)):
            f.write("%s," % inventory[i])
    print ("Game saved!")

user_name = "maki"
budget = 200
inventory = ['unicorn','pear','duck tape','crown']
savegame(user_name,budget,inventory)