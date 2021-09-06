number_of_hours_in_a_day = 24
name_of_unit = " hours "
ip_number_of_days = 0

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * 24} {name_of_unit}"


def validate_and_execute():
    try:
        ip_number_of_days = int(input("Enter the number of days: " ))        
        if (ip_number_of_days > 0):
            calculated_value = days_to_units(ip_number_of_days)
            print(calculated_value)
        elif ip_number_of_days == 0:
            print("Number of days should not be 0")
        else:
            print("You entered a -ve number, please don't do that!")    
    except ValueError:
        print("Number of days should be a number and > 1")
        
validate_and_execute()
