def dec2oct(x):
    if x == 0:
        return "0"
    result = ""
    while x !=0:
        x, reminder = divmod(x, 8)
        result = str(reminder) + result
    return result

def oct2dec(x):
    result = 0
    for i, digit in enumerate(x):
        result += int(digit) * 8 ** (len(x) - 1 - i)
    return result

def oct2dec2(x):
    return sum([
        int (val) * 8** pos for pos, val in enumerate(reversed(x)) if bit != "0"
    ])


if __name__ == "__main__":
    x = 42
    result = dec2oct(x)
    print(x, result, int(result, base=8), oct2dec(result))

    #print(bin2dec("10"))