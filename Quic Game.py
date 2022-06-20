# For loop for questions
#
# Initial Menu
# Main Menu
# Questions/Help/Exit 
# End screen with score

screen_one_counter = 0
screen_two_counter = 0
question_counter = 0

score = 0

questions = ["What is the capital of france?\n"
             "1) Paris"
             "2) Melbourne"
             "3) Berlin",
             
             "What is a young cat called?\n"
             "1) Puppy"
             "2) Kitten"
             "3) Calf",
             
             "What do bees make?"
             "1) Jam"
             "2) Chocolate"
             "3) Honey"]

while screen_one_counter == 0:
    print("Welcome to the Quiz Game!")
    I1 = input("Press any key to continue...")
    if I1 == "":
        screen_one_counter = 1
        break
    else:
        screen_one_counter = 1
        break

while screen_one_counter == 1 and screen_two_counter == 0:
    print("Please select from the following options:")
    I2 = input( "1) Help Menu\n"
                "2) Play Game\n"
                "3) Exit")
    if I2 == "1":
        print("Help menu")
    while I2 == "2":
        if question_counter == 0:
            print(questions[0])
            I3 = input("Please select an option...")
            if I3 == "1":
                score += 1
                question_counter = 1
                print("Correct!")
                continue
            else: 
                question_counter = 1
                print("Incorrect.")
                continue

        if question_counter == 1:
            print(questions[1])
            I3 = input("Please select an option...")
            if I3 == "2":
                score += 1
                question_counter = 2
                print("Correct!")
                continue
            else: 
                question_counter = 2
                print("Incorrect.")
                continue
        
        if question_counter == 2:
            print(questions[2])
            I3 = input("Please select an option...")
            if I3 == "3":
                score += 1
                question_counter = 3
                print("Correct!")
                continue
            else: 
                question_counter = 3
                print("Incorrect.")
                continue
        if question_counter == 3:
            print("Your score is {}".format(score))
            question_counter = 0
            break

    if I2 == "3":
        break
    else:
        continue