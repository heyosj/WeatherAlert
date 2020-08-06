def weatherConversion(kelvin):
    # convert celcius to fahrenheit
    fahrenheit = (kelvin * 1.8) - 459.67
    roundedValue = round(fahrenheit)
    return roundedValue


def tempAndFeelsLike(tempForTheDay, feelsLike):
    tempOutside = weatherConversion(tempForTheDay)
    feelsLikeOutside = weatherConversion(feelsLike)

    print("Currently {0} outside, feels like {1}".format(
        tempOutside, feelsLikeOutside))


def highLowTemp(highTemp, lowTemp, humidity):
    highForTheDay = weatherConversion(highTemp)
    lowForTheDay = weatherConversion(lowTemp)

    print("The high for the day is {0} with a low of {1} and humidity of {2}%".format(
        highForTheDay, lowForTheDay, humidity))


def checkWeather(notGreatWeather):
    badWeather = ["thunderstorm", "rain"]
    if notGreatWeather in badWeather:
        print("It's raining outside, watch out")
    else:
        print("No rain, all good")
