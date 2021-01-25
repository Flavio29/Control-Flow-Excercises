weight = 41.5

# Ground Shipping

if weight <= 2:
  cost_ground = (1.50 * weight) + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = (3.50 * weight) + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = (4.00 * weight) + 20.00
elif weight > 10:
  cost_ground = (4.75 * weight) + 20.00
else:
  print("Submit your package's weight.") 
print("Ground Shipping is $" + str(cost_ground))

# Premiun Ground Shipping

premium_shipping = 125
print("Ground Premium Shipping is $" + str(premium_shipping))

# Drone Shipping

if weight <= 2:
  cost_drone = (4.50 * weight) + 0.00
elif weight > 2 and weight <= 6:
  cost_drone = (9.00 * weight) + 0.00
elif weight > 6 and weight <= 10:
  cost_drone = (12.00 * weight) + 0.00
elif weight > 10:
  cost_drone = (14.25 * weight) + 0.00
else:
  print("Submit your package's weight.") 
print("Drone Shipping is $" + str(cost_drone))