package java_lib.IsPalindrome;

class IsPalindrome {
	public boolean isEven;
	int numDigits;
	int forward;
	int reversed = 0;

	public boolean run(int x) {
		if (x < 0) {return false;}
		forward = x;
		partial_reverse();
		return (reversed == forward);
	}

	public void digits_to_reverse() {
		numDigits = (int)Math.log10(forward);
		isEven = !(0 == numDigits % 2);
		if (isEven) {numDigits += 1;}
		numDigits /= 2;
	}

	public void partial_reverse() {
		digits_to_reverse();
		while (numDigits > 0) {
			safe_increment_reversed();
			forward /= 10;
			numDigits--;
		}
		if (!isEven) {forward /= 10;}
	}

	public void safe_increment_reversed() {
		reversed *= 10;
		reversed += forward % 10;
	}
}
