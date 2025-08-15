groceries = {}

while True:

    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1

        else:
            groceries[item] = 1

    except EOFError:
        for key, value in sorted(groceries.items()):
            print(value, key)

        break
