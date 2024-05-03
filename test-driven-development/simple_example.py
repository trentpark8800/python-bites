def divide_by_two(x):
    return x/2

def test_divide_by_two():
    assert divide_by_two(4) == 2
    assert divide_by_two(10) == 5
    assert divide_by_two(100) == 50

def main():
    test_divide_by_two()
    print("All tests passed!")

if __name__ == "__main__":
    main()
