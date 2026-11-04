# Student Scholarship Eligibility System

print("\n==== Student Scholarship Eligibility System ====")

# Step 1: Collect student information
student_name = input("\nEnter student name: ")
academic_marks = float(input("Enter academic marks (%): "))
attendance_percentage = float(input("Enter attendance percentage (%): "))
monthly_family_income = float(input("Enter monthly family income (Rs.): "))

# Step 2: Validate information
if student_name.strip() == "":
    print("Invalid Input! Student name cannot be empty.")

elif academic_marks < 0 or academic_marks > 100:
    print("Invalid Input! Marks must be between 0 and 100.")

elif attendance_percentage < 0 or attendance_percentage > 100:
    print("Invalid Input! Attendance must be between 0 and 100.")

elif monthly_family_income < 0:
    print("Invalid Input! Income cannot be negative.")

else:
    # Step 3: Display student information
    print("\n==== Scholarship Evaluation Report ====")
    print("\nStudent Name:", student_name)
    print("Academic Marks:", academic_marks, "%")
    print("Attendance:", attendance_percentage, "%")
    print("Monthly Family Income: Rs.", monthly_family_income)

    # Step 4: Check eligibility
    if academic_marks >= 80 and attendance_percentage >= 85 and monthly_family_income <= 50000:

        if academic_marks >= 90:
            print("\nScholarship Status: Eligible")
            print("\nScholarship Type: Full Scholarship")

        elif academic_marks >= 80:
            print("\nScholarship Status: Eligible")
            print("\nScholarship Type: Partial Scholarship")

    else:
        print("\nScholarship Status: Not Eligible")
        print("\nReason for Ineligibility:")

        if academic_marks < 80:
            print("- Academic marks are below 80%.")

        if attendance_percentage < 85:
            print("- Attendance is below 85%.")

        if monthly_family_income > 50000:
            print("- Monthly family income exceeds Rs. 50,000.")

    print("====================================")
