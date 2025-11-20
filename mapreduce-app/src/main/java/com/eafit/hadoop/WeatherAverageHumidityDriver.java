package com.eafit.hadoop;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WeatherAverageHumidityDriver {

    public static int main(String[] args) throws Exception {

        if (args.length != 2) {
            System.err.println("Uso: WeatherAverageHumidityDriver <input> <output>");
            return -1;
        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Average Humidity by City");

        job.setJarByClass(WeatherAverageHumidityDriver.class);

        job.setMapperClass(WeatherAverageHumidityMapper.class);
        job.setReducerClass(WeatherAverageHumidityReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);
        job.setNumReduceTasks(1);


        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        return job.waitForCompletion(true) ? 0 : 1;
    }
}