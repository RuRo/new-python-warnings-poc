import sys
import traceback
import warnings

class VeryImportantWarning(UserWarning):
    pass


def old_baz():
    warnings.warn(
        "old_baz is deprecated in version X, use new_baz instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return 0


def bar(*_):
    warnings.warn(
        "This is a very important warning, "
        "you need to fix it!",
        VeryImportantWarning,
    )


def foo():
    warnings.warn("This is a regular warning.")
    bar(old_baz() + 1)


if __name__ == "__main__":
    foo()
