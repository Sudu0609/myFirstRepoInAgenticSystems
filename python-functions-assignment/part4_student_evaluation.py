# Function 1: Greeting
def greet_student(name):
    return f"Hello, {name}"


# Function 2: Score analysis
def analyze_scores(scores):
    subjects = len(scores)
    average = sum(scores) / subjects
    return subjects, average


# Function 3: Result decision
def evaluate_result(avg):

    if avg >= 50:
        return "Pass"
    else:
        return "Fail"


# Main function
def main():

    name = input("Enter student name: ")

    scores = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    greeting = greet_student(name)
    subjects, avg = analyze_scores(scores)
    result = evaluate_result(avg)

    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", avg)
    print("Result:", result)


# Start program
main()
