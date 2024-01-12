import operator

def are_arithmetic(a: int, b: int, c: int):
    operations = [operator.add, operator.sub, operator.mul, operator.truediv]
    for operation in operations:
        if operation(a, b) == c:
            print(f"These can be used in an arithmetic operation, {a} {str(operation)} {b} = {c}")
            return True
        elif a == operation(b, c):
            print(f"These can be used in an arithemtic operation, {a} = {b} {str(operation)} {c}")
            return True
    print("These cannot be used in an arithmetic operation")
    return False


if __name__ == "__main__":
    user_input = input("Enter three numbers separated by spaces: ")
    a, b, c = list(map(int, user_input.split()))
    are_arithmetic(a, b, c)