# Conversion function to keep my main file clean-ish

def unitValue(unit):
    if unit == "Square kilometer":
        num = 1 / 1.076e+7
    elif unit == "Square meter":
        num = 1 / 10.764
    elif unit == "Square mile":
        num = 1 / 2.788e+7
    elif unit == "Square yard":
        num = 1 / 9
    elif unit == "Square foot":
        num = 1
    elif unit == "Square inch":
        num = 144
    elif unit == "Hectare":
        num = 1 / 107639
    elif unit == "Acre":
        num = 1 / 43560
    elif unit == "Bit per second":
        num = 1
    elif unit == "Kilobit per second":
        num = 1 / 1000
    elif unit == "Kilobyte per second":
        num = 1 / 8000
    elif unit == "Kibibit per second":
        num = 1 / 1024
    elif unit == "Megabit per second":
        num = 1 / 1e+6
    elif unit == "Megabyte per second":
        num = 1 / 8e+6
    elif unit == "Mebibit per second":
        num = 1 / (1024 * 1024)
    elif unit == "Gigabit per second":
        num = 1 / 1e+9
    elif unit == "Gigabyte per second":
        num = 1 / 8e+9
    elif unit == "Gibibit per second":
        num = 1 / (1024 * 1024 * 1024)
    elif unit == "Terabit per second":
        num = 1 / 1e+12
    elif unit == "Terabyte per second":
        num = 1 / 8e+12
    elif unit == "Tebibit per second":
        num = 1 / (1024 * 1024 * 1024 * 1024)
    elif unit == "Bit":
        num = 8
    elif unit == "Kilobit":
        num = 1 / 125
    elif unit == "Kibibit":
        num = 1 / 128
    elif unit == "Megabit":
        num = 1 / 125000
    elif unit == "Mebibit":
        num = 1 / 131072
    elif unit == "Gigabit":
        num = 1 / 1.25e+8
    elif unit == "Gibibit":
        num = 1 / (128 * (1024 ** 2))
    elif unit == "Terabit":
        num = 1 / 1.25e+11
    elif unit == "Tebibit":
        num = 1 / (128 * (1024 ** 3))
    elif unit == "Petabit":
        num = 1 / 1.25e+14
    elif unit == "Pebibit":
        num = 1 / (128 * (1024 ** 4))
    elif unit == "Byte":
        num = 1
    elif unit == "Kilobyte":
        num = 1 / 1000
    elif unit == "Kibibyte":
        num = 1 / 1024
    elif unit == "Megabyte":
        num = 1 / 1e+6
    elif unit == "Mebibyte":
        num = 1 / (1024 ** 2)
    elif unit == "Gigabyte":
        num = 1 / 1e+9
    elif unit == "Gibibyte":
        num = 1 / (1024 ** 3)
    elif unit == "Terabyte":
        num = 1 / 1e+12
    elif unit == "Tebibyte":
        num = 1 / (1024 ** 4)
    elif unit == "Petabyte":
        num = 1 / 1e+15
    elif unit == "Pebibyte":
        num = 1 / (1024 ** 5)

    return num
