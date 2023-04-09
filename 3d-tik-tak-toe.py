import random
import time

# Colors
colors = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "purple": "\033[1;35m",
    "cyan": "\033[1;36m",
    "reset": "\033[0m"
}


# insert two names into list
def pName():
    player1 = input("Player 1 please enter your name:")
    player2 = input("Do you want to play against the AI? (y/n)")
    if player2.lower() == "y":
        player2 = "AI"
    else:
        player2 = input("Player 2 please enter your name:")
    players = [player1, player2]
    return players


# random first player
def radPlayer(players):
    cp = random.choice(players)
    return cp


# player's choice:
def choose_w(players):
    x = True
    while x == True:
        opt = [colors["cyan"] + "💧" + colors["reset"], colors["red"] + "🔥" + colors["reset"],
               colors["yellow"] + "☣" + colors["reset"], colors["green"] + "🍄" + colors["reset"]]
        print(f'You can choose from follow:\n 1-{opt[0]}\t2-{opt[1]}\t3-{opt[2]}\t4-{opt[3]}')
        p1chose = int(input(f'{players[0]} Your choice:')) - 1
        p2chose = int(input(f'{players[1]} Your choice:')) - 1
        if p1chose != p2chose:
            sure = input("are you sure? y/n")
            if sure.lower() == "y":
                p1chose = opt[p1chose]
                p2chose = opt[p2chose]
                playerchoice = {players[0]: p1chose, players[1]: p2chose}
                x = False
            else:
                x = True
        else:
            print("CANT BE THE SAME")

    return playerchoice


# change players
def crUser(cp, players):
    if cp == players[0]:
        return players[1]
    else:
        return players[0]


# print board
def create_board():
    tables = [[["", "", ""], ["", "", ""], ["", "", ""]],
              [["", "", ""], ["", "", ""], ["", "", ""]],
              [["", "", ""], ["", "", ""], ["", "", ""]]]
    return tables


# board
def print_board(tables):
    for z in range(3):
        print(f'{colors["yellow"]}===Table {z + 1}==={colors["reset"]}')
        print()
        for x in range(3):
            print(colors["blue"] + "\n+---+---+---+" + colors["reset"])
            print("|", end="")
            for y in range(3):
                print(" ", tables[x][y][z], end=" |")
        print(colors["blue"] + "\n+---+---+---+" + colors["reset"])


# place new move
def move(tables, playerchoice, cp):
    print(f'{colors["purple"]}Now it is {cp} turn{colors["reset"]}')
    x = False
    start_time = time.time()
    while x == False:
        try:
            if cp == "AI":
                newmovec = random.randint(0, 2)
                newmover = random.randint(0, 2)
                newmovet = random.randint(0, 2)
            else:
                newmovec = int(input("Now Choose Column:(1-3 left to right)")) - 1
                newmover = int(input("Now Choose Row:(1-3 up to down)")) - 1
                newmovet = int(input("Now Choose Table:(1-3 left to right)")) - 1
            if newmovec < 0 or newmovec > 2 or newmover < 0 or newmover > 2 or newmovet < 0 or newmovet > 2:
                print("Invalid input. Please enter a number between 1 and 3.")
            elif tables[newmovet][newmover][newmovec] != "":
                print("Already taken, try again")
            else:
                tables[newmovet][newmover][newmovec] = playerchoice[cp]
                print_board(tables)
                x = True
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

            # Update progress bar
            elapsed_time = time.time() - start_time
            progress = int((elapsed_time / 60) * 20)
            print("[" + "#" * progress + " " * (20 - progress) + "]", end="\r")

            # Check if time limit has been reached
            if elapsed_time >= 60:
                print("\nTime's up!")
                return tables

        return tables


##check win
def is_Win(boards, playerchoice, cp):
    # Check for horizontal wins on each table
    for i in range(3):
        for j in range(3):
            if all(boards[i][j][k] == playerchoice[cp] for k in range(3)):
                return True

    # Check for vertical wins on each table
    for i in range(3):
        for k in range(3):
            if all(boards[i][j][k] == playerchoice[cp] for j in range(3)):
                return True

    # Check for diagonal wins on each table
    if all(boards[i][i][i] == playerchoice[cp] for i in range(3)):
        return True

    if all(boards[i][i][2 - i] == playerchoice[cp] for i in range(3)):
        return True

    if all(boards[i][j][i] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][2 - j][i] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][j][j] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][j][2 - j] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    # If none of the above conditions are true, the player hasn't won
    return False


def win_Display():
    print(f"{colors['yellow']}dP   dP   dP dP 888888ba  888888ba   88888888b  888888ba  {colors['reset']}")
    print(f"{colors['red']}88   88   88 88 88    `8b 88    `8b  88         88    `8b {colors['reset']}")
    print(f"{colors['blue']}88  .8P  .8P 88 88     88 88     88 {colors['yellow']}a88aaaa    a88aaaa8P' {colors['reset']}")
    print(f"{colors['blue']}88  d8'  d8' 88 88     88 88     88  88         88   `8b. {colors['reset']}")
    print(f"{colors['green']}88.d8P8.d8P  88 88     88 88     88  88         88     88 {colors['reset']}")
    print(f"{colors['red']}8888' Y88'   dP dP     dP dP     dP  88888888P  dP     dP {colors['reset']}")
    print(f"{colors['yellow']}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{colors['reset']}")


##winners board -how to do file?
def winners_B(cp, winnerdic):
    if cp not in winnerdic:
        winnerdic[cp] = 1
    else:
        winnerdic[cp] += 1
    return winnerdic


def main():
    play_again = True
    while play_again:
        players = pName()
        ans = input(
            f'Players names are: \n===> {players[0]} and {players[1]} <===\n do you want to change name? \n(hint:press y/n)')
        if ans.lower() == "n":
            print("GOOD LUCK")
        else:
            players = pName()
        cp = radPlayer(players)
        print(f'First player to play is:\n=== {cp} ===')
        playerchoice = choose_w(players)
        boards = create_board()
        print_board(boards)
        winnerdic = {}
        while not is_Win(boards, playerchoice, cp):
            boards = move(boards, playerchoice, cp)
            if is_Win(boards, playerchoice, cp):
                win_Display()
                winnerdic = winners_B(cp, winnerdic)
                break
            cp = crUser(cp, players)
            print_board(boards)
        print("== WINNER | WINS ===")
        for key, value in winnerdic.items():
            print(f'{key} | {value}', end=" ")
        play_again = input("\nDo you want to play again? (y/n)").lower() == "y"
    print("Thanks for playing!")


main()