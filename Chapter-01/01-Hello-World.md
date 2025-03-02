# Chapter 1 – Modules, Comments & Pip

Let's write our first Python program. Create a file called `hello.py` and paste the code below in it:

```python
print("hello world")
```

Execute this file by typing `python hello.py` and you will see "hello world" printed on the screen.

## Modules

A module is a file containing code written by someone else (usually) which can be imported and used in our programs.

## Pip

Pip is the package manager for Python. You can use pip to install a module on your system.

```sh
pip install flask  # Installs Flask module
```

## Types of Modules

There are two types of modules in Python:
1. Built-in Modules (Preinstalled in Python)
2. External Modules (Need to be installed using pip)

Some examples of built-in modules are `os`, `random`, etc.
Some examples of external modules are `tensorflow`, `flask`, `pyttsx3`, etc.

## Using Python as a Calculator

We can use Python as a calculator by typing `python` and pressing Enter in the terminal. This opens **REPL** (Read-Evaluate-Print Loop).

## Comments

Comments are used to write something that the programmer does not want to execute. This can be used to mark the author name, date, etc.

### Types of Comments

There are two types of comments in Python:
1. Single-Line Comments: To write a single-line comment, add a `#` at the start of the line.
    ```python
    # This is a single-line comment
    ```
2. Multi-Line Comments: To write multi-line comments, you can use `#` at each line or use a multi-line string (`''' '''`).
    ```python
    '''This is an example
    of a multi-line
    comment!''''
    ```