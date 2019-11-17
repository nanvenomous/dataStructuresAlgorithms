
import java.util.Arrays;

public class HashFun {
  String[] theArray;
  int arraySize;
  int itemsInArray = 0;

  public static void main(String[] args) {
    // run_hash_fun_one();
    run_hash_fun_two();

  }

  private static void run_hash_fun_one() {
    HashFun h_fun = new HashFun(30);
    String[] elementsToAdd = {"1", "5", "17", "21", "26"};
    h_fun.hash_fun_one(elementsToAdd, h_fun.theArray);
    System.out.println(Arrays.toString(h_fun.theArray));
  }

  private void hash_fun_one(String[] stringsForArray, String[] theArray) {
    for (int n = 0; n < stringsForArray.length; n++) {
      String newElementVal = stringsForArray[n];
      theArray[Integer.parseInt(newElementVal)] = newElementVal;
    }
  }

  private static void run_hash_fun_two() {
    HashFun h_fun = new HashFun(30);
    String[] elementsToAdd = { "100", "510", "170", "214", "268", "398",
              "235", "802", "900", "723", "699", "1", "16", "999", "890",
              "725", "998", "978", "988", "990", "989", "984", "320", "321",
              "400", "415", "450", "50", "660", "624" };

    h_fun.hash_fun_two(elementsToAdd, h_fun.theArray);
    System.out.println(Arrays.toString(h_fun.theArray));
  }

  private void hash_fun_two(String[] stringsForArray, String[] theArray) {
    // Iterate over the elements to add to the storage array
    for (int n = 0; n < stringsForArray.length; n++) {
      // Extract the element to add
      String newElementVal = stringsForArray[n];
      // Estimate an index for the value
      int arrayIndex = Integer.parseInt(newElementVal) % 29;
      System.out.println("Modulus Index: " + arrayIndex + " for value " + newElementVal);
      while (theArray[arrayIndex] != "-1") {
        ++arrayIndex;
        System.out.println("Collision! Try " + arrayIndex + " instead.");
        arrayIndex %= arraySize;
      }
      theArray[arrayIndex] = newElementVal;
    }
  }

  HashFun(int size) {
    arraySize = size;
    theArray = new String[size];
    Arrays.fill(theArray, "-1");
  }

}