def add(*args):
    total = 0
    for i in args:
        total += i
    
    print(total)

def print_args(*args):
    for i in args:
        print(i)
    
add(1, 2, 3, 4, 5, 6, 7)
print(10, 7, 6, 9)