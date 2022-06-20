# Counters
screen_one_counter = 0
screen_two_counter = 0
question_counter = 0
quit_check = 0

# Score
score = 0

# Questions list
questions = ["What is the capital of france?\n"
             "1) Paris\n"
             "2) Melbourne\n"
             "3) Berlin",
             
             "What is a young cat called?\n"
             "1) Puppy\n"
             "2) Kitten\n"
             "3) Calf",
             
             "What do bees make?\n"
             "1) Jam\n"
             "2) Chocolate\n"
             "3) Honey"]

# Welcome menu
while screen_one_counter == 0:
    if quit_check == 1:
        quick_check = 0
        break
    
    print("Welcome to the Quiz Game!")
    I1 = input("Press any key to continue...")
    if I1 == "":
        screen_one_counter = 1
        print("\n" * 100)
        break
    else:
        screen_one_counter = 1
        print("\n" * 100)
        break

# Main menu
while screen_one_counter == 1 and screen_two_counter == 0:
    score = 0
    question_counter = 0
    print("Please select from the following options:")
    I2 = input( "1) Help Menu\n"
                "2) Play Game\n"
                "3) Exit\n")

    while I2 == "1":
        I4 = input("\n" * 100 + "Select 1, 2 or 3 as options for the menu and questions.")
        if I4 == "":
            print("\n" * 100)
            break
        else:
            print("\n" * 100)
            break

    while I2 == "2":
        if question_counter == 4:
            break
        if question_counter == 0:
            print("\n" * 100 + questions[0])
            I3 = input("Please select an option...")
            if I3 == "1":
                score += 1
                question_counter = 1
                print("\n" * 100 + "Correct!\n")
                continue
            else: 
                question_counter = 1
                print("\n" * 100 + "Incorrect.\n")
                continue

        if question_counter == 1:
            print(questions[1])
            I3 = input("Please select an option...")
            if I3 == "2":
                score += 1
                question_counter = 2
                print("\n" * 100 + "Correct!\n")
                continue
            else: 
                question_counter = 2
                print("\n" * 100 + "Incorrect.\n")
                continue
        
        if question_counter == 2:
            print(questions[2])
            I3 = input("Please select an option...")
            if I3 == "3":
                score += 1
                question_counter = 3
                print("\n" * 100 + "Correct!\n")
                continue
            else: 
                question_counter = 3
                print("\n" * 100 + "Incorrect.\n")
                continue
        if question_counter == 3:
            print("Your score is {}\n".format(score))
            question_counter = 4
            break

    if I2 == "3":
        quick_check = 1
        print( "\n" * 100 + "Thanks for playing!")
        break
