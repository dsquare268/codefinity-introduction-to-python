prices = [29.99, 45.50, 12.75, 38.20]

discount_10 = 0.10
discount_20 = 0.20
discount_15 = 0.15
discount_05 = 0.05

#Iterate oveer the list of prices using range(len())
for cost in range(len(prices)):
    if cost == 0:
        prices[cost] -= prices[cost] * discount_10
        print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")
    if cost == 1:
        prices[cost] -= prices[cost] * discount_20
        print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")
    if cost == 2:
        prices[cost] -= prices[cost] * discount_15
        print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")
    if cost == 3:
        prices[cost] -= prices[cost] * discount_05
        print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")