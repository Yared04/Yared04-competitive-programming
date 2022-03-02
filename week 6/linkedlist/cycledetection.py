def has_cycle(head):
    lis = []
    while head:
        for node in lis:
            if node == head:
                return 1
            else:
                continue
        lis.append(head)
        head = head.next
    return 0