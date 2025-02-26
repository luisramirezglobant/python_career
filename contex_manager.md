# Context Manager
> A context manager in Python provide a structured approach to resource management. They ensure that resources are acquired, used properly, and finally released or cleaned up, even with errors or exceptions.

## Memory Leak
External resources (to our current program execution) like files, locks (mutex) and network connections are incorrectly managed their memomry allocations in a way that the memory wich is no longer needed is not **released**.
Another possible scenario for memory leak is when an object is istored in memory but it cannot be accessed by the running code (unreachable memory).

### Example of memory leak
Working with a database requires stablish a connection, when a stablished connection is not longer needed is a common practice to releas or reuse it. If the connections are not closed, there is a possibility that the backend stops accepting new connections. An admin has to kill those connection manually causing a problem with the interacion with the app.

Writing to text files is a buffered operation. This means that when we call the `.write()` function (or similar) it won't inmeaditly result in writing the text to physical file but to temporary **buffer** (the buffer is a temporary memory where the text is stored, so it can be easily accessed and manged since the I/O operation are expensive). If we forget to call `.write()` function (or similar), the part of the buffer that hasn't be saved in the file will be lost (chances made to the buffer).

## Resource management
Python has to approaches to deal with this porpose. Let's continue with the example of the file.

```python
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()
```

This implementation does not guarantee that the file content will be saved, an exeption may occur while executing `.write()`, an therefore the program might leak a file descriptor (file descriptor is a unique integer that the SO assigns when a file is opened. Acts a reference, allowing programs to perform I/O operations over that file). The content of the buffer will leaked and unabled to be accessed.


To tackle this problem two approches may be used.
1. `try ... finally` construct
2. `with`construct

The first approach provides a setup and teardown mechanism to manage any kind of resource. However it's a little bit verbose, and there is a posibility that certain clean up actions were forgotted in the `finally` clause.

The second approach provides a reuse setup and teardown code with the limitation of the with statement.

### `with` statement
Creates a **runtime context** (block of code enclosed by the statement, has to follow tab consistency) that allows to run a group of statements under the control of a **context manager**. This statement let us standarize the way to handle `try ... finally` cases.

General syntaxis
```python
with expression as target_var:
    do_something(target_var)
```

Order of steps followed when calling the with statement:
1. Call `expression`to obtain the context manager.
2. Store context managers `.__enter__()` and `.__exit__()` methods for later use.
3. Call `.__enter__()` on the context and bind its return value to `target_var` **if provided**.
4. Execute the `with` code block (runtime context).
5. Call `.__exit__()` on the context manager when the execution of the `with` code block finishes.

### Context management protocol
This protocol consists in two special methods:
1. `.__enter__()` is called by the with statement to enter the runtime context.
2. `.__exit__()` is called when the execution leaves the `with` code block.

The `as` *specifier* is optional, if it's used and a target_var specified the **returned** value of calling `.__enter__()` is bound to the that variable.

In the `.__exit__()` definition, the teardown or clean up logic is set.
For instance, calling `.close()` on an open file.

Let's analize the next code
```python
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")
```
- Running the with statement, `open()`returns an `io.TextIOBase` object. Therefore calling `.__enter__()` (since `open()` is a **context manager**) assigns its return value to `file` (the `io.TextIOBase` object).
- The file is manipulated inside the `with` code block.
- When the block ends, `.__exit__()` automatically gets called and executes `.close()` over the file even if an exeption is rised inside the `with` block.

In Python 3.1 and later, the with statement supports *multiple context managers*. A with statement can be supplied with any number of context managers separated by comma.
```python
with A() as a, B() as b:
    pass
```
Acts as nested with statements without being nested.
Example of usage.
```python
with open("input.txt") as in_file, open("output.txt", "w") as out_file:
    # Read content from input.txt
    # Transform the content
    # Write the transformed content to output.txt
    pass
```
