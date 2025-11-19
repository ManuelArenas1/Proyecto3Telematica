from fastapi import FastAPI
import os

app = FastAPI()

CSV_PATH_TEMP = os.path.join(os.path.dirname(__file__), "temperatura.csv")
CSV_PATH_HUM = os.path.join(os.path.dirname(__file__), "humedad.csv")

@app.get("/temperaturas")
def obtener_temperaturas():
    if not os.path.exists(CSV_PATH_TEMP):
        return {"error": "temperatura.csv no encontrado."}

    resultados_temperatura = []

    with open(CSV_PATH_TEMP, "r") as f:
        for linea in f:
            linea = linea.strip()

            if not linea:
                continue

            # separar por tabulacion
            partes = linea.split("\t")

            if len(partes) != 2:
                continue

            ciudad, temperatura = partes

            try:
                temperatura = float(temperatura)
            except:
                continue

            resultados_temperatura.append({
                "ciudad": ciudad,
                "temperatura_promedio": temperatura
            })
        return resultados_temperatura
        
@app.get("/humedades")
def obtener_humedades():
    
    if not os.path.exists(CSV_PATH_HUM):
        return {"error": "humedad.csv no encontrado."}
    
    resultados_humedad = []
    
    with open(CSV_PATH_HUM, "r") as f:
        for linea in f:
            linea = linea.strip()
    
            if not linea:
                continue
    
            # separar por tabulacion
            partes = linea.split("\t")
    
            if len(partes) != 2:
                continue
    
            ciudad, humedad = partes
    
            try:
                humedad = float(humedad)
            except:
                continue
    
            resultados_humedad.append({
                "ciudad": ciudad,
                "humedad_promedio": humedad
            })  
        
    return resultados_humedad
            
        

    