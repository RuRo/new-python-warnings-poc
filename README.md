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
