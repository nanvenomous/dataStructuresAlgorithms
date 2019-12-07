package java_lib.IsPalindrome;

class IsPalindrome {
	public boolean isEven;
	int numDigits;
	int forward;

	public boolean run(int x) {
		if (x < 0) {return false;}
		forward = x;
		return false;
	}

	public void digits_to_reverse() {
		numDigits = (int)Math.log10(forward);
		isEven = !(0 == numDigits % 2);
		if (isEven) {numDigits += 1;}
		numDigits /= 2;
	}

	public int partial_reverse() {
		int reversed = 0;

		digits_to_reverse();
		while (numDigits > 0) {
			reversed = safe_increment_reversed(reversed);
			forward /= 10;
			numDigits--;
		}
		return reversed;
	}

	public int safe_increment_reversed(int reversed) {
		reversed *= 10;
		reversed += forward % 10;
		return reversed;
	}
}
