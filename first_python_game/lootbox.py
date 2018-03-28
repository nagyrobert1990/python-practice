def loot_system():

    common_loot_list = ['cat','puppy','slime','shovel','ladder','mushroom','clover','soup square','tram ticket']
    epic_loot_list = ['horn','minigun','lucky charm','natural beard','flame thrower','codecool brooch','tank','battleship','irish dwarf','gold']
    legendary_loot_list = ['dragon','ifinity gloves','magic staff','deathstar','unicorn','supernova','kriptonit','mjolnir','palantir','horcrux']

    lootbox = int(input("Melyik lootbox-ot szeretnéd?\n[1] Common_lootbox\n[2] Epic_lootbox\n[3] Legendary_lootbox\n"))

    if lootbox == 1:
        loot = common_loot_list[random.randint(0,9)]
        budget = budget - 25
        print ("Congratulations! You've got a\n", loot)
        inventory.append(loot)
    elif lootbox == 2:
        loot = epic_loot_list[random.randint(0,9)]
        budget = budget - 100
        print ("Congratulations! You've got a\n", loot)
        inventory.append(loot)
    elif lootbox == 3:
        loot = legendary_loot_list[random.randint(0,9)]
        budget = budget - 200
        print ("Congratulations! You've got a\n", loot)
        inventory.append(loot)
    else:
        print ("rossz paraméter, új játék")

    print ("Inventory: ", inventory)