package java_lib.RomanToInteger;
import java.util.HashMap;

class RomanToInteger {
	String roman;
	char let;
	int value = 0;
	public HashMap<Character, Integer> conversion;

	public RomanToInteger() {
		conversion = new HashMap();
		conversion.put('I', 1);
		conversion.put('V', 5);
		conversion.put('X', 10);
		conversion.put('L', 50);
		conversion.put('C', 100);
		conversion.put('D', 500);
		conversion.put('M', 1000);
	}

	public int run(String s) {
		roman = s;
		// while (roman.length() > 0) {
		// }
		return 0;
	}

	public void getAndRemoveLastChar() {
		let = roman.charAt(roman.length() - 1);
		roman = roman.substring(0, roman.length() - 1);
	}
}
