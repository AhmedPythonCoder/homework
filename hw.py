
store_items = {
    "apple": 1.00,
    "banana": 0.50,
    "milk": 2.50,
    "bread": 1.75,
    "eggs": 3.00
}

def display_items():
    print("Available items in the store:")
    for item, price in store_items.items():
        print(f"{item.title()}: ${price:.2f}")
    print()

def add_to_cart(cart):
    while True:
        item = input("Enter the item to add to your cart (or type 'done' to finish): ").lower()
        if item == "done":
            break
        if item in store_items:
            quantity = int(input(f"How many {item}(s) would you like to add? "))
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
            print(f"Added {quantity} {item}(s) to your cart.")
        else:
            print(f"Sorry, {item} is not available in the store.")
    print()

def calculate_total(cart):

    total = 0
    for item, quantity in cart.items():
        total += store_items[item] * quantity
    return total

def shopping_store():
    cart = {}
    print("Welcome to the Shopping Store!")
    display_items()
    
    add_to_cart(cart)
    
    print( f"Your cart contains: {cart}")
    print(f'Your total will be: ${calculate_total(cart)}')
shopping_store()