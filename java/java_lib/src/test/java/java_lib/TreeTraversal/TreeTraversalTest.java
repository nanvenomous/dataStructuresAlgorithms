package java_lib.TreeTraversal;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

public class TreeTraversalTest {
	private TreeTraversal subject;

	@BeforeEach
	public void setup() {
		subject = new TreeTraversal();
	}

	private BinaryTree instantiate_tree(Integer[] array) {
		BinaryTree tree = new BinaryTree();
		for (Integer a : array) {
			tree.add(a);
		}
		return tree;
	}

	private void assert_traverses_tree_preorder(Integer[] ints) {
		BinaryTree tree = instantiate_tree(ints);
		List<Integer> traversal = subject.preorderTraversal(tree.root);
		List<Integer> answer = new ArrayList<Integer> (traversal);
		Collections.sort(answer);
		assertEquals(traversal, answer);
	}

	@Test
	public void should_preorder_traverse_balanced_tree() {
		Integer[] ints = {7, 0, 1, 10, 11};
		assert_traverses_tree_preorder(ints);
	}

	@Test
	public void should_preorder_traverse_right_shifted_tree_with_negative() {
		Integer[] ints = {-1, 2, 6, 12, 17};
		assert_traverses_tree_preorder(ints);
	}

	@Test
	public void should_preorder_traverse_left_shifted_tree() {
		Integer[] ints = {22, 12, 6, 5, 3};
		assert_traverses_tree_preorder(ints);
	}
}
