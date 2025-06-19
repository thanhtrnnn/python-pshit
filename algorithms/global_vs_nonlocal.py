# Global variable example
count = 0

def increment_global():
    global count  # refers to the module-level count
    count += 1

def test_global():
    print("Global count before:", count)
    increment_global()
    print("Global count after:", count)

# Nonlocal variable example
def outer():
    num = 10

    def inner():
        nonlocal num  # refers to the num defined in outer()
        num += 5
        print("Num inside inner:", num)

    print("Num before inner call in outer:", num)
    inner()
    print("Num after inner call in outer:", num)

if __name__ == "__main__":
    print("Testing global:")
    test_global()

    print("\nTesting nonlocal:")
    outer()