start_number = 5
countdown_values = []

#Introduce new variable
current = start_number

#Start the loop to count down from start_number
while current > 0:
    print(current)
    #Append the current value before decrement
    countdown_values.append(current) 
    #Decrement the value going to the list
    current -= 1
    
#Output at the end of the loop.       
print("Discount countdown complete!")
print(countdown_values)        