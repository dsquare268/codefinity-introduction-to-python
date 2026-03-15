#Discount 
discount_10 = 0.10
#define a function
def apply_discount(product_prices):
    prices_copy = product_prices.copy()
  
    for i in range(len(prices_copy)):
        product_price = product_prices[i]
    #check if price is over $2.00
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.9
    return prices_copy
    #Use for loop with index iteration to iterate over prices

  
# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

        
# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")