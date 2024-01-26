#Galactic Guessing Game

#importing modules
import random as rd
import time as tm

#defining functions


def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print("Game starts in ", i, "seconds...")
        tm.sleep(1)


def main():
    delay_seconds = 3
    print("\nGet ready! The game will start", delay_seconds, "seconds...")
    countdown_timer(delay_seconds)
    # Game start
    print("Game started! \n")


def reminder(step, n_trial):
    print("Guess a number from", step)
    print("You have", n_trial, "trials \n")


def reg(lin):
    lin = lin.lower()
    lin = lin.strip()
    return lin


def greetings():
    name = input("What's your name? ")
    print(name, "welcome to the Galactic Guessing Game ")
    tm.sleep(5)
    print("\n")
    print(
        "In the distant future, you are an intrepid astronaut on a mission to explore the far reaches of the galaxy.\n"
        "During your space journey, your spaceship's navigation system encounters a mysterious anomaly.\nTo navigate "
        "through this anomaly and continue your quest, you must decipher the correct coordinates within a limited "
        "number of attempts."
        "\nThe coordinates are represented by random numbers based on the chosen difficulty level.\nThe success of your"
        " mission depends on your ability to guess these coordinates accurately.\nAs you progress through different "
        "difficulty levels, you face increasingly complex navigational challenges."
        "\nCan you successfully navigate through the cosmic coordinates and unveil the secrets hidden within the "
        "anomaly?"
        "\nYour score reflects the efficiency of your navigation skills. Good luck, Space Explorer!")

    tm.sleep(10)
    print("\n")
    print("Choose level of difficulty...\nSimple\nRegular\nChallenging\n")


def calculate_score(steps, attempts_left):
    if steps == "simple":
        return attempts_left * 10
    elif steps == "regular":
        return attempts_left * 25
    elif steps == "challenging":
        return attempts_left * 30


def get_input():
    try:
        return int(input("What is your guess? \nEnter it: "))
    except ValueError:
        print("Invalid input .")
        return get_input()


while True:
    #initializing the game
    greetings()
    level = input("Enter the difficulty level: ")
    lvl = reg(level)
    while lvl not in ["simple", "regular", "challenging"]:
        print('Invalid game mode. Please enter a valid game mode ("simple", "regular" , "challenging").')
        lvl = input("Enter the difficulty level: ")
        lvl = reg(lvl)

    #Number of trials
    if lvl == "simple":
        trial = 3
    elif lvl == "regular":
        trial = 4
    elif lvl == "challenging":
        trial = 5

    #constants based on difficulty level
    s_guesser = rd.randint(0, 5)
    r_guesser = rd.randint(0, 10)
    c_guesser = rd.randint(0, 15)

    #preparing game
    main()
    # Initialize score variable
    score = 0

    # simple mode
    if lvl == "simple":
        s_guessed = None
        reminder("0 - 5", trial)
        while trial > 0 and s_guessed != s_guesser:
            s_guessed = get_input()
            if s_guessed == s_guesser:
                print("You guessed right!")
                score = calculate_score(lvl, trial)
                print("Your score:", score,)
            else:
                print("Try again. Attempts left:", trial - 1)
            trial -= 1

            if score == 50 and s_guesser == s_guessed:
                print("\nCorrect coordinates acquired...")
            elif score < 50 and s_guesser == s_guessed:
                print("\nAcquiring coordinates ...")
                tm.sleep(5)
                print("correct coordinates acquired ...")

    # Regular mode
    if lvl == "regular":
        r_guessed = None
        reminder("0 - 10", trial)
        while trial > 0 and r_guessed != r_guesser:
            r_guessed = get_input()
            if r_guessed == r_guesser:
                print("You guessed right!")
                score = calculate_score(lvl, trial)
                print("Your score:", score, )
            else:
                print("Try again. Attempts left:", trial - 1)
            trial -= 1

        if score == 100 and r_guesser == r_guessed:
            print("\nCorrect coordinates acquired... \nAnomaly corrected... \nNavigation system functioning at 70% ")
        elif score < 100 and r_guesser == r_guessed:
            print("\nAcquiring coordinates ...")
            tm.sleep(3)
            print("correct coordinates acquired ...")
            tm.sleep(2)
            print("Navigation system functioning at 60%")

    #Challenging mode
    if lvl == "challenging":
        c_guessed = None
        reminder("0 - 20", trial)
        while trial > 0 and c_guessed != c_guesser:
            c_guessed = get_input()
            if c_guessed == c_guesser:
                print("You guessed right!")
                score = calculate_score(lvl, trial)
                print("Your score:", score, )
            else:
                print("Try again. Attempts left:", trial - 1)
            trial -= 1

        if score == 150 and c_guesser == c_guessed:
            print("\nCorrect coordinates acquired... \nAnomaly corrected... \nNavigation system functioning at 100% ")
        elif score < 150 and c_guesser == c_guessed:
            print("\nAcquiring coordinates ...")
            tm.sleep(3)
            print("correct coordinates acquired ...")
            tm.sleep(2)
            print("Navigation system functioning at 90%")

    play_again = input("To Quit games press 'Q' or press any other key to continue: \n>>>")
    play_again = reg(play_again)
    if play_again == "q":
        break
 