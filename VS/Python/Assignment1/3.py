feet = float(input("Enter length in feet: "))
options = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]
conversions = [feet * 12, feet / 3, feet / 5280, feet * 304.8, feet * 30.48, feet * 0.3048, feet * 0.0003048]

for i in range(len(options)):
    print(f"{i+1}. Convert to {options[i]}")

choice = int(input("Enter your choice (1-7): "))

if 1 <= choice <= 7:
    print(f"{feet} feet is {conversions[choice - 1]:.5f} {options[choice - 1].lower()}")
else:
    print("Invalid choice")