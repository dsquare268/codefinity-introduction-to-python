# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

#use zip and list to combine three separate lists and create a single list 
combined_list = list(zip(products,prices,quantities_sold))

#use sorted() to sort combined_list by product's name in asending order
sorted_products = sorted(combined_list)

#loop through sorted list and print product's name, price and quantity sold
for product_name, price, quantity_sold in sorted_products:
    print(f"Product:{product_name}, Price:{price}, Quantity Sold:{quantity_sold}")
