def add_item(cart,item):
    cart.append(item)
    print("Item added to cart.")
    
def remove_item(cart, item):
    cart.remove(item)
    print("Item removed from cart.")
    
def update_quantity(cart,item,new_quantity):
    for i in range(len(cart)):
        if cart[i] == item:
            cart[i] = (item, new_quantity)
            print("Item quantity updated")
            break
    else:
        print("Item not found in cart.")
        
def print_cart(cart):
    for item in cart:
        print(item)

cart = []

while True:
    print("1. Add Items")
    print("2. Remove Items")
    print("3. Update quatity")
    print("4. Print cart")
    print("5. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        item = input("Enter item name: ")
        add_item(cart,item)
    elif choice == 2:
        item = input("Enter item name: ")
        remove_item(cart, item)
    elif choice == 3:
        item = input("Enter item name: ")
        new_quantity = int(input("Enter new quantity: "))
        update_quantity(cart, item, new_quantity)
    elif choice == 4:
        print_cart(cart)
    elif choice == 5:
            break
    else:
        print("Invalid choice.")