temperature = 30

if temperature < 30:
    print("The temperature is less than 30 degrees.")
elif temperature > 30:
    print("The temperature is greater than 30 degrees.")
else:
    print("The temperature is exactly 30 degrees.")


age = 19
has_license = True
drunk = True

if age >= 18:
    if has_license:
        if not drunk:
            print("You can drive.")
        else:
            print("You cannot drive because you are drunk.")