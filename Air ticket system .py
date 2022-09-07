print("Make a ticketing system")
print("The price of a single ticket is $100.\nFor children under 3 years old ,the ticket is free.")

print("Welcome to Vedu Air Ticket System!")
while True:
    name = input("Enter your Name here...")
    i = 0
    total = 0
    while True:
        age = input("Enter your Age here....")
        i += 1
        if age == "stop":
            break
        elif int(age) > 3:
            total += 100
        elif int(age) < 3:
            continue

        elif age == "stop":
            break

    print(name + ", yout total ticket price is " + str(total))
    continue
