package com.eafit.hadoop;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import java.io.IOException;

public class WeatherAverageTempMapper 
        extends Mapper<LongWritable, Text, Text, FloatWritable> {

    private Text city = new Text();
    private FloatWritable temperature = new FloatWritable();

    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        // Saltar encabezado
        String line = value.toString();
        if (line.startsWith("source")) return;

        // Dividir CSV
        String[] parts = line.split(",");

        // Formato esperado:
        // source,city,date,temp_c,humidity,wind_kph,precip_mm,condition
        if (parts.length < 4) return;

        String cityName = parts[1];
        float tempC;

        try {
            tempC = Float.parseFloat(parts[3]);
        } catch (NumberFormatException e) {
            return; // evitar líneas dañadas
        }

        city.set(cityName);
        temperature.set(tempC);

        context.write(city, temperature);
    }
}