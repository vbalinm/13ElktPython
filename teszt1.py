def homerseklet():
    homersekletC = int(input("Kérék egy hőmérséklet értéket: "))

    if homersekletC <= 0:
        print("Szilárd halmazállapot.")
    elif homersekletC <= 100:
        print("Folyékony halmazállapot.")
    else: 
        print("Lég halmazállapot.")

homerseklet()