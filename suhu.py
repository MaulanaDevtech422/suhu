def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

def celcius_to_reamur(celcius):
    reamur = celcius * 4/5
    return reamur

def main():
    print ("            \033[0;32m+++++++++++++++++++++++++++")
    print ("            +  SUHU BY MaulanDevtech  +")
    print ("            +++++++++++++++++++++++++++")
    print ("-----------------------------------------------------")
    print ("-     aplikasi ini dibuat untuk tujuan menghitun    -")
    print ("-  sebuah suhu celcius,fahrenhait,kelvin & reamur   -")
    print ("-----------------------------------------------------")

    celcius = float(input("\033[0;33mMasukkan suhu dalam Celcius: "))
    fahrenheit = celcius_to_fahrenheit(celcius)
    kelvin = celcius_to_kelvin(celcius)
    reamur = celcius_to_reamur(celcius)
    print ("\033[0;36m-----------------------------------")
    print(f"- {celcius} Celcius = {fahrenheit:.2f} Fahrenheit  -")
    print(f"- {celcius} Celcius = {kelvin:.2f} Kelvin     -")
    print(f"- {celcius} Celcius = {reamur:.2f} Reamur       -")                             print ("-----------------------------------")
if __name__ == "__main__":
    main()
