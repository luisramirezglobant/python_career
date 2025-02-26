class MyMeta(type):  # Inheriting from type
    def __new__(
        cls, name, bases, attrs
    ):  # Overriding __new__
        print("MyMeta.__new__ called")
        new_attrs = {}
        for (
            attr_name,
            attr_value,
        ) in attrs.items():  # modify attributes
            if attr_name.startswith("__"):
                new_attrs[attr_name] = attr_value
            else:
                new_attrs[attr_name] = (
                    attr_value * 2
                )  # multiply the attribute value by 2
        return super().__new__(
            cls, name, bases, new_attrs
        )  # Call type.__new__

    def __init__(
        cls, name, bases, attrs
    ):  # Overriding __init__
        print("MyMeta.__init__ called")
        super().__init__(name, bases, attrs)


class MyClass(
    metaclass=MyMeta
):  # Using the metaclass
    x = 10
    y = "hello"


obj = MyClass()
print(obj.x)  # Output: 20
print(obj.y)  # Output: hellohello
