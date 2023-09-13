import pandas as pd

# Load the CSV file
data = pd.read_csv('MeanMedianData.csv')

# Compute mean, median, and mode for each column
mean_values = data.mean()
median_values = data.median()
mode_values = data.mode().iloc[0]

print("Mean values:\n", mean_values)
print("Median values:\n", median_values)
print("Mode values:\n", mode_values)

import matplotlib.pyplot as plt

# Plot each column using different colors
for column in data.columns:
    plt.plot(data[column], label=column)

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Column Data")
plt.legend()
plt.show()