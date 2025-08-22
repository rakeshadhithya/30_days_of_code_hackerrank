/* 
DAY21:
PROBLEM: write a method that takes array of any type
LINK: https://www.hackerrank.com/challenges/30-generics/problem?isFullScreen=true
*/

import java.util.*;

class Printer <T> {

    /**
    *    Method Name: printArray
    *    Print each element of the generic array on a new line. Do not return anything.
    *    @param A generic array
    **/
    
    // Write your code here
    void printArray(Object[] arr){
        for (Object i : arr){
            System.out.println(i);
        }
    }

}

public class Day21_Generics {
    
    public static void main(String args[]){
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        
        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if(Printer.class.getDeclaredMethods().length > 1){
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    } 
}