#!/bin/bash

JAR="target/mapreduce-app-1.0.jar"
API_DIR="../api"

run_temperature() {
    echo "Ejecutando job de temperatura..."
    hadoop jar $JAR com.eafit.hadoop.WeatherAverageTempDriver /input /output_temp

    echo "Exportando resultado temperatura..."
    hdfs dfs -get -f /output_temp/part-r-00000 temperatura.csv

    echo "Moviendo temperatura.csv a API..."
    mv temperatura.csv $API_DIR/temperatura.csv
}

run_humidity() {
    echo "Ejecutando job de humedad..."
    hadoop jar $JAR com.eafit.hadoop.WeatherAverageHumidityDriver /input /output_humi

    echo "Exportando resultado humedad..."
    hdfs dfs -get -f /output_humi/part-r-00000 humedad.csv

    echo "Moviendo humedad.csv a API..."
    mv humedad.csv $API_DIR/humedad.csv
}

run_all() {
    run_temperature
    run_humidity
}

echo "Selecciona el job:"
echo "1) Temperatura"
echo "2) Humedad"
echo "3) Ambos"
read -p "Opción: " opt

case $opt in
    1) run_temperature ;;
    2) run_humidity ;;
    3) run_all ;;
    *) echo "Opción inválida" ;;
esac

echo "Listo."