# TukTuk Auto: Fare Calculator with Discount & Festive Tip

name = input("Kripya kar ke apna naam batayein. ")
distance = float(input("Kitni doori km tak jana hai? "))

fare = 0
discount = 0
tip = 0

if distance <= 0:
    print("Kripya sahi doori darj karein.")
elif distance > 30:
    print("Maaf kijiye, TukTuk Auto 30 km se zyada nahi jaata.")
else:
    if distance <= 5:
        fare = 60
    elif distance <= 10:
        fare = 120
    else:
        fare = distance * 15  # Rs.15 per km for >10 km

    # Discount conditions
    if distance in [10, 20, 30]:
        discount += 5
    if distance == 20:
        discount += 20
    elif distance == 30:
        discount += 25

    discount_amount = fare * (discount / 100)
    final_fare = fare - discount_amount

    # Ask for occasion
    occasion = input("Kya koi khas mauka hai? (diwali, newyear)")

    if occasion in ["diwali", "newyear"]:
        tip = 20
        print(f"Festive Tip: ₹{tip} (Diwali/New Year special)")

    total_payable = final_fare + tip

    # Show breakdown
    print(f"\n Original Fare: ₹{fare:.2f}")
    if discount > 0:
        print(f" Discount Applied ({discount}%): -₹{discount_amount:.2f}")
    print(f" Final Fare after Discount: ₹{final_fare:.2f}")
    if tip > 0:
        print(f"Tip Added: ₹{tip}")
    print(f"Total Amount Payable: ₹{total_payable:.2f}")

    # Ask if user wants to ride
    jayegaa = input("\nKya aap TukTuk Auto se jana chahenge? (True/False): ")

    if jayegaa == "Haa":
        print(f"Swagat hai {name} ji, TukTuk Auto me!")
    else:
        print("Hume khed hai ki hum aapki seva nahi kar sake.")

