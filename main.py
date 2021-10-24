import random
from os import system, name

import ascii_art as art

def game():
    system('cls') if name == 'nt' else system('clear')
    print(art.logo)

    win_count = 0
    lose_count = 0
    tie_count = 0

    while True:
        player_choice = input('''Please make your choice:
            "r" for Rock
            "p" for Paper
            "s" for Scissors
            "i" for info & "q" to quit game
        your choice = ''').lower()
        if player_choice == 'i':
            print("""
                The rules to play it are pretty simple.
                The game is played where players deliver hand signals that will represent the elements of the game; rock, paper and scissors.
                The outcome of the game is determined by 3 simple rules:

                * Rock wins against scissors.
                * Scissors win against paper.
                * Paper wins against rock.
            """)
        elif player_choice == "q":
            print("\n Thanks for game.")
            return f"\t win: {win_count};  lose: {lose_count}; tie: {tie_count}"
        elif player_choice in ["r", "p", "s"]:
            computer_choice = random.choice(["r", "p", "s"])
            if computer_choice == "r":
                if player_choice == "r":
                    print(art.rr)
                    print(art.tie)
                    tie_count += 1
                elif player_choice == "p":
                    print(art.rp)
                    print(art.win)
                    win_count += 1
                else:
                    print(art.rs)
                    print(art.lose)
                    lose_count += 1
            elif computer_choice == "p":
                if player_choice == "r":
                    print(art.pr)
                    print(art.lose)
                    lose_count += 1
                elif player_choice == "p":
                    print(art.pp)
                    print(art.tie)
                    tie_count += 1
                else:
                    print(art.ps)
                    print(art.win)
                    win_count += 1
            else:
                if player_choice == "r":
                    print(art.sr)
                    print(art.win)
                    win_count += 1
                elif player_choice == "p":
                    print(art.sp)
                    print(art.lose)
                    lose_count += 1
                else:
                    print(art.ss)
                    print(art.tie)
                    tie_count += 1
        else:
            print("your choice is incorrect")


print(game())
