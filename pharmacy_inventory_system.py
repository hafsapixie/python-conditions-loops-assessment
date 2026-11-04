# Smart Pharmacy Inventory & Sales Management System

print("\n==== Smart Pharmacy Inventory & Sales Management System ====")

# Step 1: Ask how many medicines to process
total_medicines = int(input("\nEnter the number of medicines: "))

# Step 2: Initialize variables
total_revenue = 0
restock_count = 0

# Step 3: Process each medicine using for loop
for i in range(total_medicines):

    print("\n---- Medicine", i + 1 , "----")

    # Step 4: Collect medicine information
    medicine_name = input("Enter medicine name: ")
    stock = int(input("Enter available stock: "))
    price = float(input("Enter price per unit (Rs.): "))
    quantity_sold = int(input("Enter quantity sold: "))

    # Step 5: Check input validity
    if stock < 0 or price < 0 or quantity_sold < 0:
        print("\nInvalid input! Values cannot be negative.")

    # Step 6: Check stock availability
    elif quantity_sold > stock:
        print("\nInsufficient stock!")
        print("Available stock:", stock)
        print("Requested quantity:", quantity_sold)

        print("Sale could not be processed.")

    else:
        # Step 7: Calculate sales amount
        sales_amount = quantity_sold * price

        # Step 8: Calculate remaining stock
        remaining_stock = stock - quantity_sold

        # Step 9: Update total revenue (Accumulator)
        total_revenue = total_revenue + sales_amount

        # Step 10: Display medicine details
        print("\nMedicine Name:", medicine_name)
        print("Sales Amount: Rs.", sales_amount)
        print("Remaining Stock:", remaining_stock)

        # Step 11: Check low stock
        if remaining_stock < 10:
            print("\nWarning: Low Stock! Restocking Required.")

            # Counter
            restock_count = restock_count + 1

        else:
            print("\nStock Status: Sufficient")

# Step 12: Display final pharmacy report
print("\n=== Daily Pharmacy Sales Report ===")

print("\nTotal Medicines Processed:", total_medicines)
print("Total Pharmacy Revenue: Rs.", total_revenue)
print("Medicines Requiring Restocking:", restock_count)

print("==================================")
