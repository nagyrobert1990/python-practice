def loadgame(user_name):
    inventory = []
    with open("%s_save_file.txt" % user_name,"r") as fl:
        lines = fl.readlines()
        inventory = lines[1].split(',')
        del inventory[-1]
    budget = lines[0].rstrip()
    return budget,inventory