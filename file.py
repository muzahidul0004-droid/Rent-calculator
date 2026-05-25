# So here is , how things will be done
#input we need from the user
#Total rent
#Total food ordered 
# Total Elcetricity Spend
#Total charge per unit
#Person Living in room 

##Output
#how much Each person Have to pay


Rent= int(input("Enter Your Hostel/Flat Rent:"))
Food= int(input("Enter the amount of food has Ordered:"))
Electricity_spend= int(input("Enter how much electricity has spend:"))
Charge_per_unit= int(input("Enter the charge per unit:"))
Persons= int(input("Enter the number of persons Live in the hostel/flat:"))

total_Bill= Electricity_spend * Charge_per_unit
Output= (Food + Rent + total_Bill) // Persons

print("Each Person will pay = " , Output)
