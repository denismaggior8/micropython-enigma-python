# assertion.py
def assert_eq(a, b, msg=""):
    """Check equality, print result."""
    if a != b:
        print("FAIL: ", a, "!=", b, " ", msg)
        return False
    else:
        print("PASS")
        return True

def assert_true(expr, msg=""):
    """Check if expression is True."""
    if not expr:
        print("FAIL:", expr, "is not True", " ", msg)
        return False
    else:
        print("PASS")
        return True

def assert_false(expr, msg=""):
    """Check if expression is False."""
    if expr:
        print("FAIL:", expr, "is not False", " ", msg)
        return False
    else:
        print("PASS")
        return True