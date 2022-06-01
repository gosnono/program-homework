import math
import wavelength

def wavelegth():


    if 350 < wavelength < 430:
        print("violet")
    elif 430< wavelength < 480:
        print("blue")
    elif 480< wavelength < 580:
        print("green")
    elif 580< wavelength < 640:
        print("orange")
    elif 640< wavelength < 760:
        print("red")
    else:
        print("infrared")

def main():
    h = float(6.626*10**(-34))
    c = float(3.0*(10**8))
    wavelength = (h*c)/(Eg)

    print(Eg(2))

if __name__ =="__main__":
    main()
