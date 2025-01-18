def cashier_receipts():
    num_customers = int(input("Enter the number of customers: "))
    
    overall_total = 0  # Variable to keep track of the total for the day
    for customer in range(1, num_customers + 1):
        print(f"\nCustomer {customer}:")
        num_items = int(input(f"How many items did Customer {customer} purchase? "))
        
        customer_total = 0  # Initialize the total for the current customer
        for item in range(1, num_items + 1):
            item_price = float(input(f"Enter the price of item {item}: $"))
            customer_total += item_price  # Add the item price to the customer's total

        print(f"Total bill for Customer {customer}: ${customer_total:.2f}")
        overall_total += customer_total
    print(f"\nOverall total for the day: ${overall_total:.2f}")
if __name__ == "__main__":
    cashier_receipts()
