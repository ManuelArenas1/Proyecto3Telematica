from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse


import boto3
import csv
import os

app = FastAPI()



# Configuración: usa tus parámetros reales
BUCKET_NAME = "telematica-weather-bucket"
TEMP_KEY = "output_temp/part-r-00000"
HUMI_KEY = "output_humi/part-r-00000"

s3 = boto3.client("s3")

def download_from_s3(key: str, local_path: str):
    s3.download_file(BUCKET_NAME, key, local_path)
    return local_path


@app.get("/results/json")
def get_results_json():
    temp_file = download_from_s3(TEMP_KEY, "temp_output.txt")
    humi_file = download_from_s3(HUMI_KEY, "humi_output.txt")

    def parse_file(path):
        entries = []
        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    entries.append({"Ciudad": parts[0], "value": float(parts[1])})
        return entries

    return {
        "temperatura": parse_file(temp_file),
        "humedad": parse_file(humi_file)
    }


@app.get("/results/csv")
def get_results_csv():
    temp_file = download_from_s3(TEMP_KEY, "temp_output.txt")
    humi_file = download_from_s3(HUMI_KEY, "humi_output.txt")

    # Convertir a CSV
    def convert_to_csv(txt_path, csv_path):
        with open(txt_path, "r") as infile, open(csv_path, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Ciudad", "value"])
            for line in infile:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    writer.writerow(parts)
        return csv_path

    temp_csv = convert_to_csv("temp_output.txt", "temperature.csv")
    humi_csv = convert_to_csv("humi_output.txt", "humidity.csv")

    return {
        "temperature_csv": "/download/temp",
        "humidity_csv": "/download/humi"
    }


@app.get("/download/temp")
def download_temp_csv():
    return FileResponse("temperature.csv", media_type="text/csv")


@app.get("/download/humi")
def download_humi_csv():
    return FileResponse("humidity.csv", media_type="text/csv")


