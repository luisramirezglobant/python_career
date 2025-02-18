# Decorators
> Decorators provide a way to wrap functions with extra functionality without directly changing the original function's code.

## Fundamentals
- Python has the ability to treat **functions** as ==first-class== objects (i.e., you can pass them as arguments to other functions, return them from functions, and assign them to variables).
- A **closure** is a function that retains access to variables or arguments from his definition context, this is translated to a function defined inside another and therefore the inner functions has access to all the argumets *(function parameters)* and variables that are available in a previous scope

## What are Decorators?
Think of **decorators** as wrappers. They take a function as input, add some functionality to it, and then return the modified function (or a new function that does the same thing).  

In a more technical approach, a **decorator** is a function that receives a function as parameter, and this function encloses a **closure**. The inner function known as `wrapper` mantains access to the *decorated* function passed as argument and all of elements created in the outer scope. Inside this `closure` is where the *decorated* function modifications are made, and has to return a result similar to what is expected by incoming function.
This can be achieved by:
1. Returning the argument function execution.
2. Executing the decorated function, modify the result and the return the same type of response.
3. Return the result or execution of a similar function as the decorated one.

A key aspect of the decorator function is that have to **return** the `wrapper` function

```python
def decorator(function):
    def wrapper():
        # Function execution and modification
        return function()
    return wrapper
```

### Syntax and Basic Usage

The `@` symbol is used to apply a decorator to a function.  Here's the basic syntax:

```python
@my_decorator
def my_function():
    # function code
    pass

print(f"Result of the function decorated {my_function}")
```

## Decorating functions with expected parameters
If the function to be decorated expects some *parameters*, these can be defined in the **closure**.
There are two to proceed in this scenario.

### Custom decorator by function arguments
Build a custom decorator where the wrapper requiers all of the function parameters. This parameters needs be matched by number and position or by keyword depending their definition.

```python
def decorator(function):
    def wrapper(func_arg_1, func_arg_2):
        return function(func_arg_1, func_arg_2)
    return wrapper

@decorator
def decorated_function(arg_1, arg_2):
    # function code
    pass

print(f"Execution of the decorated function {decorated_function(var_1, var_2)}")
```

### General porpuose decorator
Instead of matching the parameters of the certain function, use `*args` and `**kwargs` to handle differebt situations for multiple function scenarios.

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        param = = kwargs.get("arg_name") if "arg_name" in kwargs else (args[0] if args else None)
        return function(param, args[1])
    return wrapper

@decorator
def decorated_function(arg_1, arg_2):
    # function code
    pass

print(f"Execution of the decorated function {decorated_function(var_1, var_2)}")
```

## Decorators with parameters
If there is a use case where we need to recive parameters in our decorator, we can wrap our decorator with another function to handle this scenario.
- The *most outter function* **(decorator maker)** manages the paramets with the requirements of number, position o keyword. This function has to return the *decorator function*.
- The **decorator** function as usual recives the *decorated* function as parameter, returns the wrapper function.
- The **closure** (*wrapper*) has access to the all functions and parameters defined in an outter scope. Execute and returns a value of the expected type as the decorated function.

```python
def decorator_maker(decorator_arg)
    def decorator(function):
        def wrapper(*args, **kwargs):
            param = = kwargs.get("arg_name") if "arg_name" in kwargs else (args[0] if args else None)
            # the decorator arguments can be functions or values
            result = decorator_arg(param)
            return function(result, func_arg_2)
        return wrapper
    return decorator

@decorator_maker(lambda param: print(f"parameter passed {param}"))
def decorated_function(arg_1, arg_2):
    # function code
    pass

print(f"Execution of the decorated function {decorated_function(var_1, var_2)}")
```