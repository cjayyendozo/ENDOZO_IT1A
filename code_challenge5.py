def cc5(): 

# FAHRENHEIT TO CELSIUS CONVERTER
        print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

        print("=========================================")

        fahrenheit = eval(input("Enter temperature in Fahrenheit ---> : "))
        celsius = ((fahrenheit - 32) * 5 / 9)

        print(f"{fahrenheit} °F converted to celsius is {round(celsius, 2)} °C.")