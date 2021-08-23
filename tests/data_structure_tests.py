import distructures


def main():
    queue = distructures.cyclicQueue(10)
    for i in range(100):
        queue.push(i)
        print(queue)
        print(queue.front(), queue.rear())


if "__main__" == __name__:
    main()
