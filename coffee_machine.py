coffee = {
    #[price, water, caffee, milk]
    "espresso": [1.5, 50, 18, 0],
    "latte": [2.5, 200, 24, 150],
    "cappuccino": [3, 250, 24, 100]
}

# TODO: 1 Create choosing coffe interface function
#  "What would you like?" (espresso/latte/capuccino)
def select_coffee():
    inserted_coffee = input("What would you like? (espresso 1.5/latte 2.5/cappuccino 3) ").lower()
    return inserted_coffee


# TODO: 2 Verify if enough available resources for selected coffe
def enough_resources_for_coffee():
    enough_resources = True
    if selected_coffee in list(coffee.keys()):
        if remaining_water < coffee[selected_coffee][1] or remaining_coffee < coffee[selected_coffee][2] \
                or remaining_milk < coffee[selected_coffee][3]:
            enough_resources = False
            print("Not enough resources to make selected drink")
    elif selected_coffee != "report":
        if selected_coffee != "off":
            print("Invalid drink selected ")
        enough_resources = False
    return enough_resources


# TODO: 3 Create money processing function
# Calculates inserted coins and compares to selected coffe price
def coffee_payment():
    global money
    make_coffee = True
    print("Insert money")
    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickel = int(input("How many nickels? "))
    num_pennies = int(input("How many pennies "))
    inserted_amount = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickel * 0.05) + (num_pennies * 0.01)
    if selected_coffee in list(coffee.keys()):
        if inserted_amount < coffee[selected_coffee][0]:
            print("Not enough money")
            make_coffee = False
        elif inserted_amount >= coffee[selected_coffee][0]:
            refund = round(inserted_amount - coffee[selected_coffee][0], 2)
            if refund > 0:
                print(f"Refund: ${refund}")
            money += coffee[selected_coffee][0]
    return make_coffee


# TODO: 4  coffee resource consumption function
# Subtract used resources from available resources
def resources_consumption():
    global remaining_water, remaining_coffee, remaining_milk
    remaining_water -= coffee[selected_coffee][1]
    remaining_coffee -= coffee[selected_coffee][2]
    remaining_milk -= coffee[selected_coffee][3]


# TODO: 5 Create report function
# # Display how much resource from each item is left
def report():
    print(f"Remaining water: {remaining_water}ml")
    print(f"Remaining coffee: {remaining_coffee}g")
    print(f"Remaining milk: {remaining_milk}ml")
    print(f"Money: ${money}")


remaining_water = 300
remaining_milk = 200
remaining_coffee = 100
money = 0


selected_coffee = ""
while selected_coffee != "off":
    selected_coffee = select_coffee()
    if selected_coffee == "report":
        report()
    else:
        is_enough = enough_resources_for_coffee()
        if is_enough and coffee_payment():
            print(f"Here is your {selected_coffee}. Enjoy!")
            resources_consumption()
