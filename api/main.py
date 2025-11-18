from fastapi import FastAPI
import os

app = FastAPI()

CSV_PATH = os.path.join(os.path.dirname(__file__), "resultado.csv")

@app.get("/resultados")
def obtener_resultados():
    if not os.path.exists(CSV_PATH):
        return {"error": "resultado.csv no encontrado."}

    resultados = []

    with open(CSV_PATH, "r") as f:
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

            resultados.append({
                "ciudad": ciudad,
                "temperatura_promedio": temperatura
            })

    return resultados