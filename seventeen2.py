import random


def get_next_move(line, n):
    # taking the next position of the line which indicates the next move of
    # player 1
    next_move = line[n]
    return next_move


def get_next_game(input_file):
    # reading the next line and capturing it in a list so we can go through it
    # number by number
    line = input_file.readline()
    line = line.strip().split(",")
    return line



def save_game_to_file(file, game_number, play_sequence, winner):
    # writing game result to file
    file.write("Game #{}. Play sequence: {}. Winner: {}\n".format(
        game_number, play_sequence, winner))


def check_human_input(number, marbles_left):
    # checks if human input is never more than the marbles that are left
    # If that is not the case, all remaining marbles will be taken
    if int(number) > marbles_left:
        return marbles_left
    else:
        return int(number)


def seventeen2():
    input_file = open("i206_placein_input.txt", "r")  # opening input file
    # open/create output file
    output_file = open("i206_placein_output2_carinasauter.txt", "w")
    # initialize game values
    game_number = 0
    number_wins_1 = 0
    number_wins_2 = 0
    line = "!"  # initializing the line to something so that it will enter the while loop
    while line != []:
        line = get_next_game(input_file)  # starting new game
        if line == ['']:  # check if we are out of game input -
            # if there are no more lines with input then the list will contain
            # an empty string
            break
        # initializing round specific values
        game_number += 1
        round = 0
        marbles_left = 17  # marbles initiated at 17
        play_sequence = ""

        while marbles_left > 0:  # loop is entered until no marbles left
            user_input = get_next_move(line, round)
            user_input = check_human_input(
                user_input, marbles_left)  # user input sent to check
            marbles_left -= user_input
            play_sequence = play_sequence + str(user_input)
            if marbles_left == 0:  # check if game is over
                winner = "P1"
                number_wins_1 += 1
                save_game_to_file(output_file, game_number,
                                  play_sequence, winner)
                break
            round += 1
            random_number = random.randint(1, 3)  # computer generates input
            random_number = check_computer_input(
                random_number, marbles_left)  # computer move sent to check
            marbles_left -= random_number
            play_sequence = play_sequence + "-" + str(random_number) + "-"
        else:
            play_sequence = play_sequence + "-" + str(random_number)
            winner = "P2"
            number_wins_2 += 1
            save_game_to_file(output_file, game_number, play_sequence, winner)
    output_file.write("Player 1 won {} times; Player 2 won {} times.".format(
        number_wins_1, number_wins_2))
    input_file.close()
    output_file.close()
    exit()


def check_computer_input(number, marbles_left):
    # checks if the computer-generated number is ok in case there are few marbles left.
    # Otherwise, will repeat generation of random number until condition is met
    while number > marbles_left:
        number = random.randint(1, 3)
        continue
    return number


def main():  # CALL YOUR FUNCTION BELOW
    seventeen2()


if __name__ == '__main__':
    main()
