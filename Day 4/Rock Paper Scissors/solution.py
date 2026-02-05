import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_not_over = True
game_image = [rock, paper, scissors]

while game_not_over:

    user_choice = int(input("Enter your choice (0 = rock, 1 = paper, 2 = scissors): "))

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. You lost!")
        break

    print("Your choice:")
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(game_image[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 0 and computer_choice == 1) or
        (user_choice == 1 and computer_choice == 2) or
        (user_choice == 2 and computer_choice == 0)
    ):
        print("You lost!")
    else:
        print("You won!")

    option = input("Do you want to end the game? (yes/no): ").lower()
    if option == "yes":
        game_not_over = False
        print("Game Over")
