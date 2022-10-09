def dec2hex(x):
    if x == 0:
        return "0"
    result = ""

    dictn = {
        1: "1", 2: "2", 3: "3", 4: "4",
        5: "5", 6: "6", 7: "7", 8: "8",
        9: "9",10: "A",11: "B",12: "C",
        13: "D",14: "E",15: "F",
    }
    while x !=0:
        x, reminder = divmod(x, 16)
        result = str(dictn[reminder]) + result
    return result

def hex2dec(x):
    dictn = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    result = 0
    for i, digit in enumerate(x):
        result += int(dictn.get(digit,digit)) * 16 ** (len(x) - 1 - i)
    return result


if __name__ == "__main__":
    print(hex2dec("ABC"))
    print(dec2hex(2748))