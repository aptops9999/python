# ---------------------------
# 10th Grade Marksheet Program
# ---------------------------

# Function to calculate total, percentage and grade
def calculate_results(marks):
    # Arithmetic Operators
    total = sum(marks)  # total = marks[0] + marks[1] + ...
    percentage = total / len(marks)

    # Grade assignment using comparison and logical operators
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'

    return total, percentage, grade

# Function to print the marksheet
def print_marksheet(name, roll, subjects, marks):
    total, percentage, grade = calculate_results(marks)

    print("\n-----------------------------")
    print("       10th Grade Marksheet ")
    print("-----------------------------")
    print("Name      :", name)
    print("Roll No.  :", roll)
    print("-----------------------------")
    print("Subject-wise Marks:")
    for sub, mark in zip(subjects, marks):
        print(f"{sub:12}: {mark}")
    print("-----------------------------")
    print(f"Total Marks : {total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print("-----------------------------")

    # Logical and bitwise operator example (just for demonstration)
    passed = all(m >= 33 for m in marks)  # all subjects should have >= 33
    print("Result      :", "PASS" if passed else "FAIL")
    
    # Bitwise check for fun (not needed, just demonstrating)
    print("Bitwise check (total & 1):", total & 1)  # Checks if total is odd/even

# Main Program

# Variables (Name, Roll number, Subjects, Marks)
student_name = "Riya Sharma"
roll_number = "2025A001"

subjects = ["Math", "Science", "English", "Hindi", "Social"]
marks = [88, 75, 92, 85, 79]  # All out of 100

# Function call
print_marksheet(student_name, roll_number, subjects, marks)

# Identity and membership operators demo
extra_subjects = ["Sanskrit", "Computer"]
print("\n'Sanskrit' in extra_subjects:", 'Sanskrit' in extra_subjects)  # Membership
print("marks is marks:", marks is marks)  # Identity
print("marks is not subjects:", marks is not subjects)
