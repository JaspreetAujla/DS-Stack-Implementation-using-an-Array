def stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed: " + item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = stack()
push(stack, str(23))
push(stack, str(34))
push(stack, str(42))
push(stack, str(54))
print("\nPOPPED: " + pop(stack))
print("\nAfter popping an element:\n " + str(stack))
