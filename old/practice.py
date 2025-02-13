# Basic Analysis:

# Write a function to calculate the mean engagement_score for each department. Convert the result into a dictionary.

# Data Insights:

# Identify the department with the highest average engagement score.
# Identify the department with the lowest average engagement score.

# Filtering and Grouping:

# Filter out all employees with an engagement_score below 7 and recalculate the average engagement score per department.
# Trend Analysis:

# Suppose the data has a month column added. Calculate the average engagement_score for each department across months.
# Visualization Challenge:

# Plot a bar chart to show the average engagement score per department.

import pandas as pd

data = [
    {"employee_id": 1, "department": "HR", "engagement_score": 8},
    {"employee_id": 2, "department": "Engineering", "engagement_score": 7},
    {"employee_id": 3, "department": "HR", "engagement_score": 6},
    {"employee_id": 4, "department": "Engineering", "engagement_score": 9},
    {"employee_id": 5, "department": "Sales", "engagement_score": 5},
    {"employee_id": 6, "department": "Sales", "engagement_score": 7},
    {"employee_id": 7, "department": "Engineering", "engagement_score": 8},
    {"employee_id": 8, "department": "HR", "engagement_score": 9},
    {"employee_id": 9, "department": "HR", "engagement_score": 7},
    {"employee_id": 10, "department": "Sales", "engagement_score": 6},
]


df = pd.DataFrame(data)

df.dropna()

# Write a function to calculate the mean engagement_score for each department. Convert the result into a dictionary.

eng_score = df.groupby('department')['engagement_score'].mean().to_dict()

print(eng_score)

print(f"Highest eng_score: {max(eng_score, key = eng_score.get)}")
print(f"Lowest eng_score: {min(eng_score, key = eng_score.get)}")

# Filter out all employees with an engagement_score below 7 and recalculate the average engagement score per department.

filtered_df = df[df['engagement_score']>7]
print(filtered_df)

# Suppose the data has a month column added. Calculate the average engagement_score for each department across months.

new_data = [
    {"employee_id": 1, "department": "HR", "engagement_score": 8, "month": "Jan"},
    {"employee_id": 2, "department": "Engineering", "engagement_score": 7, "month": "Jan"},
    {"employee_id": 3, "department": "HR", "engagement_score": 6, "month": "Feb"},
    {"employee_id": 4, "department": "Engineering", "engagement_score": 9, "month": "Mar"},
    {"employee_id": 5, "department": "Sales", "engagement_score": 5, "month": "Feb"},
    {"employee_id": 6, "department": "Sales", "engagement_score": 7, "month": "Mar"},
    {"employee_id": 7, "department": "Engineering", "engagement_score": 8, "month": "Apr"},
    {"employee_id": 8, "department": "HR", "engagement_score": 9, "month": "Feb"},
    {"employee_id": 9, "department": "HR", "engagement_score": 7, "month": "Mar"},
    {"employee_id": 10, "department": "Sales", "engagement_score": 6, "month": "Jan"},
]

new_df = pd.DataFrame(new_data)

eng_score_new = new_df.groupby(['month','department'])['engagement_score'].mean().unstack().fillna(0).to_dict()

print(eng_score_new)



