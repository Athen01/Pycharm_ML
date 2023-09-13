import pandas as pd
from scipy import stats

# Read CSV file into a DataFrame
data = pd.read_csv("marks_data.csv")

# Calculate mean, median, and mode for marks column
marks_column = data['marks']
mean = marks_column.mean()
median = marks_column.median()
mode = stats.mode(marks_column)[0]  # Get the array of modes
mode_str = ""
for x in mode:
    mode_str += str(x) + ", "
mode_str = mode_str[:-2# Convert modes to a comma-separated string


print("Statistics for Marks:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode_str}")
print("-" * 20)

# Example: Calculating statistics for each student (if needed)
student_statistics = {}
for index, row in data.iterrows():
    student_name = row['name']
    student_marks = row['marks']
    if student_name not in student_statistics:
        student_statistics[student_name] = {'marks': [], 'Mean': None, 'Median': None, 'Mode': None}
    student_statistics[student_name]['marks'].append(student_marks)

for student, stats_dict in student_statistics.items():
    marks = stats_dict['marks']
    stats_dict['Mean'] = sum(marks) / len(marks)
    stats_dict['Median'] = stats.median(marks)
    mode_result = stats.mode(marks)
    stats_dict['Mode'] = ", ".join(str(x) for x in mode_result[0])

# Display computed statistics for each student
print("Statistics for Each Student:")
for student, stats_dict in student_statistics.items():
    print(f"Student: {student}")
    print(f"Mean: {stats_dict['Mean']}")
    print(f"Median: {stats_dict['Median']}")
    print(f"Mode: {stats_dict['Mode']}")
    print("-" * 20)