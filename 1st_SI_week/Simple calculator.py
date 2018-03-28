while True:
    try:
        number1 = int(raw_input("Enter a number (or a letter to exit): "))
        operation = raw_input("Enter an operation: ")
        number2 = int(raw_input("Enter another number: "))
    except ValueError:
        print("Have a nice day!")
        break
    if (operation == "+"):
        result = int(number1) + int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "-"):
        result = int(number1) - int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "*"):
        result = int(number1) * int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "/"):
        result = int(number1) / int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "%"):
        result = int(number1) % int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "**"):
        result = int(number1) ** int(number2)
        print("Result: " + str(result) + "\n")
    elif (operation == "//"):
        result = int(number1) // int(number2)
        print("Result: " + str(result) + "\n")
    else:
        print("It's not an operation.\nTry again!")