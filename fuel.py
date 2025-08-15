
def main():
    while True:

        try:
            car = input(f"Fraction: ")

            x, y = car.split("/")

            fuel = int(x) / int(y)

            if fuel <= 1:

                tank(fuel)
                break

        except (ValueError, ZeroDivisionError, IndexError):
            pass

def tank(fuel):
    # here's where we need to round the results for it to give us 67% instead of 66,6% when dividing 2 by 3

    tank = round(fuel * 100)

    if tank <= 1:
        print("E")

    elif tank >= 99:
        print("F")

    else:
        print(f"{tank}%")


main()
