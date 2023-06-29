import java.util.Arrays;
import java.util.ArrayList;

public class JavaTest { // The name of your class must match the name of your file EXACTLY!
    // This is a comment

    // Somewhere in your project, you need a main method
    public static void main(String[] args) {
        // Define some variables
        int x = 10; // Creating a variable called "x" that has to be an integer (int)
        int y = 15;
        int z = x + y;
        boolean isHappy = false; // Variables follow the camelCase convention; same with methods
        System.out.println("The value of z is "+ z);
        System.out.println("Hello everybody!");

        // If statement demo
        if (isHappy == true) {
            System.out.println("I'm glad you're happy!");
        } else {
            System.out.println("I'm sorry - I hope you can cheer up soon....");
        }

        // For loop demo - display odd values
        for (int i = 1; i <= 100; i += 2) {
            System.out.println(i);
        }

        // Arrays demo
        int[] myIntegers = {1, 2, 3, 5, 8}; // To define a fixed array of values, you have to use the {}
        System.out.println(Arrays.toString(myIntegers));

        // Unfortunately, once an array is defined, it stays fixed in size, so you can't add or remove values
        // ArrayLists will do that for us
        ArrayList<Integer> integerList = new ArrayList<Integer>();
        integerList.add(2); // add method adds to the list
        integerList.add(10);
        System.out.println(integerList);
    }
}