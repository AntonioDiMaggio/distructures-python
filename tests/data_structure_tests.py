import distructures


def main():
    linkedList = distructures.linkedList()
    print(linkedList)

    for i in range(10):
        linkedList.append(i)
        print(linkedList)
        print(len(linkedList))

    linkedList.remove(0)
    print(linkedList)
    print(len(linkedList))

    linkedList.append(10)
    print(linkedList)
    print(len(linkedList))

    linkedList.remove(5)
    print(linkedList)
    print(len(linkedList))

    linkedList.append(11)
    print(linkedList)
    print(len(linkedList))

    linkedList.remove(11)
    print(linkedList)
    print(len(linkedList))

    linkedList.append(11)
    print(linkedList)
    print(len(linkedList))


if "__main__" == __name__:
    main()
