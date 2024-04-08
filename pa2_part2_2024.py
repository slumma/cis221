cars = 0

passengers = int(input("Enter the number of passengers:  "))

van_pass = passengers // 15

extras = passengers % 15

if extras > 0:
    if extras <= 3:
        print("You will need additional space for less than 4 passengers.")
        extra_car = input("Do you want to use a car? (Y/N) ").lower()

        if extra_car == "y":
            cars += 1
        elif extra_car == "n":
            print("We will add another van to the reservation.")
            van_pass += 1
    elif extras > 3:
        van_pass += 1


if cars > 0:
    print(f"\nThis trip will require {van_pass} vans and {cars} car.")
else:
    print(f"\nVans needed for this trip: {van_pass}")
