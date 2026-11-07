<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="typy-on-dark.svg">
    <img src="typy-on-light.svg" alt="TyPy" width="360">
  </picture>
</p>

<p align="center">
  A typed subset of standard Python, compiled ahead of time to small native
  executables through LLVM.
</p>

TyPy is an independent implementation of Python. Its source is ordinary
Python: every program TyPy accepts also runs under CPython 3.12 to 3.15,
with the same output and exit status. TyPy refuses a program it cannot
compile with CPython's meaning, and the diagnostic names the rule. The
output is one native executable, with no interpreter and no garbage
collector pauses; a hello world linked statically with musl is 75 KB.

```python
def area(width: int, height: int) -> int:
    return width * height


print(area(3, 4))
```

```sh
typy run area.py     # prints 12
typy build area.py   # writes the executable ./area
```

- [typy](https://github.com/typy-lang/typy): the compiler, its runtime and
  the documents. Start with its README.
- [Releases](https://github.com/typy-lang/typy/releases): archives for
  x86_64 Linux.
- [Security](https://github.com/typy-lang/typy/security/policy): how to
  report a vulnerability privately.

TyPy is licensed under either of the Apache License, Version 2.0 or the MIT
license, at your option.
