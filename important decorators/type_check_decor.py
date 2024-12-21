def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected type {expected_type} but got {type(arg)}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


print(add(1, 'b'))
