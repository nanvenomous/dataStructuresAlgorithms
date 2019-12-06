package java_lib.ReverseInteger;

class ReverseInteger {
	public int run(int forward) {
		if ( forward < (-1*Math.pow(2, 31)) || forward > (Math.pow(2, 31) + 1) ) {
			return 0;
		}

		int reversed = 0;

		while (forward != 0) {
			reversed *= 10;
			reversed += forward % 10;
			forward /= 10;
		}
		return reversed;
	}
}
