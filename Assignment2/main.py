import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = #####
cashier_instance = ######




def main():
    while True:
        # Display menu
        print("\nWelcome to the Sandwich Shop!")
        print("Menu:")
        for size, details in recipes.items():
            print(f"{size.capitalize()} - ${details['cost']}")

        # Get user input
        choice = input("\nWhat size sandwich would you like? (small/medium/large or 'exit' to quit): ").lower()
        
        if choice == "exit":
            print("Goodbye!")
            break

        # Validate choice
        if choice not in recipes:
            print("Invalid choice. Please select from the menu.")
            continue

        # Check if resources are available
        sandwich_ingredients = recipes[choice]["ingredients"]
        if not sandwich_maker_instance.check_resources(sandwich_ingredients):
            print("Sorry, not enough ingredients available.")
            continue

        # Process payment
        cost = recipes[choice]["cost"]
        print(f"The cost of a {choice} sandwich is ${cost:.2f}")
        total_money = cashier_instance.process_coins()

        if not cashier_instance.transaction_result(total_money, cost):
            print("Insufficient funds. Transaction failed.")
            continue

        # Make the sandwich
        sandwich_maker_instance.make_sandwich(choice, sandwich_ingredients)
        print(f"Enjoy your {choice} sandwich!")

if __name__=="__main__":
    main()
