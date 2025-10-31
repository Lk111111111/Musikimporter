def artist_decorator(function):
    def wrapper(*args, **kwargs):
        function(*args)
        print("artist file created")
    return wrapper