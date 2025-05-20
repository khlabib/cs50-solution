import pytest
def main():
    while True:
        frac = input("Fraction: ")
        try:
            result = convert(frac)
            final = gauge(result)
        except (ZeroDivisionError, ValueError, TypeError):
            continue
        else:
            print(final)
            break


def convert(fraction):
    fraction = fraction.split("/")
    if not fraction[0].isdigit() or not fraction[1].isdigit():
        raise ValueError

    fraction[0] = int(fraction[0])
    fraction[1] = int(fraction[1])

    if fraction[1] == 0:
        raise ZeroDivisionError

    if fraction[0] >fraction[1]:
        raise ValueError

    return round(float(fraction[0]) / float(fraction[1]) * 100)


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()