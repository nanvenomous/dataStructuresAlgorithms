package java_lib.RomanToInteger;
import java.util.HashMap;

class RomanToInteger_HashMap {
	String roman;
	char let;
	int num;
	int prevNum = 0;
	int value = 0;
	public HashMap<Character, Integer> conversion = new HashMap<Character, Integer>();

	public RomanToInteger_HashMap() {
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
		while (roman.length() > 0) {
			getAndRemoveLastChar();
			num = conversion.get(let);
			if (num < prevNum) {
				value += prevNum - num;
				prevNum = 0;
			} else {
				value += prevNum;
				prevNum = num;
			}
		}
		value += prevNum;
		return value;
	}

	public void getAndRemoveLastChar() {
		let = roman.charAt(roman.length() - 1);
		roman = roman.substring(0, roman.length() - 1);
	}
}
