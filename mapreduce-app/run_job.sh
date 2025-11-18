#!/bin/bash

echo "Ejecutando job MapReduce..."
hadoop jar temperature-job.jar com.eafit.hadoop.WeatherAverageTempDriver /input /output

echo "Exportando resultado desde HDFS..."
hdfs dfs -get -f /output/part-r-00000 resultado.csv

echo "Moviendo resultado a la API..."
mv resultado.csv ../api/resultado.csv

echo "Listo. CSV actualizado."