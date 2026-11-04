# Student Scholarship Eligibility System

print("\n==== Student Scholarship Eligibility System ====")

# Step 1: Collect student information
name = input("\nEnter student name: ")
marks = float(input("Enter academic marks (%): "))
attendance = float(input("Enter attendance percentage (%): "))
income = float(input("Enter monthly family income (Rs.): "))

# Step 2: Validate information
if name.strip() == "":
    print("Invalid Input! Student name cannot be empty.")

elif marks < 0 or marks > 100:
    print("Invalid Input! Marks must be between 0 and 100.")

elif attendance < 0 or attendance > 100:
    print("Invalid Input! Attendance must be between 0 and 100.")

elif income < 0:
    print("Invalid Input! Income cannot be negative.")

else:
    # Step 3: Display student information
    print("\n==== Scholarship Evaluation Report ====")
    print("\nStudent Name:", name)
    print("Academic Marks:", marks, "%")
    print("Attendance:", attendance, "%")
    print("Monthly Family Income: Rs.", income)

    # Step 4: Check eligibility
    if marks >= 80 and attendance >= 85 and income <= 50000:

        if marks >= 90:
            print("\nScholarship Status: Eligible")
            print("\nScholarship Type: Full Scholarship")

        elif marks >= 80:
            print("\nScholarship Status: Eligible")
            print("\nScholarship Type: Partial Scholarship")

    else:
        print("\nScholarship Status: Not Eligible")
        print("\nReason for Ineligibility:")

        if marks < 80:
            print("- Academic marks are below 80%.")

        if attendance < 85:
            print("- Attendance is below 85%.")

        if income > 50000:
            print("- Monthly family income exceeds Rs. 50,000.")

    print("====================================")
