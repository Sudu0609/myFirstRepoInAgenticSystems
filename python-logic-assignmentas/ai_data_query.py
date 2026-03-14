import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [95, 92, 78, 88, 83],
    "Passed": [True, True, False, True, False],
    "Category": ["A", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")


print("Single Column (Name):")
print(df["Name"])
print("\n")


print("Multiple Columns (Name and Score):")
new_df = df[["Name", "Score"]]
print(new_df)
print("\n")


print("First Three Rows using iloc:")
print(df.iloc[0:3])
print("\n")


df_indexed = df.set_index("Name")

print("Using loc after setting index:")
print(df_indexed.loc["Alice"])
print("\n")


high_scores = df[df["Score"] > 85]

print("Students with Score > 85:")
print(high_scores)
print("\n")


filtered_students = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Students with Score > 85 AND Passed:")
print(filtered_students)
print("\n")


sorted_students = filtered_students.sort_values(by="Score", ascending=False)

print("High-performing students (sorted):")
print(sorted_students[["Name", "Score"]])