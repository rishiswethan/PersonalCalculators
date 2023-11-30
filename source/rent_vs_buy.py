import time


# -------------------------------------------------------------------------------------------------------------------------------
"""
typical house in London
"""

# property_price_initial = interest_adjusted_property_price = property_price = 500000  # in pounds
#
# interest_rate = 0.055
# down_payment = 0.2
# tenure = 30
# yearly_savings_return = 0.06
# property_price_appreciation = 0.04
#
# rent_percentage = 0.05  # rental yield
# rent_maintenance_per = 0.1  # amount of the rent that goes to maintenance, property tax, etc.
#
# inflation = 0.02

# -------------------------------------------------------------------------------------------------------------------------------
"""
typical house in Chennai
"""

property_price_initial = interest_adjusted_property_price = property_price = 120000  # in pounds

interest_rate = 0.086
down_payment = 0.2
tenure = 30
yearly_savings_return = 0.1
property_price_appreciation = 0.07

rent_percentage = 0.023  # rental yield
rent_maintenance_per = 0.07  # amount of the rent that goes to maintenance, property tax, etc.

inflation = 0.04

# -------------------------------------------------------------------------------------------------------------------------------
"""
Calculate the monthly loan payment, monthly rent, and the amount saved at the end of the tenure if we rent and saved the difference.
"""

# - calculate the monthly loan payment
down_payment = property_price * down_payment
interest = ((property_price - down_payment) * interest_rate)
principal = (property_price - down_payment) / tenure

monthly_payment = (interest + principal) / 12

# - calculate the monthly rent
rent = (property_price * rent_percentage) / 12
rent_maintenance = rent * rent_maintenance_per  # amount lost to maintenance expenses every month by the landlord

print(f"\nDown payment: {down_payment}")
print(f"Monthly payment: {round(monthly_payment)}")
print(f"Yearly interest: {interest}\n\n")
print("__________________________________________________________________________________________________\n")

# - let's see how much we'll have at the end of the tenure if we rent and saved the difference
amount_saved = 0
total_interest_liability = 0
break_even_reached = False
break_even_point = 0
for i in range(tenure):

    amount_saved += amount_saved * yearly_savings_return  # savings return every year
    rent = (property_price * rent_percentage) / 12  # recalculate rent every year based on the property price
    rent_maintenance = rent * rent_maintenance_per  # rent maintenance increase every year

    for j in range(12):
        amount_saved += monthly_payment - rent + rent_maintenance  # amount saved every month

    print(f"Year {i + 1}:")
    print(f"Amount saved by not paying EMI: {round(amount_saved)}")
    print(f"Rent: {round(rent)}")
    print(f"Rent maintenance: {round(rent_maintenance)}\n")

    property_price += property_price * property_price_appreciation  # property price increase every year

    # calculate the interest adjusted property price
    total_interest_liability += interest
    interest_adjusted_property_price = property_price - total_interest_liability

    print("property_price: ", round(property_price))
    print("interest adjusted property_price: ", round(interest_adjusted_property_price), "\n\n\n")

    # check break even point
    if amount_saved > interest_adjusted_property_price and not break_even_reached:
        print(f"--- Break even point: {i + 1} years ---\n\n")
        break_even_reached = True
        break_even_point = i + 1

"""
Let's see how much we'll have at the end of the tenure if we rent and saved the difference or if we bought the house.
"""

print("__________________________________________________________________________________________________\n")

if not break_even_reached:
    print("Break even point never reached\n\n")
    difference = interest_adjusted_property_price - amount_saved
    print(f"Total amount wasted by renting: {round(difference)}\n\n")

else:
    print(f"Break even point reached in {break_even_point} years\n\n")
    difference = amount_saved - interest_adjusted_property_price
    print(f"Total amount saved by renting: {round(difference)}\n\n")

inflation_adjusted_difference = difference / ((1 + inflation) ** tenure)
print(f"Inflation adjusted difference: {round(inflation_adjusted_difference)}\n\n")
