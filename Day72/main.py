import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
pd.options.display.float_format = "{:,.2f}".format

clean_df = df.dropna()

max_median_salary = clean_df["Starting Median Salary"].max()
index_max_median_salary = clean_df["Starting Median Salary"].idxmax()

# print(clean_df["Undergraduate Major"].loc[index_max_median_salary])
# print(max_median_salary)

# 1 question
max_mid_career_salary = clean_df["Mid-Career Median Salary"].max()
index_max_mid_career = clean_df["Mid-Career Median Salary"].idxmax()
# print(clean_df["Undergraduate Major"][index_max_mid_career])
# print(max_mid_career_salary)

# 1) Chemical engineer
# 2) 107,000.00
################################
# 2 question
min_starting_salary = clean_df["Starting Median Salary"].min()
index_min_starting_salary = clean_df["Starting Median Salary"].idxmin()
# print(clean_df["Undergraduate Major"].loc[index_min_starting_salary])
# print(min_starting_salary)

# 1) Spanish
# 2) 34,000.00
#################################
# 3 question
min_mid_career_salary = clean_df["Mid-Career Median Salary"].min()
index_min_mid_career = clean_df["Mid-Career Median Salary"].idxmin()
# print(clean_df["Undergraduate Major"][index_min_mid_career])
# print(min_mid_career_salary)

# 1) Education
# 2) 52,000.00

# Lowest risk majors
diff_salary = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)
clean_df.insert(1, "Diff Salary", diff_salary)
min_salary_diff = clean_df["Diff Salary"].min()
index_min_salary_diff = clean_df["Diff Salary"].idxmin()
safe_major = clean_df["Undergraduate Major"][index_min_salary_diff]
# print(min_salary_diff)
# print(index_min_salary_diff)
# print(safe_major)

clean_df["diff_salary"] = diff_salary
low_risk = clean_df.sort_values(by="diff_salary")
# print(low_risk[['diff_salary', 'Undergraduate Major']].head())
highest_potential = clean_df.sort_values(by="diff_salary", ascending=False)
# print(highest_potential[['diff_salary', 'Undergraduate Major']].head())

# print(clean_df[['Undergraduate Major', 'Group']].groupby('Group').count())
salary_of_group = (
    clean_df[["Mid-Career Median Salary", "Group"]].groupby("Group").mean()
)
print(salary_of_group)
