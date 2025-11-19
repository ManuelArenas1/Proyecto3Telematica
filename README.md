# Proyecto 3 Telematica MAP_Reduce_Hadoop
Integrantes:
- Jose Manuel Carvajal Aristizabal
- Tomas Echavarria Gil
- Manuel Antonio Arenas Lara

## Descripcion del trabajo
En este trabajo se logra El uso de MapReduce para filtrar archivos csv sacados de la api the WEATHERAPI, en donde se filtra por diferentes valores como la temperatura, humedad, condicion del dia, viento, precipitacion.

Se filtra en la api de la siguiente manera:
- Current
- Forecast (14 dias de base)

de ahi se genera un csv, con los resultados obtenidos de la API y luego se filtra en 2 jobs

### Jobs

El primer job que hicimos fue sacar el promedio de temperatura de cada una de las ciudades elegidas,
los archivos para generados para la filtracion de estos se encuentran en la carpeta /mapreduce-app y llevan como nombre WeatherAverageTempDriver/Reducer/Mapper

y se genera un csv llamado temperatura.csv que muestra la siguiente información:
![alt text](image.png)

ademas se muestra en linea de la siguiente forma:
![alt text](image-1.png)

El segundo job saca el promedio de la humedad en cada una de las ciudades elegidas, este tambien se encuentra en la carpeta /mappreduce-app y los archivos generados fueron WeatherAverageHumidityDriver/Reducer/Mapper

este genera el csv llamado humedad.csv que muestra la siguiente informacion:
![alt text](image-2.png)

y en linea se muestra la siguiente información:
![alt text](image-3.png)