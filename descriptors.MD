# Descriptors
> Descriptors are a way to customize attribute access (getting, setting, deleting) in Python classes. They provide a mechanism to intercept these operations and execute custom code.

## High level definition
Any class that implements at least one of the methods in the *descriptor protocol*, then your class has a special behavior when is accessed (or an attribute is set) depending on the methods implemented.

## Descriptor protocol
The descriptor protocol is compose by 4 methods.
```python
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
__set_name__(self, owner, name)
```
Depending on the implemented methods, the **descriptor** may have different behaviors an their type may vary.

There are two types of descriptors.
1. **non-data descriptor:** It's a **descriptor** that just implements `.__get__()` method.
2. **data descriptor:** It's When the **class** implements `.__set__()` or `.__delete__()`.

This difference it's not only about the name, they **interact different** in the class *lookup process*.

Once your descriptor class has been created, you are able to use it in other class where you want modify their attributes behavior. This is achieved by assigning a class attribute to another class, this attributes of the *base class* that are an instance of the descriptor class gain the ability to control how their values are accessed or interacted.

```python
class MyDescriptor:  # The descriptor class
    def __get__(self, instance, owner):
        # ... (implementation)

class MyClass:
    my_attr = MyDescriptor()  # Descriptor instance as a class attribute

obj = MyClass()  # obj is an instance of MyClass

obj.my_attr  # Accessing the attribute triggers the descriptor's __get__
```
For **class instance attributes**, the attribute is existing previous to the class initialization. 

The main difference between the **composition** and the **descriptor class instance** is that composition is desing principle to create complex objects based on relationships with *simplier* classes
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

my_car = Car()
my_car.engine.start()  # Accessing the composed object's method
```
In **composition** the instance is made in the `__init__()` or where the object is initiated. 

