Temperature = int(input("Temperature: "))

class TempConvertion:
    def __init__(self, temp):
        self.__temp = temp

    def Celsius(self):
        print("Celsius to Fahrenheit: ", (temperature-32)*5/9)
        print("Celsius to Kelvin: ", temperature-273.13)

    def Kelvin(self):
        print("Kelvin to Fahrenheit: ", (temperature + 459.67) / 1.8)
        print("Kelvin to Celsius: ", temperature+273.15)

    def Fahrenheit(self):
        print("Fahrenheit to Celsius: ", (temperature * 9 / 5) + 32)
        print("Fahrenheit to kelvin: ", (1.8*temperature)-459.67)

Celcius = TempConvertion(temperature)
celcius.celsius()
fahrenheit = TempConvertion(temperature)
fahren.Fahrenheit()
kelvin = TempConvertion(temperature)
kelv.Kelvin()



