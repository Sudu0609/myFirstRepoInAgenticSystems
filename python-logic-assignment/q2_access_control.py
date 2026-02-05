age = input("Enter your age: ")
age = int(age)

has_id = input("Do you have ID (True/False): ")
has_id = has_id == "True"

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
