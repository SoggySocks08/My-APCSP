import os, time

system = "cls" if os.name == "nt" else "clear"

os.system(system)

menu_dict = {"chicken sandwich": 5,
             "spicy sandwich": 8,
             "fries": 5,
             "da bev": 4,
             "fruit salad": 4
}

inventory_dict = {"chicken sandwich": 5,
             "spicy sandwich": 5,
             "fries": 5,
             "da bev": 5,
             "fruit salad": 5
}

restocks_dict = {"chicken sandwich": 0,
             "spicy sandwich": 0,
             "fries": 0,
             "da bev": 0,
             "fruit salad": 0
}

cust_ords = {}
yes_bank = ["yes", "sure", "yeah", "ye", "totally", "sure thing", "for sure", "i think so", "probably", "uh huh","si", "sí"]
no_bank = ["no", "nah", "absolutely not", "nope", "i don't think so", "nuh uh"]

RED = "\033[31m"
RESET = "\033[0m"

def take_order(name):
    order = []
    wTBA = "no"
    while wTBA in no_bank:
        os.system(system)
        display_menu()
        print(f"{name}'s order: {order}")
        item = input(f"Hello {name}, What would you like to order? (one at a time!) ").lower()
        if item in menu_dict:
            order.append(item)
        else:
            print(f"{RED}Sorry, we do not serve {item}! Please pick something from the menu!{RESET}")
            time.sleep(2)
            os.system(system)
            continue
        while True:
            wTBA = input("\nWill that be all? ").lower()
            if wTBA not in yes_bank and wTBA not in no_bank:
                print(f"{RED}Please enter yes or no.{RESET}")
                time.sleep(2)
            else:
                break
    cust_ords[name] = order

def calc_totals():
    totals = {}
    for name, order in cust_ords.items():
        cost = 0
        for item in order:
            cost += menu_dict[item]
        totals[name] = cost
    return(totals)

def calc_rev():
    revenue = 0
    for name, total in calc_totals().items():
        revenue += total
    for item, restocks in restocks_dict.items():
        for i in range (restocks):
            revenue -= (menu_dict[item] - 3) * 5
    return(revenue)

def display_menu():
    for item, price in menu_dict.items():
        print(f"{item.capitalize()}: ${price}")
    print()

def inv_func():
    for name, order in cust_ords.items():
        for item in order:
            if inventory_dict[item] > 0:
                inventory_dict[item] -= 1
            else:
                inventory_dict[item] = 4
                restocks_dict[item] += 1
    print("\nInventory:")
    for item, count in inventory_dict.items():
        print(f"{item}: {count}")
    print("\nRestocks:")
    for item, restocks in restocks_dict.items():
        print(f"{item}: {restocks}")

def display_ords():
    for name, order in cust_ords.items():
        print(f"{name}'s order: {order}")

def display_totals():
    print()
    for name, total in (calc_totals().items()):
        print(f"{name}'s total: ${total}")

def display_rev():
    print(f"\nDaily revenue: ${calc_rev()}\n")

def order_up():
    while True:
        try:
            orders = 0
            while True:
                orders = int(input("How many orders are being placed? "))
                if orders <= 0:
                    print(f"{RED}Please enter a number greater than 0.{RESET}")
                    time.sleep(2)
                    os.system(system)
                elif orders > 5:
                    print(f"{RED}Limit of 5 orders at one time.{RESET}")
                    time.sleep(2)
                    os.system(system)
                else:
                    break

            for i in range(orders):
                take_order(input("Please enter a name for the order: ").capitalize())
                os.system(system)
            break
        except ValueError:
            print(f"{RED}Please enter a number.{RESET}")
            time.sleep(2)
            os.system(system)


order_up()
display_ords()
display_totals()
inv_func()
display_rev()