var1 = "Python"

def add(x, y):
    print(f"Addition of {x} and {y} is {x + y}")
    return f'we are in return statement of add: {x + y}'    


def multiply(x, y):
    print(f"Multiplication of {x} and {y} is {x * y}")
    return x * y    


print("Value stored in variable __name__ is:", __name__)

if __name__ == "__main__":
    add(5, 3)
   
    multiply(5, 3)
    print("I am learning Python!")

    print("hello world")