# Employee tuple
employee = (101, "Sudarshan", "IT")

# Roles set
roles = {"admin", "editor", "viewer"}

# Print employee info using indexing
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])

# Check admin access
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
