from ch03.stack import Stack


def main():
    stack = Stack[int](10, 11, 12)
    stack.push(9)
    for item in stack:
        print(item)


if __name__ == "__main__":
    main()
