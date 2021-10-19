weight = 41.5

#Ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print("cost: $" + str(cost_ground))
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
  print("cost: $" + str(cost_ground))
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
  print("cost: $" + str(cost_ground))
elif weight >= 10:
  cost_ground = weight * 4.75 + 20
  print("cost: $" + str(cost_ground))

cost_premium = 125.0
print("Ground Shipping premium: " + str(cost_premium))

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
  print("cost drone: $" + str(cost_drone))
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
  print("cost drone: $" + str(cost_drone))
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
  print("cost drone: $" + str(cost_drone))
elif weight >= 10:
  cost_drone = weight * 14.25
  print("cost drone: $" + str(cost_drone))