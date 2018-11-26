#!/usr/bin/env python3

import click
from weather import Weather, Unit


@click.command()
@click.option('--city', required=True, type=str, help='The name of the desired city.')
@click.option('--forecast', required=True, type=str, help='Forecast for amount of days: < TODAY | TODAY+N (1-9) >')
@click.option('-c', 'temp_unit', required=True, flag_value='-c', type=str, help='Display temperature in CELSIUS.')
@click.option('-f', 'temp_unit', required=True, flag_value='-f', type=str, help='Display temperature in FAHRENHEIT.')
def main(city, forecast, temp_unit):
    try:
        if temp_unit == '-c':
            temp_unit = 'CELSIUS'
        elif temp_unit == '-f':
            temp_unit = 'FAHRENHEIT'

        weather = Weather(unit=getattr(Unit, temp_unit))
        city_weather_info = weather.lookup_by_location(city)
        weather_condition = city_weather_info.condition.text
        forecasts = city_weather_info.forecast
        temperature_for_today = forecasts[0].low + '-' + forecasts[0].high

        click.echo(f"The weather in {city} TODAY is {weather_condition} "
                   f"with temperatures trailing from {temperature_for_today} {temp_unit}.")

        if len(forecast) > 5:
            forecast_days = int((forecast.split('+'))[1])
            click.echo(f"\nForecast for the next {forecast_days} days:\n")

            for day in range(forecast_days):
                date = forecasts[day].date
                weather_condition = forecasts[day].text
                day_temperature = forecasts[day].low + '-' + forecasts[day].high
                click.echo(f"{date} {weather_condition} with temperatures trailing from {day_temperature} {temp_unit}.\n")

    except AttributeError:
        click.echo(f"ERROR: There is no such city: {city}")


if __name__ == '__main__':
    main()
