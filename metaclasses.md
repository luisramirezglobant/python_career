# Metaclasses
> A **metaclass** defines how a class behaves. 


- A class itself is an instace of a metaclass.
- A class defines how a instance of that class will behave.

## type()
> Python uses a *metaclass* called `type`.  When you define a class using the class keyword, type is the metaclass that's used to create that class.

At high level is a function that help us find the **type** of an object. The first attribute is the *class name*
```python
type(1)
<class 'int'>

type("example")
<class 'str'>

class Foo:
    pass

type(Foo)
<class 'type'>

type(Foo())
<class '__main__.Foo'>
```

Also `type()` has the ability to dinamically create classes.
```python
test_class = type("TestClass", (), {})

test_class # variale that holds the class reference
<class '__main__.TestClass'>

test_class() #object instance
<__main__.TestClass object at 0x1030cdca0>

type(test_class)
<class 'type'>
```

Also the classes created with `type()` may include **inheritance** by passing a class as the second paramenter in a *tuple* (enclosed by parethesis), also the class may include **class attributes** and ussing a dictionary in the third argument.

```python
test_class = type(
    "TestClass",
    (Foo,),
    {
        "test_arg_1": "test value 1",
        "test_arg_2": "test value 2",
    },
)

test_class.test_arg_1, test_class.test_arg_2
test value 1 test value 2

test_class()
<__main__.TestClass object at 0x104a05f70>

type(test_class)
<class 'type'>
```
All objects are of type `type`

## Metaclasses
Everything in Python is an object, these objects are created by **metaclasses**. Whenever we call `class` to create class, there is a metaclass that creates the class behind the scenes. It's similar with `str` that creates a string object or `int`.
The `__class__` attribute enables check the type of the current instance.
```python
test_var = 'metaclasses'

test_var.__class__
str

type(test_var)
str

type(str)
type

test_var.__class__.__class__
type
```

## Custom metaclasses
**Note:** it's not recommended to change the behavior of how a class ins created using custom metaclasses, this is just for learning porposes.

Metaclasses can be defined in two ways.
### __new __
The `__new__()` method is used when we want to define a *dict* or *tuple* before the class is created.
The return value of `__new__` is usualy a instance of `cls`. Allows subclasses of immutable tyoes to customeze instance creation.
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x
```
- Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class
- Assigns the custom attribute attr to the class, with a value of 100
- Returns the newly created class
```python
class Foo(metaclass=Meta):
    pass

Foo.attr
100
```

### __init __
Method called after the object has been created (the class attributes were assigned).
```python
class Meta(type):
    def __init__(
        cls, name, bases, dct
    ):
        cls.attr = 100

class X(metaclass=Meta):
    pass

X.attr
100

class Y(metaclass=Meta):
    pass

Y.attr
100
```

In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template for the creation of classes. Metaclasses are sometimes referred to as class factories.