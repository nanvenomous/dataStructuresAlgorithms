package java_lib.ReverseInteger;

class ReverseInteger {
	double p_overflow = Math.pow(2, 31) - 1;
	double n_overflow = Math.pow(-2, 31);
	int remainder;

	public int run(int x) {
		int reversed = 0;

		while (x != 0) {
			reversed = safe_increment_reversed(reversed, x);
			x /= 10;
		}
		return reversed;
	}

	public int safe_increment_reversed(int reversed, int x) {
		remainder = x % 10;
		if ((n_overflow - remainder)/10 > reversed || reversed > (p_overflow - remainder)/10) {
			return 0;
		}
		reversed *= 10;
		reversed += remainder;
		return reversed;
	}
}
