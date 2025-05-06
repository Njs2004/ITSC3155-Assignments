import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes

sandwich_maker = SandwichMaker(resources)
cashier = Cashier()

def main():
    while True:
        choice = input("What size sandwich would you like? (small/medium/large/off): ").lower()
        if choice == "off":
            print("Turning off machine. Goodbye!")
            break
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker.check_resources(sandwich["ingredients"]):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
