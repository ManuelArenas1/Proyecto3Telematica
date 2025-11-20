package com.eafit.hadoop;



public class DriverMaster {

    public static void main(String[] args) throws Exception {



        if (args.length < 3) {

            System.err.println("Uso: <temp|hum> <input> <output>");

            System.exit(1);

        }



        String job = args[0];

        String input = args[1];

        String output = args[2];



        switch (job) {

            case "temp":

                WeatherAverageTempDriver.main(new String[]{input, output});

                break;



            case "hum":

                WeatherAverageHumidityDriver.main(new String[]{input, output});

                break;



            default:

                System.err.println("Job inválido. Use: temp o hum");

                System.exit(1);

        }

    }

}