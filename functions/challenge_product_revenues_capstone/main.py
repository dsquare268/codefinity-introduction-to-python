# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


#define calculate_revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []

    for price, qty in zip(prices, quantities_sold):
        revenue.append(price * qty)
    
    return revenue
    

# Define format revenue
def formatted_output(revenues):
    # Sort alphabetically by product name
    sorted_list = sorted(revenue_per_product)
    # Print formatted results
    for product, rev in sorted_list:
        print(f"{product} has total revenue of ${rev:.2f}")


# Main program
revenue = calculate_revenue(prices, quantities_sold)  

# Combine products and revenue
revenue_per_product = list(zip(products, revenue))

# Call formatting function
formatted_output(revenue_per_product)
# Example of expected output line (do not remove):
#print(f"{product_name[0]} has total revenue of ${revenue[1]}")