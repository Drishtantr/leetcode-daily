import pandas as pd

# Sample employee data
data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'department': ['HR', 'Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'HR', 'Engineering', 'Sales', 'HR'],
    'salary': [55000, 80000, 50000, 95000, 60000, 45000, 58000, 100000, 47000, 63000],
    'gender': ['F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'M'],
    'join_date': ['2020-01-15', '2019-03-22', '2021-07-12', '2018-11-19', '2020-04-10', '2021-06-30', '2021-01-25', '2017-10-05', '2020-05-18', '2019-12-05'],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert join_date to datetime
df['join_date'] = pd.to_datetime(df['join_date'])


df['join_date'] = pd.to

# Group the data by department and calculate the average salary in each department.

avg_sal = df.groupby('department')['salary'].mean().round().to_dict()


# Group the data by department and count how many employees are in each department.

count_emp = df.groupby('department')['salary'].count()

# Group by gender and calculate the average salary for each gender.

gen_sal = df.groupby('gender')['salary'].mean().round().to_dict()
print(gen_sal)

print('the number of people who aren\'t going to be goint there' )

