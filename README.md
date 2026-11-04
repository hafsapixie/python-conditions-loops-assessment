# Python Conditions & Loops Assessment

A beginner-friendly Python project demonstrating conditional statements and loop structures through two practical applications.

## Repository Information

**Repository Name:** `python-conditions-loops-assessment`

**Programming Language:** Python

## Project Overview

This project contains two Python applications developed as part of the Conditions & Loops Assessment.

### Task 1: Student Scholarship Eligibility System

**File:** `student_scholarship_system.py`

A Python application that evaluates students' eligibility for university scholarships based on their academic marks, attendance percentage, and monthly family income.

**Features:**

- Collects student information.
- Validates marks, attendance, and family income.
- Checks scholarship eligibility using conditional statements.
- Awards Full Scholarship for marks of 90% or above.
- Awards Partial Scholarship for marks between 80% and 89%.
- Displays reasons for ineligibility.
- Generates a complete scholarship evaluation report.

**Scholarship Eligibility Criteria:**

| Requirement | Criteria |
|---|---|
| Academic Marks | At least 80% |
| Attendance | At least 85% |
| Monthly Family Income | Rs. 50,000 or less |
| Full Scholarship | Marks 90% or above |
| Partial Scholarship | Marks 80% to 89% |

### Task 2: Smart Pharmacy Inventory & Sales Management System

**File:** `pharmacy_inventory_system.py`

A Python application that manages medicine inventory and calculates daily pharmacy sales revenue.

**Features:**

- Processes multiple medicines using a for loop.
- Collects medicine name, available stock, price, and quantity sold.
- Checks medicine stock availability before processing sales.
- Calculates sales amounts and remaining stock.
- Displays low-stock warnings when remaining stock is below 10 units.
- Calculates total pharmacy revenue using an accumulator.
- Counts medicines requiring restocking.
- Generates a final daily sales report.

## Python Concepts Covered

The following Python concepts are demonstrated in this project:

- `input()` and `print()` functions
- Variables and data types
- Type conversion (`int()` and `float()`)
- Conditional statements (`if`, `elif`, `else`)
- Comparison operators
- Logical operators (`and`, `or`)
- `for` loop
- `range()` function
- Conditions inside loops
- Counters and accumulators
- Basic input validation

## Project Structure

```text
python-conditions-loops-assessment/
│
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Requirements

- Python 3.x
- Any Python-supported code editor, such as Visual Studio Code.

## How to Run the Programs

**1. Clone the repository**

```bash
git clone https://github.com/YourUsername/python-conditions-loops-assessment.git
```

**2. Open the project folder**

```bash
cd python-conditions-loops-assessment
```

**3. Run Task 1**

```bash
python student_scholarship_system.py
```

**4. Run Task 2**

```bash
python pharmacy_inventory_system.py
```

## Sample Input/Output

### Task 1: Scholarship System

**Sample Input:**

```text
Enter student name: Ali
Enter academic marks (%): 95
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 30000
```

**Sample Output:**

```text
===== Scholarship Evaluation Report =====
Student Name: Ali
Academic Marks: 95.0 %
Attendance: 90.0 %
Monthly Family Income: Rs. 30000.0
Scholarship Status: Eligible
Scholarship Type: Full Scholarship
========================================
```

### Task 2: Pharmacy System

**Sample Input:**

```text
Enter the number of medicines: 2

Medicine 1:
Medicine name: Panadol
Available stock: 50
Price per unit: 30
Quantity sold: 45

Medicine 2:
Medicine name: Calpol
Available stock: 40
Price per unit: 50
Quantity sold: 10
```

**Sample Output:**

```text
===== Daily Pharmacy Sales Report =====
Total Medicines Processed: 2
Total Pharmacy Revenue: Rs. 1850.0
Medicines Requiring Restocking: 1
=======================================
```

## Author

**Hafsa Naseer**

Created as part of the Python Conditions & Loops Assessment.

---