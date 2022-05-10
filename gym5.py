def rectangle_area (a,b):
    return a*b
print(rectangle_area(17,23))

print((lambda a,b:a*b)(17,23))

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(15,2))

print((lambda a,b:a if a>b else b)(15,2))