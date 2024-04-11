def load_config(txt):
    prices = {}
    costs = {}
    with open(txt, 'r') as infile:
        for m in infile:
            name, price, cost = m.strip().split(',')
            if len(x) == 3:
                prices.update({name.lower() : eval(price)})
                costs.update({name.lower() : eval(cost)})
                #              ^ product            ^ value
            else:
                print('Error in number of values - Must be 3.')
                quit()
    return prices, costs
    
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

def save_summary(r, b, n, ttl, disc, final, prof):
    with open("transaction_summary.txt", 'w') as outfile:
        outfile.write("=" * 64)
        outfile.write("\n\t\t   Summary of your purchase:\n")
        outfile.write("=" * 64)
        outfile.write(f"\nRings:\t\t\t\t\t\t{r:11}\n")
        outfile.write(f"Bracelet:\t\t\t\t\t{b:11}\n")
        outfile.write(f"Necklaces:\t\t\t\t\t{n:11}\n")
        outfile.write("=" * 64)
        outfile.write(f"\nTotal for your purchase:\t\t\t\t${ttl:10,.2f}\n")
        outfile.write(f"Discount applied:\t\t\t\t\t\t${disc:10,.2f}\n")
        outfile.write(f"Final total purchase after discount:\t${final:10,.2f}\n")
        outfile.write(f"Total profit from sale:\t\t\t\t\t${prof:10,.2f}\n")
        outfile.write("=" * 64)

        outfile.close()

#! purchase summary func
def purchase_sum(r, b, n, ttl, disc, final, prof):
    print("=" * 64)
    print("\t\t   Summary of your purchase:")
    print("=" * 64)
    print(f"Rings:\t\t\t\t\t\t{r:11}")
    print(f"Bracelet:\t\t\t\t\t{b:11}")
    print(f"Necklaces:\t\t\t\t\t{n:11}")
    print("=" * 64)
    print(f"Total for your purchase:\t\t\t${ttl:10,.2f}")
    print(f"Discount applied:\t\t\t\t${disc:10,.2f}")
    print(f"Final total purchase after discount:\t\t${final:10,.2f}")
    print(f"Total profit from sale:\t\t\t\t${prof:10,.2f}")
    print("=" * 64)

#! discount application func
def dis_calc(ttl):
    # * checks if order ttl qualifies for a discount
    if ttl > 1000:
        discount = 0.15 * ttl
    elif ttl > 750:
        discount = 0.12 * ttl
    elif ttl > 500:
        discount = 0.1 * ttl
    ttl_disc_price = ttl - discount
    return ttl_disc_price, discount

#! item amount func
def item_amt(item):
    amt = int(input(f"How many {item} would you like:  "))
    return int(amt)

def calc_ttl(r, b, n, price_catalog):
    ttl = ((r * price_catalog.get("ring")) + (b * price_catalog.get("bracelet")) + (n * price_catalog.get("necklace")))
    return ttl
    
#! main func
def main():
    #establish dicts
    sales = {
        "rings" : 0,
        "bracelets" : 0,
        "necklaces" : 0
        } 
    
    prices, costs = load_config("config.txt")
    print("Welcome to Sam's Jewelry Store!")
    ans = "y"

    while ans in ['yes', 'y']: 
        menu_list()  # * prints the item menu (function is above)
        choice = int(input("Choose the item number you wish to purchase:  "))   #populates cart dict with values 
        if choice == 1:
            ring_num = item_amt('rings')
            sales["rings"] = sales.get("rings") + ring_num
        elif choice == 2:
            bracelet_num = item_amt("bracelets")
            sales["bracelets"] = sales.get("bracelets") + bracelet_num
        elif choice == 3:
            necklace_num = item_amt("necklaces")
            sales["necklaces"] = sales.get("necklaces") + necklace_num
        else:
            print("Invalid entry. Please try again\n")
            continue
        # * formatting -- making it look better
        ans = input("Enter another item? (Y/N):  ").lower()
    
    #calculations :D worked first try
    ttl = calc_ttl(sales.get("rings"), sales.get("bracelets"), sales.get("necklaces"), prices)
    priceWithDisc, disc = dis_calc(ttl)
    prof = priceWithDisc - calc_ttl(sales.get("rings"), sales.get("bracelets"), sales.get("necklaces"), costs)

    

    # * output statements

    purchase_sum(sales.get("rings"), sales.get("bracelets"), sales.get("necklaces"), ttl, disc, priceWithDisc, prof)  # * prints summary menu
    save_summary(sales.get("rings"), sales.get("bracelets"), sales.get("necklaces"), ttl, disc, priceWithDisc, prof)

    print("A file has been created with your transaction summary.")

main()

