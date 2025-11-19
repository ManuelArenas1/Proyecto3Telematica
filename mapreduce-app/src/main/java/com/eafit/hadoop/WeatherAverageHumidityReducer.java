package com.eafit.hadoop;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import java.io.IOException;

public class WeatherAverageHumidityReducer 
        extends Reducer<Text, FloatWritable, Text, FloatWritable> {

    @Override
    protected void reduce(Text key, Iterable<FloatWritable> values, Context context)
            throws IOException, InterruptedException {

        float sum = 0;
        int count = 0;

        for (FloatWritable v : values) {
            sum += v.get();
            count++;
        }

        float avg = sum / count;

        context.write(key, new FloatWritable(avg));
    }
}