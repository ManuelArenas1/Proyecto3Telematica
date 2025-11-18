import json
import csv
import glob

OUTPUT_FILE = "dataset/weather_dataset.csv"

fields = [
    "source",        # current o forecast
    "city",
    "date",
    "temp_c",
    "humidity",
    "wind_kph",
    "precip_mm",
    "condition"
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # --------------------------
    # Procesar CURRENT
    # --------------------------
    for filepath in glob.glob("dataset/raw_json/current/*.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        city = data["location"]["name"]
        current = data["current"]
        date = data["location"]["localtime"].split(" ")[0]

        writer.writerow({
            "source": "current",
            "city": city,
            "date": date,
            "temp_c": current["temp_c"],
            "humidity": current["humidity"],
            "wind_kph": current["wind_kph"],
            "precip_mm": current["precip_mm"],
            "condition": current["condition"]["text"]
        })

    # --------------------------
    # Procesar FORECAST
    # --------------------------
    for filepath in glob.glob("dataset/raw_json/forecast/*.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        city = data["location"]["name"]
        forecast_days = data["forecast"]["forecastday"]

        for day in forecast_days:
            writer.writerow({
                "source": "forecast",
                "city": city,
                "date": day["date"],
                "temp_c": day["day"]["avgtemp_c"],
                "humidity": day["day"]["avghumidity"],
                "wind_kph": day["day"]["maxwind_kph"],
                "precip_mm": day["day"]["totalprecip_mm"],
                "condition": day["day"]["condition"]["text"]
            })

print("CSV generado correctamente en:", OUTPUT_FILE)