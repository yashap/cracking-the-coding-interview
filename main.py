from ch02.linked_list import LinkedList

def main():
    ll = LinkedList(10, 11, 12, 13)
    print(str(ll))
    print(len(ll))
    ll = ll.prepend(9)
    ll = ll.append(14)
    print(str(ll))
    print(len(ll))
    print(str(ll.tail()))

if __name__ == "__main__":
    main()
