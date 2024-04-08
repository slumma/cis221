#! PA2 Lough
# -- LA sam ogden
#! function for print statements
def menu_list():
    print("=" * 32)
    print("Available Jewelry Types:")
    print(
        """\t1. Ring
        2. Necklace
        3. Bracelet"""
    )
    print("=" * 32)


#! purchase summary func
def purchase_sum():
    print("=" * 64)
    print("\t\t   Summary of your purchase:")
    print("=" * 64)


#! total cost func
def ttl_cost(rings, necklaces, bracelets):

    # * Item costs
    ring_cost = 50.25
    necklace_cost = 75
    bracelet_cost = 40

    ring_cost = ring_cost * rings
    necklace_cost = necklace_cost * necklaces
    bracelet_cost = bracelet_cost * bracelets

    total_cost = ring_cost + necklace_cost + bracelet_cost

    return total_cost


#! total price func
def ttl_price(rings, necklaces, bracelets):

    # * Item prices
    ring_price = 100
    necklace_price = 150
    bracelet_price = 75

    ring_price = rings * ring_price
    necklace_price = necklaces * necklace_price
    bracelet_price = bracelets * bracelet_price

    total_price = ring_price + necklace_price + bracelet_price

    ttl_disc_price, discount = discount_app(total_price)

    return total_price, ttl_disc_price, discount


#! discount application func
def discount_app(price):
    # * checks if order price qualifies for a discount
    if price > 1000:
        discount = 0.15 * price
    elif price > 750:
        discount = 0.12 * price
    elif price > 500:
        discount = 0.1 * price

    ttl_disc_price = price - discount

    return ttl_disc_price, discount


#! item amount func
def item_amt(item):
    amt = int(input(f"How many {item} would you like:  "))

    return int(amt)


#! main func
def main():
    # * setting the item amounts to zero, no one starts with items in their cart
    ring_amt = 0
    necklace_amt = 0
    bracelet_amt = 0

    cart = [0, 0, 0]  # * rings , necklaces , bracelets

    print("Welcome to Sam's Jewelry Store!")
    ans = "y"

    while ans == "y" or ans == "yes":
        menu_list()  # * prints the item menu (function is above)
        choice = int(input("Choose the item number you wish to purchase:  "))

        if choice == 1:
            ring_num = int(input("Enter rings quantity: "))
            cart[0] += ring_num
        elif choice == 2:
            necklace_num = item_amt("necklaces")
            necklace_amt += necklace_num
        elif choice == 3:
            bracelet_num = item_amt("bracelets")
            bracelet_amt += bracelet_num
        else:
            print("Invalid entry. Please try again\n")
            continue

        # * formatting -- making it look better
        ans = input("Enter another item? (Y/N):  ").lower()
        print()

    price_xdisc, price_disc, disc = ttl_price(ring_amt, necklace_amt, bracelet_amt)
    cost = ttl_cost(ring_amt, necklace_amt, bracelet_amt)
    prof = price_disc - cost

    # * output statements

    purchase_sum()  # * prints summary menu
    print(f"Rings:\t\t\t\t\t\t{ring_amt:11}")
    print(f"Necklaces:\t\t\t\t\t{necklace_amt:11}")
    print(f"Bracelet:\t\t\t\t\t{bracelet_amt:11}")
    print("=" * 64)
    print(f"Total for your purchase:\t\t\t${price_xdisc:10,.2f}")
    print(f"Discount applied:\t\t\t\t${disc:10,.2f}")
    print(f"Final total purchase after discount:\t\t${price_disc:10,.2f}")
    print(f"Total profit from sale:\t\t\t\t${prof:10,.2f}")


main()
