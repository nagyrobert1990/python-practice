def display_inventory(inv):

    for k,v in inv.items():
        print(v,k)
    print("Total number of items:", sum(inv.values()))

def add_to_inventory(inv, added_items):

    for i in range(0,len(added_items)):
        if inv.get(added_items[i]) != None :
            inv[added_items[i]] += 1
        else:
            inv[added_items[i]] = 1
    return(inv)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)