import random
import pandas as pd

computer_wins = 0
user_wins = 0

for i in range(10):
    computer = random.randint(1, 9)
    user_input = int(input("Enter the number between 1 and 9: "))
    print(f"Computer: {computer}")
    print(f"User: {user_input}")
    if computer > user_input:
        print("Computer won")
        computer_wins += 1
    elif computer == user_input:
        print("Tie")
    else:
        print("You won")
        user_wins += 1

data = {"Computer Wins": [computer_wins], "User Wins": [user_wins]}
df = pd.DataFrame(data)

csv_filename = 'LoterryData.csv'
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")

import pandas as pd
import matplotlib.pyplot as plt

csv_filename = 'LoterryData.csv'
df = pd.read_csv(csv_filename)

computer_wins = df['Computer Wins'][0]
user_wins = df['User Wins'][0]

labels = ['Computer Wins', 'User Wins']
values = [computer_wins, user_wins]

plt.bar(labels, values, color=['blue', 'green'])
plt.xlabel('Outcome')
plt.ylabel('Number of Wins')
plt.title('Computer vs User Wins')
plt.show()