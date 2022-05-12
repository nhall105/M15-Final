# Equations for temperature because they are too different

def tempConv(unit1, unit2, num):
    if unit1 == unit2:
        return num
    elif unit1 == "Celsius" and unit2 == "Fahrenheit":
        return (num * (9 / 5)) + 32
    elif unit1 == "Celsius" and unit2 == "Kelvin":
        return num + 273.15
    elif unit1 == "Fahrenheit" and unit2 == "Celsius":
        return (num - 32) * (5 / 9)
    elif unit1 == "Fahrenheit" and unit2 == "Kelvin":
        return (num - 32) * (5 / 9) + 273.15
    elif unit1 == "Kelvin" and unit2 == "Celsius":
        return num - 273.15
    elif unit1 == "Kelvin" and unit2 == "Fahrenheit":
        return (num -  273.15) * (9 / 5) + 32
