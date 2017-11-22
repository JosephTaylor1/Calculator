while True:
    print ("To add just type add")
    print("To quit just type quit")
    print("To multiply just type multiply")
    user_input = (input("type here: "))

    if user_input == "quit":
        break

    elif user_input == "add":
        numone = float(input("What is your first number? "))
        numtwo = float(input("What is your first number? "))
        print("Your answer is: %d") % (numone + numtwo)

    elif user_input == "multiply":
        numone = float(input("What is your first number? "))
        numtwo = float(input("What is your first number? "))
        print("Your answer is: %d") % (numone * numtwo)

    else:
        print("\nYou didn't type either quit,add or multiply...\n")
