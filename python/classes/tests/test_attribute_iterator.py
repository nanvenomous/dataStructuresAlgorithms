from ..attribute_iterator import Example

e = Example()
e.iterate()

def test_did_iteration_with_attribute_elem():
    assert 3 == e.elem
