grocery_inventory = {
    "Milk":("Dairy",3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)
}
#check egg price
eggs = grocery_inventory.get("Eggs")

if eggs and eggs[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, price, stock = eggs
    grocery_inventory["Eggs"] = (category, price - 1, stock)
else:
    print("The price of eggs is reasonable.")

#Add a new item
grocery_inventory.update({
    "Tomatoes":("Produce",1.20,30)
})
print("Inventory after adding Tomatoes:", grocery_inventory)

milk = grocery_inventory.get("Milk")

if milk and milk[2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category, price,stock = milk
    grocery_inventory["Milk"] = (category,price, stock + 20)
else:
    print("Milk has sufficient stock.")

apples = grocery_inventory.get("Apples")

if apples and apples[1] > 2:
    category, price, stock = apples
    grocery_inventory.pop(["Apples"]) 
    print("Apples removed from inventory due to high price.")
else:
    print("Updated inventory:", grocery_inventory)
    