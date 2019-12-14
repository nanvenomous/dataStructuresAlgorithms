package java_lib.RomanToInteger;
import java.util.Arrays;

class RomanToInteger {
	String roman;
	char let;
	int num;
	int prevNum = 0;
	int value = 0;
	int[] convert = new int[26];

	void convert_init() {
		convert['I' - 'A'] = 1;
		convert['V' - 'A'] = 5;
		convert['X' - 'A'] = 10;
		convert['L' - 'A'] = 50;
		convert['C' - 'A'] = 100;
		convert['D' - 'A'] = 500;
		convert['M' - 'A'] = 1000;
	}

	public int run(String s) {
		convert_init();
		roman = s;
		while (roman.length() > 0) {
			getAndRemoveLastChar();
			num = convert[let - 'A'];
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
