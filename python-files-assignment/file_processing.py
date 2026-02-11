def read_numbers(file_name):
    numbers_list = []

    with open(file_name, "r") as file:
        print("File opened successfully")

        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                numbers_list.append(int(cleaned_line))

    return numbers_list


def compute_statistics(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average_value = total_sum / total_count if total_count > 0 else 0

    return total_count, total_sum, average_value


def write_logs(file_name, count, total, average):
    with open(file_name, "a") as log_file:

        log_file.write("File opened successfully\n")
        log_file.write(f"Read {count} numbers\n")
        log_file.write(f"Sum: {total}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n")
        log_file.write("--------------------------\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers(input_file)
    count, total, average = compute_statistics(numbers)
    write_logs(log_file, count, total, average)

    print("Processing completed. Check results.log")


if __name__ == "__main__":
    main()
