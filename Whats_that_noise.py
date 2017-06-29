GameOn = True

while GameOn:
    option = input("You are laying in your bed when you hear a noise downstairs. Do you go investigate? Yes or No?" )
    if not option:
        exit()
    if option == "Yes":
        Weapon = input("Ahh! There is a monster in your kitchen! What weapon will you use? A wooden spoon or frying pan?")
        if Weapon == "Wooden spoon":
            action1 = input("The monster feels threatened. Do you want to try to reason with it or fight?")
            if action1 == "reason with it":
                print ("Oh no! The monster ate you!")
            elif action1 == "fight":
                    print ("You take your chances and win!")

        elif Weapon == "frying pan":
            hideaction = input("You wack the monster in the head and temporarily stun it. Where will you run and hide? Bathroom or Closet?")
            if hideaction == "Bathroom":
                    action2 = input("You lock the door. Will you stay and try to find a weapon or jump out the window? Weapon or jump?")
                    if action2 == "Weapon":
                            action3 = input("Blowdryer or cup of water?")
                            if action3 == "cup of water":
                                    print ("The water dissolves the monster and kills it. You win!")
                            elif action3 == "Blowdryer":
                                    action4 = input("The hot air angers the monster and it bites you. You need to act quick. Fight, Escape, or Tend to your wounds?")
                                    if action4 == "Fight":
                                            print ("The monster is stronger. You die.")
                                    elif action4 == "Escape":
                                            print ("You escaped the monster. You win!")
                                    elif action4 == "Tend to your wounds":
                                            print ("You tried to get to the med kit but it's too late!")
                    if action2 == "jump":
                        action5 = input("You open the window and jump out, but you get stuck in the tree. Emergency services come and rescue you. Do you tell them about the monster? Yes or No?")
                        if action5 == "Yes":
                            print ("They investigate the house and find nothing. They conclude that you are delusional, but at least you are safe from the monster!")
                        elif action5 == "No":
                            print ("The monster comes outside and eats everyone.")

            elif hideaction == "Closet":
                print ("The monster sniffed you out and ate you!")

    if option == "No":
        print ("Oh no! A monster came up the stairs and ate you!")
