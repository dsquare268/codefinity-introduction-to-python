# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}


total_sales_list = []

#Iterate through the dictionary
for item, details in products.items():
    price, quantity_sold = details
    price_converted = float(price)
    quantity_sold_converted = int(quantity_sold)
    total_sales = price_converted * quantity_sold_converted
    print(f"Total sales for {item}:", "$",total_sales)
    total_sales_list.append(total_sales)
    
total_sum = sum(total_sales_list)


print(f"Total sum of all sales:", "$",total_sum)
min_sales = min(total_sales_list)
print(f"Minimum sales:", "$",min_sales)
max_sales = max(total_sales_list)
print(f"Maximum sales:", "$",max_sales)
    