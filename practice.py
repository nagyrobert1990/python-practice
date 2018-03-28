import operator


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))

print (sorted_inv)

for row in sorted_inv:
    print("{: >20} {: >20}".format(*row))

print("Total number of items:", sum(inv.values()))

my_string = 'she sells seashells by the seashore.'
print(my_string[4:9])