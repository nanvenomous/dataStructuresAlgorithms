package java_lib.TreeTraversal;

public class BinaryTree {
	TreeNode root;

	public void add(int value) {
		root = add_recursive(root, value);
	}

	private TreeNode add_recursive(TreeNode cur, int value) {
		if (cur == null) {return new TreeNode(value);}

		if (value < cur.val) {
			cur.left = add_recursive(cur.left, value);
		} else if (value > cur.val) {
			cur.right = add_recursive(cur.right, value);
		}

		return cur;
	}
}
