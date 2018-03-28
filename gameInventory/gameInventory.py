from collections import Counter

# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print ("Inventory:")
    for k,v in inventory.items():
        print(v,k)
    print("Total number of items:", sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for i in range(0,len(added_items)):
        if inventory.get(added_items[i]) != None :
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1
    return(inventory)


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    width = (len(max(inventory, key=len)))
    print ("Inventory:")
    print ("{:>{width}}    {:>{width}}".format("count","item name", width=width))
    print ("{:->{width}}----{:->{width}}".format("","", width=width))
    if order == None:
        sortedInventory = inv.items()
    elif order == "count,asc":
        sortedInventory = sorted(inv.items() , key=lambda t : t[1])
    elif order == "count,desc":
        sortedInventory = sorted(inv.items() , key=lambda t : t[1] , reverse=True)
    for value, key in sortedInventory:
        print ("{:>{width}}    {:>{width}}".format(key, value, width=width))
    print ("{:->{width}}----{:->{width}}".format("","", width=width))
    totalInv = 0
    for key in inv:
        totalInv = totalInv + inv[key]
    print ("Total number of items:",totalInv)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename,"r") as importFile:
        inv2memory = importFile.readline()
    inv2memory.split(",")
    added_items = inv2memory.split(",")
    inv = add_to_inventory(inventory, added_items)
    return inv


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, 'w') as invFile:
        tmp=[]
        for i in inventory:
            addList=(str(inventory[i]*[i]))
            tmp.append(addList)
        inv2file = (','.join(tmp).replace("[","").replace("]","").replace("'","").replace(", ",","))
        invFile.write(inv2file)


# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(inv)
print("\t")

inv = add_to_inventory(inv, dragon_loot)

inv = import_inventory(inv)

print_table(inv, "count,desc")

export_inventory(inv)