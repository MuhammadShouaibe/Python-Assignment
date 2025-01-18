# Function to handle the cashier tasks
def cashier_receipts():
    # Step 1: Prompt the user to input the number of customers
    num_customers = int(input("Enter the number of customers: "))
    
    overall_total = 0  # Variable to keep track of the total for the day

    # Step 2: Loop through each customer
    for customer in range(1, num_customers + 1):
        print(f"\nCustomer {customer}:")
        
        # Ask how many items the customer purchased
        num_items = int(input(f"How many items did Customer {customer} purchase? "))
        
        customer_total = 0  # Initialize the total for the current customer
        
        # Step 3: Loop through each item for the current customer
        for item in range(1, num_items + 1):
            item_price = float(input(f"Enter the price of item {item}: $"))
            customer_total += item_price  # Add the item price to the customer's total
        
        # Display the total bill for the current customer
        print(f"Total bill for Customer {customer}: ${customer_total:.2f}")
        
        # Add the customer's total to the overall total for the day
        overall_total += customer_total

    # Step 4: Display the overall total for the day
    print(f"\nOverall total for the day: ${overall_total:.2f}")

# Run the cashier task function
if __name__ == "__main__":
    cashier_receipts()
