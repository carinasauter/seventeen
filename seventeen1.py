import random


def check_human_input(number, marbles_left):
    # checks if human input is 1, 2 or 3 and that it is never more than the marbles that are left
    # If that is not the case, the check will prompt the user for a new input
    # until all conditions are fulfilled.
    lst = ["1", "2", "3"]
    while str(number) not in lst or int(number) > marbles_left:
        print("Sorry, that is not a valid option. Try again!")
        status_prompt(marbles_left)
        number = input(
            "\nYour turn: How many marbles will you remove (1-3)? ")
        number = check_human_input(number, marbles_left)
    return int(number)


def check_computer_input(number, marbles_left):
    # checks if the computer-generated number is ok in case there are few marbles left.
    # Otherwise, will repeat generation of random number until condition is met
    while number > marbles_left:
        number = random.randint(1, 3)
        continue
    return number


# helper function to print the status prompt across the game
def status_prompt(marbles_left):
    print("Number of marbles left in jar: {}".format(marbles_left))


def seventeen():
    print("\n\nLet's play the game of Seventeen!")
    marbles_left = 17  # marbles initiated at 17
    status_prompt(marbles_left)
    while marbles_left > 0:  # loop is entered until no marbles left
        user_input =  input(
            "\nYour turn: How many marbles will you remove (1-3)? ")
        user_input = check_human_input(
            user_input, marbles_left)  # user input sent to check
        print("You removed {} marbles.".format(user_input))  # feedback to user
        marbles_left -= user_input
        if marbles_left > 0:
            status_prompt(marbles_left)
            print("\nComputer's turn...")
            random_number = random.randint(1, 3)
            random_number = check_computer_input(
                random_number, marbles_left)  # random number sent for check
            marbles_left -= random_number
            print("Computer removed {} marbles.".format(random_number))
            if marbles_left > 0:
                status_prompt(marbles_left)
        else:
            print("There are no marbles left. Computer wins!")
            exit()
    print("There are no marbles left. You win!")


def main():  # CALL YOUR FUNCTION BELOW
    seventeen()

if __name__ == '__main__':
    main()
