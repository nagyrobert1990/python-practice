import os

command = input("Please specify a command [list, add, mark, archive]: ")

def list_items():
    print ("You saved the following to-do items:")
    with open("todo_list.txt", "r") as f:
        for i, line in enumerate(f):
            print('{}. {}'.format(i+1, line.strip()))

def add_item():
    f = open("todo_list.txt","a")
    add = input("Add an item: ")
    f.write("[ ] " + str(add) + "\n")
    f.close()
    print("Item added.\n")

def marking():
    print ("You saved the following to-do items:")
    with open("todo_list.txt", "r") as f:
        for i, line in enumerate(f):
            print('{}. {}'.format(i+1, line.strip()))
    markedLine = int(input("Which one you want to mark as completed: "))

    f = open("todo_list.txt","r")
    lines = f.readlines()
    markedLine = markedLine-1

    mark1= "[ ]"
    mark2= "[x]"

    lines = open('todo_list.txt').read().splitlines()
    lines[markedLine] = (lines[markedLine].replace(mark1, mark2))
    open('todo_list.txt','w').write('\n'.join(lines))

    print ("Learn Python is completed")

def archiveing():
    marked = ['[x]']
    with open('todo_list.txt') as oldfile, open('todo_list_temp.txt', 'w') as newfile:
        for line in oldfile:
            if not any(mark in line for mark in marked):
                newfile.write(line)
    with open("todo_list_temp.txt") as f:
        with open("todo_list.txt", "w") as f1:
            for line in f:
                f1.write(line)
    os.remove("todo_list_temp.txt")
    print("All completed tasks got deleted.")

if (command == "list"):
    list_items()

elif (command == "add"):
    add_item()

elif (command == "mark"):
    marking()

elif (command == "archive"):
    archiveing()

else:
    print("$hit maaan!")