def announce(function):
    def wrapper():
        print("about to run the function")
        function()
        print("Done with the function")

    return wrapper


@announce
def hello():
    print("hello")


hello()
