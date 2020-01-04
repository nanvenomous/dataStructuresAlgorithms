from binarytree import tree, bst

t = bst(height=3)
# t = bst(height=2)
# t = bst(height=2, is_perfect=True)

print(t)

print('inorder: ascending numerical order')
print(t.inorder)

print()

print('preorder: prints root first')
print(t.preorder)

print()

print('postorder: prints root last')
print(t.postorder)

print()
