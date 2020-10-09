# Object Oriented Programming
| Method | definition |
|---|---|
| virtual | declared in a base class and overwritten in a derived class |
| static | encapsulated in a class but not strictly needing anything from the class, does not require instantiation |
| constructor | creates and returns the object |
| initializer | populates the state of the object and returns the object |
| class | associated with the class, does not require instantiation, call other class method |
| instance | takes in object, can use anything associated with the object |
| destructor | removes the object from memory unless in cyclic dependence |
| signature | the first line of a method declares inputs, method type, input and output types |
| visibility | public, private, other |

| Term | definition |
|---|---|
| encapsulation | keeping all data and methods that act on that data in the same class |
| polymorphism | the ability of a class of function to have many forms (i.e. optional inputs, abatract methods) |

* one class having an instance of another class as a member/attribute
	* delegation/forwarding: attribute class is unassociated but does something the container class needs
	* composition: attribute class is associated by being a specific chunck of the container class
	* aggregation: composition but component objects are not garbage collected when container class is deleted

### Overriding vs Overloading
* overloading: when one class has same method name with differing number of input arguments
* overriding: implementing a function that was either defined or declared in an abstract class

### Abstract Class vs Interface

| Difference | Abstract Class | Interface |
|---|---|---|
| methods | abstract and normal methods | only abstract methods |
| variables | can also have non-static & non-final variables | only static and final |
| implementation | can implement interface | cannot implement abstract class |
| inheritance | can be extended (inheritance) | can be implemented by a class or another interface (not inheritance) |
| multiple implementation | can extend a java class & implement multiple interfaces | can only extend another interface |
| accessibility of members | can also have private, protected, ... | public by default |



# Improving already written code
* what happens with negatives
* what happens when you get a lot of data?
* will any lists be accessed out of range?
