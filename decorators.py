import functools
import time

def time_decorator(function):
    @functools.wraps(function)
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"elapsed time {end-start}")
    return wrapper

@time_decorator
def list_comprhension():
    return [x for x in range(100000000)]


def logger_decorator(function):
    @functools.wraps(function)
    def wrapper(x, y):
        print(f"función {function.__name__} con parametros {x} {y}")
        return function()
    return wrapper

@logger_decorator
@time_decorator
def list_map():
    return list(map(lambda x: x, range(10)))


def is_logged_in(function):
    def wrapper(credentials, verb, url, body):
        if credentials != "valid credentials":
            raise ValueError("Invalid credentials")
        print("Valid sesion")
        return function(credentials, verb, url, body)
    return wrapper

@is_logged_in
def make_request(credentials: str, verb: str, url: str, body: dict):
    print(f"{verb} request to {url} with body {body}")

def requires_auth(auth_function):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            credentials = kwargs.get("credentials") if "credentials" in kwargs else (args[0] if args else None)
            if auth_function(credentials):
                return function(*args, **kwargs)
            raise AuthException("Invalid credentials")
        return wrapper
    return decorator

class AuthException(ValueError):
    ...

def is_valid_credentials(credentials: str):
    if credentials == "valid credentials":
        return True
    return False

@requires_auth(is_valid_credentials)
def protected_function(credentials: str, verb: str, url: str, body: dict):
    print(f"{verb} request to {url} with body {body}")

if __name__ == "__main__":
    list_comprhension()
    print(f"result {list_map("a", "b")}")
    make_request(
        "valid credentials", "GET", "www.google.com", {}
    )
    # make_request("invalid", "", "", {})
    protected_function("valid credentials", "POST", "wwww.google.com", {"body": "body"})
    protected_function(
        "invalid credentials", "GET", "www.google.com", {}
    )