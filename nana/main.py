number_of_hours_in_a_day = 24
name_of_unit = " hours "

def days_to_units(number_of_days):
    return(f"{number_of_days} days are {number_of_days * 24} {name_of_unit}")

ip_number_of_days = int(input("Enter the number of days: 10" ))
calculated_value = days_to_units(10)
print(calculated_value)
days_to_units(ip_number_of_days)

