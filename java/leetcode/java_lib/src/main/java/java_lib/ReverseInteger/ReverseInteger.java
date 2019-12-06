package java_lib.ReverseInteger;

class ReverseInteger {
	public int run(int forward) {
		int reversed = 0;

		while (forward != 0) {
			reversed *= 10;
			reversed += forward % 10;
			forward = forward / 10;
		}
		return reversed;
	}
}
