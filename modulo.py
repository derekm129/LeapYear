year_input = int(input("Enter a year:  "))

if year_input % 4 == 0:
    print("Remainder is 0 so ", year_input, "is a leap year!")

else:
    print(year_input, "Not a leap year!")

#  To find out if a year is a leap year or not,
# you can divide it by four and if the remainder is zero,
# it is a leap year.

