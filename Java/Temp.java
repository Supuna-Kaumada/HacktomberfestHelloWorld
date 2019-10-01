import java.util.Scanner;

public class Temp { // convertion of fahrenheit to celcius and vise versa

    public static void main(String[] args) {
        double celcius, fahrenheit;
        Scanner in = new Scanner(System.in);

        System.out.print("Enter the value of temperature in degree celcius: ");
        celcius = in.nextDouble();
        fahrenheit = celcius * 9 / 5 + 32; // convertion formula for celcius to fahrenheit
        System.out.printf(celcius+" °C = %.1f °F\n", fahrenheit);

        System.out.print("Now enter the value of temperature in degree fahrenheit: ");
        fahrenheit = in.nextDouble();
        celcius = (fahrenheit - 32) * 5 / 9; // formula of fahrenheit to celcius
        System.out.printf(fahrenheit +" °F = %.1f °C\n", celcius);
    }
}
