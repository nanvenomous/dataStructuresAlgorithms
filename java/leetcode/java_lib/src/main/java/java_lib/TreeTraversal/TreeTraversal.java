package java_lib.TreeTraversal;

import java.util.List;
import java.util.ArrayList;

class TreeTraversal {
	List<Integer> lst = new ArrayList<Integer>();

	private void addWithNullCheck(TreeNode node) {
		if (node != null) {
			addNodeToList(node);
		}
	}

	private void addNodeToList(TreeNode node) {
		addWithNullCheck(node.left);
		lst.add(node.val);
		addWithNullCheck(node.right);
	}

	public List<Integer> preorderTraversal(TreeNode root) {
		addNodeToList(root);
		return lst;
	}
}
