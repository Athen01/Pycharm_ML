import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('task1.csv')
print(data.to_string())

mean_runs = data['runs'].mean()
mean_batting_avg = data['batting average'].mean()
mean_strike_rate = data['strike rate'].mean()

print(f"\nMean Runs: {mean_runs}")
print(f"Mean Batting Average: {mean_batting_avg}")
print(f"Mean Strike Rate: {mean_strike_rate}")

mean_values = [mean_runs, mean_batting_avg, mean_strike_rate]
plt.plot(numeric_columns, mean_values, marker='o')
plt.ylabel('Mean Value')
plt.title('Mean Statistics')
plt.show()