# Conversion function to keep my main file clean-ish

def unitValue(unit):

    # Area units
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

    # DTR units
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

    # DS units
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

    # Energy units
    elif unit == "Joule":
        num = 1
    elif unit == "Kilojoule":
        num = 1 / 1000
    elif unit == "Gram calorie":
        num = 1 / 4.184
    elif unit == "Kilocalorie":
        num = 1 / 4184
    elif unit == "Watt hour":
        num = 1 / 3600
    elif unit == "Kilowatt hour":
        num = 1 / 3.6e+6
    elif unit == "Electronvolt":
        num = 6241506363094000000
    elif unit == "British thermal unit":
        num = 9.478169879e-9
    elif unit == "US therm":
        num = 9.480434279e-9
    elif unit == "Foot-pound":
        num = 0.7375621493

    # Frequency units
    elif unit == "Hertz":
        num = 1
    elif unit == "Kilohertz":
        num = 1 / 1000
    elif unit == "Megahertz":
        num = 1 / 1e+6
    elif unit == "Gigahertz":
        num = 1 / 1e+9

    # FE units
    elif unit == "Miles per gallon":
        num = 2.3521458329
    elif unit == "Miles per gallon (Imperial)":
        num = 2.8248093628
    elif unit == "Kilometer per liter":
        num = 1
    elif unit == "Liter per 100 kilometers":
        num = 100

    # Length units
    elif unit == "Kilometer":
        num = 0.0003048
    elif unit == "Meter":
        num = 0.3048
    elif unit == "Centimeter":
        num = 30.48
    elif unit == "Millimeter":
        num = 304.8
    elif unit == "Micrometer":
        num = 304800
    elif unit == "Nanometer":
        num = 3.048e+8
    elif unit == "Mile":
        num = 1 / 5280
    elif unit == "Yard":
        num = 1 / 3
    elif unit == "Foot":
        num = 1
    elif unit == "Inch":
        num = 12
    elif unit == "Nautical mile":
        num = 0.0001645788

    # Mass units
    

    return num
