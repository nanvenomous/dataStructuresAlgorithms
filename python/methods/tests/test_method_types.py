
import pytest
from ..method_types import DecoratorExample

subject = DecoratorExample()

class TestStaticMethod:
	def test_static_method_cannot_access_attribute(self):
		with pytest.raises(NameError):
			subject.static_method_attempt_attribute_access()

	def test_static_method_cannot_access_other_method(self):
		with pytest.raises(NameError):
			subject.static_method_attempt_other_method_access()

	def test_access_private_static_method(self):
		assert 1 == subject._private_static_method() # private methods can apparently be accessed

	def test_static_method_before_instantiation(self):
		assert 1 == DecoratorExample._private_static_method()

class TestClassMethod:
	def test_class_mentod_access_other_method(self):
		assert 1 == subject.class_method()

	def test_class_method_cannot_access_attribute(self):
		with pytest.raises(AttributeError):
			subject.class_method_attempt_attribute_access()

	def test_class_method_accessable_before_instantiation_if_not_calling_instance_method(self):
		assert 1 == DecoratorExample.class_method()

	def test_class_method_not_accessable_before_instantiation_if_calling_instance_method(self):
		with pytest.raises(TypeError):
			DecoratorExample.class_method_calling_instance_method()

class TestInstanceMethod:
	def test_instance_method_access_other_methods_and_attributes(self):
		assert 2 == subject.instance_method()

	def test_instance_mentod_not_accessable_before_instantiation(self):
		with pytest.raises(TypeError):
			DecoratorExample.instance_method()