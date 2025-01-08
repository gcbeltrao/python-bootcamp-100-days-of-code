MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def check(coffee):
    global resources
    global MENU
    for ingredients in resources:
        if resources[ingredients] > MENU[coffee]["ingredients"][ingredients]:
            return True
        else:
            return False


def report_resources():
    for ingredient in resources:
        if ingredient == "coffee":
            print(f"{ingredient} : {resources[ingredient]} g")
        else:
            print(f"{ingredient} : {resources[ingredient]} ml")
    print(f"Money: ${profit}")


def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_order(coffee):
    if check(coffee):
        global profit
        total = payment()
        if total >= MENU[coffee]["cost"]:
            change = "{:.2f}".format(round(total - MENU[coffee]["cost"], 2))
            print(f"Here is ${change} in change.")
            profit += MENU[coffee]["cost"]
            for ingredients in resources:
                left = resources[ingredients] - MENU[coffee]["ingredients"][ingredients]
                resources[ingredients] = left
        else:
            print("Sorry that is not enough money. Money refunded.")
    else:
        print("Sorry, there is not enough resources")


def attend_client():
    must_attend = True
    profit = 0
    while must_attend:
        order = input("What would you like? (espresso/ latte/ cappuccino):")
        if order == "espresso":
            check_order(order)
        elif order == "cappuccino":
            check_order(order)
        elif order == "latte":
            check_order(order)
        elif order == "report":
            report_resources()
        elif order == "fill":
            global resources
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }

        elif order == "off":
            must_attend = False
        else:
            print("Invalid key, please try again.")


attend_client()
