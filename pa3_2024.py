def load_config(txt):
    sales_price = {}
    with open(txt, 'r') as infile:
        for m in infile:
            x = m.strip().split(',')
            if len(x) == 3:
                sales_price.update({x[0].lower() : [eval(x[1]),eval(x[2])]})
                #                   ^ product            ^ price      ^ cost
            else:
                print('Error in number of values - Must be 5.')
                quit()
                
    return sales_price

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
    sales = {
        "rings" : 0,
        "necklaces" : 0,
        "bracelets" : 0
        } 

    print("Welcome to Sam's Jewelry Store!")
    ans = "y"

    while ans in ['yes', 'y']:
        menu_list()  # * prints the item menu (function is above)
        choice = int(input("Choose the item number you wish to purchase:  "))
        if choice == 1:
            ring_num = int(input("Enter rings quantity: "))
            sales["rings"] = sales.get("rings", 0) + ring_num
        elif choice == 2:
            necklace_num = item_amt("necklaces")
            sales["necklaces"] = sales.get("necklaces", 0) + necklace_num
        elif choice == 3:
            bracelet_num = item_amt("bracelets")
            sales["bracelets"] = sales.get("bracelets", 0) + bracelet_num
        else:
            print("Invalid entry. Please try again\n")
            continue
        # * formatting -- making it look better
        ans = input("Enter another item? (Y/N):  ").lower()
            
    
    prices = load_config("config.txt")
    
    

    # * output statements

    purchase_sum()  # * prints summary menu
    print(f"Rings:\t\t\t\t\t\t{sales.get("rings"):11}")
    print(f"Necklaces:\t\t\t\t\t{sales.get("necklaces"):11}")
    print(f"Bracelet:\t\t\t\t\t{sales.get("bracelets"):11}")
    print("=" * 64)
    print(f"Total for your purchase:\t\t\t${price_xdisc:10,.2f}")
    print(f"Discount applied:\t\t\t\t${disc:10,.2f}")
    print(f"Final total purchase after discount:\t\t${price_disc:10,.2f}")
    print(f"Total profit from sale:\t\t\t\t${prof:10,.2f}")


main()

    
