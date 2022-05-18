def repeat_call(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(0, n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_call(4)
def func1():
    print("Vizov funksii")