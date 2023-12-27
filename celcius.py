# Formula is ( Cels x 9/5 + 32 )

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# This is my logic code
Temprature = float(input("Enter the Temprature in celsius : "))

Celsius_to_far = celsius_to_fahrenheit(Temprature)

print(Temprature,"C in fahrenheit is" ,Celsius_to_far,"F")