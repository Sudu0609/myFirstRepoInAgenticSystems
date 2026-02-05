# Store marks of at least 8 students
marks = [78, 85, 90, 65, 70, 88, 92, 80]

# Print full list
print("All Marks:", marks)

# First 3 marks using slicing
print("First 3 marks:", marks[:3])

# Last 3 marks using slicing
print("Last 3 marks:", marks[-3:])

# Highest mark
print("Highest:", max(marks))

# Lowest mark
print("Lowest:", min(marks))

# Average mark
average = sum(marks) / len(marks)
print("Average:", average)
