def message (x):
    def print_message(y):
        return x, y
    return print_message
d = message(6)
print(d(7))

