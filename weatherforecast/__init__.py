from . import open_meteo_forecast_api as forecast 
from . import analyse_sample as analyse

def get(location: str = "tokyo") -> dict:
    return forecast.get(location)

def apply(temperature_list: list) -> dict:
    return analyse.apply(temperature_list)

def main() -> None:
    result_dict = get()
    print(result_dict["location"])
    print(result_dict["time"])
    print(result_dict["temperature_2m"])

