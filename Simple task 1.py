import random
import pandas as pd
import matplotlib.pyplot as plt


def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        print("Choose: 1 - Rock, 2 - Paper, 3 - Scissors")
        user_choice = int(input("Enter your choice: "))
        computer_choice = random.randint(1, 3)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
                (user_choice == 2 and computer_choice == 1) or \
                (user_choice == 3 and computer_choice == 2):
            print("Congratulations! You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    return user_wins, computer_wins


def save_to_excel(user_wins, computer_wins):
    data = {'User Wins': [user_wins], 'Computer Wins': [computer_wins]}
    df = pd.DataFrame(data)
    df.to_excel('game_results.xlsx', index=False)
    print("Results saved to 'game_results.xlsx'.")


def plot_results(user_wins, computer_wins):
    total_games = user_wins + computer_wins
    user_success_rate = user_wins / total_games * 100
    computer_success_rate = computer_wins / total_games * 100

    labels = ['User Wins', 'Computer Wins']
    success_rates = [user_success_rate, computer_success_rate]

    plt.bar(labels, success_rates, color=['green', 'red'])
    plt.ylabel('Success Rate (%)')
    plt.title('Game Success Rates')
    plt.ylim(0, 100)
    plt.show()


def main():
    print("Welcome to Rock, Paper, Scissors Game!")

    user_wins, computer_wins = play_game()
    save_to_excel(user_wins, computer_wins)
    plot_results(user_wins, computer_wins)