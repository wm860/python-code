from sbin import bin2dec


def zfill(value, width):
    n = width - len(value)
    return n * "0" + value

if __name__ == "__main__":
    print(zfill("1", 6))
    print(bin2dec("1001"))