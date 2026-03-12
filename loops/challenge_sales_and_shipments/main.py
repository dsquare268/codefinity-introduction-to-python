# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

#Iterate over the list of products using range(len())
for i in range(len(products)):
    product_name = products[i][0]
    #Check each item in units_sold
    for sold_item in units_sold:
        if sold_item[0] == product_name:
            #Subtract units sold from stock
            products[i][1] -= sold_item[1]

    
# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]
#Iterate again over the list of products using range(len())
for i in range(len(products)):
    product_name = products[i][0]
    #Check each item in shipment_received
    for shipped_items in shipment_received:
        if shipped_items[0] == product_name:
        #Add units received from shipments
            products[i][1] += shipped_items[1]
    

print("Final stock levels for all products:", products)