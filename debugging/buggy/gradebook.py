def get_letter_grade(score):
    breakpoint() # 1
    #
    # Convert numerical scores to letter grades
    if score >= 90:
        letter = "A"
    if score >= 80:
        letter = "B"
    if score >= 70:
        letter = "C"
    if score >= 60:
        letter = "D"
    else:
        letter = "F"

    return letter


def process_student_grades(grades_dict):
    letter_grades = {}
    total = 0

    for student, score in grades_dict.items():
        # add score to total
        total += score

        # breakpoint() # 2
        # track count of how many of each letter grade
        letter_grades[student] = get_letter_grade(score)
        total += score

    class_average = total / len(grades_dict)

    # Count how many of each grade
    grade_counts = {}
    for grade in letter_grades.values():
        if grade in grade_counts:
            # breakpoint() # 3
            grade_counts[grade] += 1

    return letter_grades, class_average, grade_counts


grades = {
    "Beau": 55,
    "Fran": 68,
    "Reza": 95,
}


def main():
    letters, avg, counts = process_student_grades(grades)
    print(f"Letter Grades: {letters}")
    print(f"Class Average: {avg}")
    print(f"Grade Distribution: {counts}")


if __name__ == "__main__":
    main()
