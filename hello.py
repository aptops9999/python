# Single-line comment: This program evaluates a student's grade based on marks

# Multi-line comment:
'''
This Python program demonstrates the use of:
- Comments
- Variables
- Functions
- All types of operators
- Now includes subject names
'''


def evaluate_grade(subject_marks):
    # Arithmetic Operators: +, -, *, /, %, **, //
    marks = list(subject_marks.values())   # extract just the marks
    total = sum(marks)
    avg = total / len(marks)

    # Comparison Operators: >, <, >=, <=, ==, !=
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Logical Operators: and, or, not
    passed = avg >= 40 and grade != 'F'

    # Identity Operators: is, is not
    grade_is_A = grade is 'A'

    # Membership Operators: in, not in
    reward = 'Yes' if grade in ['A', 'B'] else 'No'

    # Bitwise Operators: &, |, ^, ~, <<, >>
    bitwise_demo = (5 & 3) | (8 >> 2)

    return {
        'Total': total,
        'Average': avg,
        'Grade': grade,
        'Passed': passed,
        'Is Grade A': grade_is_A,
        'Eligible for Reward': reward,
        'Bitwise Result': bitwise_demo
    }

# Assignment Operators: =, +=, -=, etc.
student_name = "Alice"
student_class = "10" # New variable for a class. 

# Dictionary: subjects and their marks
subject_marks = {
    'Math': 85,
    'Science': 90,
    'English': 78,
    'Computer': 92,
    'History': 88
}

# Add bonus marks using +=
for subject in subject_marks:
    subject_marks[subject] += 2  # adding 2 bonus marks

# Function call
result = evaluate_grade(subject_marks)

# Output
print(f"\nStudent Name: {student_name}")
print("\nSubject-wise Marks:")
for subject, mark in subject_marks.items():
    print(f"{subject}: {mark}")

print("\nResult Summary:")
for key, value in result.items():
    print(f"{key}: {value}") 
