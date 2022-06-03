## Proof of Concept implementation for new Warning formatting

See, [this discuss thread](https://discuss.python.org/t/default-warning-formatting-improvements/16006) for context. Based on [CPython `warnings.py@d8f40ead`](https://github.com/python/cpython/blob/d8f40ead92b5a973cff3a30482a7659d3b46b1ba/Lib/warnings.py).

Keep in mind, that the current implementation:

- Assumes Python 3.11 or newer.
  (Uses the new `co_positions()` method)

- Is written in pure Python.
  (The C `_warning` extension loading is disabled)

- Is **not** well tested.
  (I haven't checked any `warnings` APIs apart from `warnings.warn`)

- Is currently not backwards compatible.
  (I've added some new fields and parameters, which probably breaks monkey-patching)

You can see an example comparison between old and new warnings by running `./compare_warnings.sh` or `./compare_warnings_in_docker.sh` if you don't have Python 3.11 installed locally.

### Examples

#### Old Warnings

```python
/long/path/to/code/that/may/end/up/wrapping/example.py:27: UserWarning: This is a regular warning.
  warnings.warn("This is a regular warning.")
```
```python
/long/path/to/code/that/may/end/up/wrapping/example.py:28: DeprecationWarning: old_baz is deprecated in version X, use new_baz instead.
  bar(old_baz() + 1)
```
```python
/long/path/to/code/that/may/end/up/wrapping/example.py:19: VeryImportantWarning: This is a very important warning, you need to fix it!
  warnings.warn(
```

#### New Warnings

```python
File "/long/path/to/code/that/may/end/up/wrapping/example.py", line 27, in foo
  UserWarning: This is a regular warning.
```
```python
File "/long/path/to/code/that/may/end/up/wrapping/example.py", line 28, in foo
  bar(old_baz() + 1)
      ^^^^^^^^^
  DeprecationWarning: old_baz is deprecated in version X, use new_baz instead.
```
```python
File "/long/path/to/code/that/may/end/up/wrapping/example.py", line 19, in bar
  VeryImportantWarning: This is a very important warning, you need to fix it!
```
