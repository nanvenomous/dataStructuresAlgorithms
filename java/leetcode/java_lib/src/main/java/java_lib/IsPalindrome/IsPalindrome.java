package java_lib.IsPalindrome;

class IsPalindrome {
	public boolean isEven;
	int numDigits;

	public boolean run(int x) {
		if (x < 0) {return false;}
		return false;
	}

	public void digits_to_reverse(int pal) {
		numDigits = (int)Math.log10(pal);
		isEven = !(0 == numDigits % 2);
		if (isEven) {numDigits += 1;}
		numDigits /= 2;
	}

	public int partial_reverse(int forward) {
		int reversed = 0;

		while (forward != 0) {
			reversed = safe_increment_reversed(reversed, forward);
			forward /= 10;
		}
		return reversed;
	}

	public int safe_increment_reversed(int reversed, int forward) {
		reversed *= 10;
		reversed += forward % 10;
		return reversed;
	}
}
