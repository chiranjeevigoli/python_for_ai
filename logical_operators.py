age = 25

has_license = True

drunk = False

# and - both must be True

can_drive = age >= 18 and has_license == True and drunk
print(can_drive)

# or - at lease one must be True

day = "Sunday"

is_weekend = day == "Saturday" or day == "Sunday"

print(is_weekend)


# not - opposite of boolean value not(True) is False and not(False) is True

a = not True
a