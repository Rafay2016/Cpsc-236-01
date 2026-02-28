def feet_to_meters(feet):
    return round(feet * 0.3408, 2)

def meters_to_feet(meters):
    return round(meters / 0.3408, 2)

def display_title():
    print("Feet and Meters Converter\n")

def display_menu():
    print("Conversions Menu:")
    print("a.\tFeet to Meters")
    print("b.\tMeters to Feet")

    