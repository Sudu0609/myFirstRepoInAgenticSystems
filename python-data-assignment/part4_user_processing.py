# Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)


# Function to check admin role
def is_admin(roles):
    return "admin" in roles


# Main function
def main():

    # List of users
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 72],
            "roles": {"viewer"}
        }
    ]

    # Iterate users
    for user in users:

        avg_score = calculate_average(user["scores"])
        admin_status = is_admin(user["roles"])

        print("\nName:", user["name"])
        print("Average Score:", avg_score)
        print("Admin Access:", admin_status)


# Run main
main()
