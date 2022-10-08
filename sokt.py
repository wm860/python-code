def dec2oct(x):
    if x == 0:
        return "0"
    result = ""
    while x !=0:
        x, bit = divmod(x, 8)
    #    result.append(bit)
    #    bit=x%2
    #    result.append(bit)
    #    x = x // 2
        result = str(bit) + result
    return result

def oct2dec(x):
    liczba = 0
    #x = list(x)
    for i in range(len(x)):
        liczba += int(x[i]) * 8**(len(x)-1-i)
    return liczba


if __name__ == "__main__":
    print(dec2oct(235))
    print(oct2dec("353"))