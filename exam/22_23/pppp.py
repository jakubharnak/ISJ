try:
    for i in range(3):
        try:
            1/0
            print("Divided by zero")
        except ZeroDivisionError:
            print("Inner ZeroDivisionError")
            raise KeyError("Zero")
        except KeyError:
            print("Inner KeyError")
        finally:
            print("Finally block")
            break
except ZeroDivisionError:
    print("Outer ZeroDivisionError")
    
# Inner ZeroDivisionError
# Finally block