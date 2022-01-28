import sys

KELVIN = 273


def pvtn():
    try:
        x = int(input("[1] new volume\n[2] new pressure\n[3] new tempture\n\nwhat are we sloving for:"))
    except Exception as e:
        print("[Error] invalid input")
        sys.exit(1)

    if (x == 1):
        init_temp = float(input("init tempture (C): "))
        final_temp = float(input("final tempture (C): "))
        init_vol = float(input("init volume (mL): "))
        init_temp += KELVIN
        final_temp += KELVIN
        if (init_temp > final_temp):
            return init_vol * (final_temp / init_temp)
        else:
            return init_vol_ * (init_temp / final_temp)

    if (x == 2):
        init_vol = float(input("init volume (mL): "))
        init_pressure = float(input("init pressure (kPa): "))




def make_pvtn_table():
    pass


def convert_units():
    pass

if __name__ == "__main__":
    print(pvtn())