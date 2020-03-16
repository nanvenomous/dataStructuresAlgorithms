
import java.util.Arrays;

public class HashFun {
  String[] theArray;
  int arraySize;
  int itemsInArray = 0;
  boolean verboseHash = false;
  boolean verboseFind = true;

  public static void main(String[] args) {
    HashFun h_fun = new HashFun(30);
    String[] elementsToAdd = { "100", "510", "170", "214", "268", "398",
              "235", "802", "900", "723", "699", "1", "16", "999", "890",
              "725", "998", "978", "988", "990", "989", "984", "320", "321",
              "400", "415", "450", "50", "660", "624" };

    h_fun.hash_fun(elementsToAdd, h_fun.theArray);
    h_fun.findKey("660");
    System.out.println(Arrays.toString(h_fun.theArray));
  }

  HashFun(int size) {
    arraySize = size;
    theArray = new String[size];
    Arrays.fill(theArray, "-1");
  }

  public String findKey(String key) {
    int arrayIndexHash = Integer.parseInt(key) % 29;
    // go until you hit an empty spot that would have been filled
    while (theArray[arrayIndexHash] != "-1") {
      if (theArray[arrayIndexHash] == key) {
        print_find(key + " was found in index " + arrayIndexHash);
        return theArray[arrayIndexHash];
      }
      ++arrayIndexHash;
      arrayIndexHash %= arraySize;
    }
    return null;
  }

  private void hash_fun(String[] stringsForArray, String[] theArray) {
    // Iterate over the elements to add to the storage array
    for (int n = 0; n < stringsForArray.length; n++) {
      // Extract the element to add
      String newElementVal = stringsForArray[n];
      // Estimate an index for the value
      int arrayIndex = Integer.parseInt(newElementVal) % 29;
      print_hash("Modulus Index: " + arrayIndex + " for value " + newElementVal);
      while (theArray[arrayIndex] != "-1") {
        ++arrayIndex;
        print_hash("Collision! Try " + arrayIndex + " instead.");
        arrayIndex %= arraySize;
      }
      theArray[arrayIndex] = newElementVal;
    }
  }

  private void print_hash(String message) {
    if (verboseHash) {
      System.out.println(message);
    }
  }

  private void print_find(String message) {
    if (verboseFind) {
      System.out.println(message);
    }
  }
}