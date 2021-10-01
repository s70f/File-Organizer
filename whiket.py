
class BreakLoop(Exception):
    pass


def func(num):
    print("function")
    yes = num
    raise BreakLoop
    print("OMFAOMFA")


try:
    while True:
        print("Hello")
        func(True)
except BreakLoop:
    print("broken")
