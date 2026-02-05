# Ask user name
user_name = input("Enter your name: ")

# Ask user age
user_age = input("Enter your age: ")
user_age = int(user_age)

# Ask active user status
active_status = input("Are you an active user (True/False): ")
active_status = active_status == "True"

# Print summary
print(f"User {user_name} is {user_age} years old. Active status: {active_status}")
