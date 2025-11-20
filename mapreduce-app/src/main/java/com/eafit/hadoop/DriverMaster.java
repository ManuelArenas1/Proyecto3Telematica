package com.eafit.hadoop;

public class DriverMaster {

    public static void main(String[] args) throws Exception {

        if (args.length < 3) {
            System.err.println("Uso opción 1: <temp|hum|both> <input> <output>");
            System.err.println("Uso opción 2 (both): <both> <input> <output_temp> <output_hum>");
            System.exit(1);
        }

        String job = args[0];
        String input = args[1];

        switch (job) {
            case "temp":
                if (args.length != 3) {
                    System.err.println("Para temp: <temp> <input> <output>");
                    System.exit(1);
                }
                System.out.println("==> Ejecutando job de TEMPERATURA...");
                WeatherAverageTempDriver.main(new String[]{input, args[2]});
                System.out.println("==> Temperatura completada exitosamente.");
                break;

            case "hum":
                if (args.length != 3) {
                    System.err.println("Para hum: <hum> <input> <output>");
                    System.exit(1);
                }
                System.out.println("==> Ejecutando job de HUMEDAD...");
                WeatherAverageHumidityDriver.main(new String[]{input, args[2]});
                System.out.println("==> Humedad completada exitosamente.");
                break;

            case "both":
                if (args.length != 4) {
                    System.err.println("Para both: <both> <input> <output_temp> <output_hum>");
                    System.exit(1);
                }
                String outputTemp = args[2];
                String outputHum = args[3];
                
                System.out.println("==> Ejecutando AMBOS jobs...");
                System.out.println("==> 1/2 - Procesando TEMPERATURA...");
                int tempResult = WeatherAverageTempDriver.main(new String[]{input, outputTemp});
                
                if (tempResult != 0) {
                    System.err.println("ERROR: Falló el job de temperatura");
                    System.exit(tempResult);
                }
                
                System.out.println("==> 2/2 - Procesando HUMEDAD...");
                int humResult = WeatherAverageHumidityDriver.main(new String[]{input, outputHum});
                
                if (humResult != 0) {
                    System.err.println("ERROR: Falló el job de humedad");
                    System.exit(humResult);
                }
                
                System.out.println("==> Ambos jobs completados exitosamente!");
                break;

            default:
                System.err.println("Job inválido. Use: temp, hum o both");
                System.exit(1);
        }
    }
}