public class BinaryTree {
	Node root;

	public void add(int value) {
		add_recursive(root, value);
	}

	private Node add_recursive(Node cur, int value) {
		if (cur == null) {return new Node(value);}

		if (value < cur.value) {
			cur.left = add_recursive(cur.left, value);
		} else if (value > cur.value) {
			cur.right = add_recursive(cur.right, value);
		}

		return cur;
	}
}

