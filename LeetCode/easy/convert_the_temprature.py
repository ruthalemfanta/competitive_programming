def convertTemperature(celsius):
    kalvin = celsius + 273.15
    fahernhiet = celsius * 1.80 + 32

    return [kalvin, fahernhiet]


result = convertTemperature(36.50)
