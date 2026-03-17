import pandas as pd
import numpy as np


data = {
    "Employee": ["Amit", "Neha", "Rahul", "Sneha", "Vikram", "Priya", "Arjun", "Divya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [600000, 500000, np.nan, 700000, 520000, np.nan, 650000, 480000],
    "Temporary_Notes": [
        "On probation", "Contract", "Pending docs", "Verified",
        "Intern", "New joiner", "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
print("\n")


print("Missing Values:\n", df.isnull().sum())
print("\n")


mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)

print("After Filling Missing Salary:\n", df)
print("\n")


df_cleaned = df.drop(columns=["Temporary_Notes"])

print("After Dropping Temporary_Notes:\n", df_cleaned)
print("\n")


df_cleaned = df_cleaned.rename(columns={"Salary": "Annual_Salary"})

print("After Renaming Column:\n", df_cleaned)
print("\n")


summary = df_cleaned.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)


print("Final Summary Table:\n", summary)