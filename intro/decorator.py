from functools import wraps

def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """ this is decorated function """
        print("I'm above foo")
        f()
        print("I'm below foo")
        print("d name", decorated_function.__name__)
    # decorated_function.__name__ = f.__name__  # using wraps instead of this
    print("d name", decorator.__name__)
    return decorated_function   # if we type decorated_function() then it will get call also automatically

@decorator
def foo():
    """ this is foo """
    print("I'm foo")

foo()
print("function name", foo.__name__)
print("function docstring" + foo.__doc__)
print("function module", foo.__module__)
