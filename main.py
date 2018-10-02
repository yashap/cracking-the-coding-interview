from ch03.queue import Queue


def main():
    queue = Queue[int](10, 11, 12)
    queue.add(9)
    for item in queue:
        print(item)
    print(queue.remove())


if __name__ == "__main__":
    main()
