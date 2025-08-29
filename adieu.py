import inflect

p = inflect.engine()
base = "Adieu, adieu, to "
l = []

while True:
    try:
        inp = input("Name: ")
        l.append(inp)

    except EOFError:
        print()
        print(base + p.join(l))
        exit()
