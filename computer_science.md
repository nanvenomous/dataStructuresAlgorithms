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

| Term | definition |
|---|---|
| encapsulation | keeping all data and methods that act on that data in the same class |
|   |   |

* one class having an instance of another class as a member/attribute
	* delegation/forwarding: attribute class is unassociated but does something the container class needs
	* composition: attribute class is associated by being a specific chunck of the container class
	* aggregation: composition but component objects are not garbage collected when container class is deleted



# Improving already written code
* what happens with negatives
* what happens when you get a lot of data?
* will any lists be accessed out of range?
