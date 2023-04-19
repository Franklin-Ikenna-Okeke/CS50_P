def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   #Converts a dollar amount in string format to a float.
   return float(d.strip("$"))


def percent_to_float(p):
    #Converts a percentage in string format to a float.
    return float(p.strip("%")) / 100


main()