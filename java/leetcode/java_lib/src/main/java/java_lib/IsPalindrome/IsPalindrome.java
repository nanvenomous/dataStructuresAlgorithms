package java_lib.IsPalindrome;

class IsPalindrome {
	double p_overflow = Math.pow(2, 31) - 1;
	double n_overflow = Math.pow(-2, 31);
	int remainder;

	public boolean run(int x) {
		return true;
	}

	public int digits_to_reverse(int pal) {
		return (int)Math.log10(pal);
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
		remainder = forward % 10;
		if ((n_overflow - remainder)/10 > reversed || reversed > (p_overflow - remainder)/10) {
			return 0;
		}
		reversed *= 10;
		reversed += remainder;
		return reversed;
	}
}
