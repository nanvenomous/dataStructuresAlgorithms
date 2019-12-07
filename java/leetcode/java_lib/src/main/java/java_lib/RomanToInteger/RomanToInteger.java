package java_lib.RomanToInteger;

class RomanToInteger {
	String roman;
	char let;

	public int run(String s) {
		roman = s;
		return 0;
	}

	public void getAndRemoveLastChar() {
		let = roman.charAt(roman.length() - 1);
		roman = roman.substring(0, roman.length() - 1);
	}
}
