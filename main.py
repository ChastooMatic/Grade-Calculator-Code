def calculate_total(marks_list):
    return sum(marks_list)

def calculate_percentage(total, num_subjects=5):
    return total / num_subjects

def get_valid_mark(subject_num):
    while True:
        try:
            mark = float(input(f"Marks for subject {subject_num}: "))
            if 0 <= mark <= 100: return mark
            print("Invalid marks. Enter a number between 0 and 100.")
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")

def main():
    while True:
        name = input("Name: ")
        marks = []
        for i in range(1, 6):
            marks.append(get_valid_mark(i))

        total = calculate_total(marks)
        percentage = calculate_percentage(total)

        if percentage >= 85: grade = 'A'
        elif percentage >= 70: grade = 'B'
        elif percentage >= 55: grade = 'C'
        elif percentage >= 40: grade = 'D'
        else: grade = 'F'

        result = "Pass" if percentage >= 40 else "Fail"
        print(f"{name} | Total: {total:.0f} | Percentage: {percentage:.2f}% | Grade: {grade} | Result: {result}")

        if input("Another student? (y/n): ").strip().lower() != 'y':
            break

if __name__ == "__main__":
    main()
