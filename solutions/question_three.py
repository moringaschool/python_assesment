def sequence():
    items = []
    num = [x for x in raw_input().split(',')]
    for p in num:
        x = int(p, 2)
        if not x%5:
            items.append(p)
    print(','.join(items))
