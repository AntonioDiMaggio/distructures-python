import distructures


def main():
    queue = distructures.cyclicQueue(10)

    for i in range(100):
        queue.push(i)

    while not queue.empty():
        print(queue.pop())


if "__main__" == __name__:
    main()
