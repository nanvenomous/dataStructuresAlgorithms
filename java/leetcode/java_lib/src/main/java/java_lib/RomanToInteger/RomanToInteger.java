package java_lib.RomanToInteger;
import java.util.Arrays;

class RomanToInteger {
	static final int[] convert = new int[26];

	static {
		convert['I' - 'A'] = 1;
		convert['V' - 'A'] = 5;
		convert['X' - 'A'] = 10;
		convert['L' - 'A'] = 50;
		convert['C' - 'A'] = 100;
		convert['D' - 'A'] = 500;
		convert['M' - 'A'] = 1000;
	}

	public int run(String s) {
		char[] roman = s.toCharArray();
		char let;
		int num;
		int prevNum = 0;
		int value = 0;
		for (int i=roman.length - 1; i >= 0; i--) {
			let = roman[i];
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
}
