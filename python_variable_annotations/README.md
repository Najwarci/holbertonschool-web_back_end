 # 🐍 Python - Variable Annotations

This repository demonstrates how to use **variable annotations** in Python, a feature introduced in Python 3.6 to improve code readability and static type checking.

---

## 📘 Table of Contents

- [Introduction](#introduction)
- [Syntax](#syntax)
- [Examples](#examples)
- [Using with mypy](#using-with-mypy)
- [Limitations](#limitations)
- [References](#references)

---

## 🧠 Introduction

**Variable annotations** allow you to specify the expected type of a variable. This helps tools like `mypy`, `pyright`, or IDEs such as VSCode and PyCharm to provide static type checking.

```python
age: int
name: str = "Alice"
```

Note: These annotations are **ignored at runtime** unless additional tools are used.

---

## ✍️ Syntax

```python
variable_name: type_hint
variable_name: type_hint = value
```

Examples:

- `x: int` → `x` is expected to be an integer.
- `y: List[str] = []` → `y` is a list of strings.

---

## 📌 Examples

### Basic Variables

```python
title: str = "Python Guide"
count: int
price: float = 19.99
is_active: bool = True
```

### Complex Types

```python
from typing import List, Dict, Optional, Union

names: List[str] = ["Alice", "Bob"]
config: Dict[str, int] = {"retry": 3, "timeout": 10}
maybe_number: Optional[int] = None
value: Union[int, float] = 3.14
```

---

## ✅ Using with `mypy`

Install `mypy`:

```bash
pip install mypy
```

Run it on your script:

```bash
mypy your_script.py
```

Example of a detected issue:

```python
x: int = "hello"  # Error: Incompatible types (expected "int", got "str")
```

---

## ⚠️ Limitations

- Variable annotations are **not enforced at runtime** by default.
- They are **only hints** unless used with a static type checker or runtime validator (e.g., `pydantic`, `enforce`).

---

## 📚 References

- [PEP 526 – Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
- [Typing — Python Documentation](https://docs.python.org/3/library/typing.html)
- [mypy — Optional Static Typing for Python](http://mypy-lang.org/)
