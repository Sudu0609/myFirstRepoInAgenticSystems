import pandas as pd

# Step 1: Load CSV file
print("Loading Dataset...\n")
df = pd.read_csv("students.csv")

# Step 2: Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Step 3: Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Step 4: Dataset Info
print("\nDataset Info:")
df.info()

# Step 5: Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 6: Select single column
print("\nSelecting Single Column (Score):")
score_column = df["Score"]
print(score_column)

# Step 7: Select multiple columns
print("\nSelecting Multiple Columns (Name, Score):")
selected_columns = df[["Name", "Score"]]
print(selected_columns)

# Step 8: Filter rows
print("\nFiltered Rows (Score > 80):")
filtered_data = df[df["Score"] > 80]
print(filtered_data)
