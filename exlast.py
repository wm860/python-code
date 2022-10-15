def is_lucky(serial):
    first_part = [int(x) for x in serial[:3]]
    second_part = [int(x) for x in serial[3:]]
    return sum(first_part) == sum(second_part)

def create_lucky_tickets1(n):
    result = []
    i = 0
    for i in range(10 **6):
        serial = str(i).zfill(6)
        if is_lucky(serial):
            result.append(serial)
        if len(result) >=n:
            break
    return result

def create_lucky_tickets2(n):
    result = []
    i = 0
    while len(result) < n:
        serial = str(i).zfill(6)
        if is_lucky(serial):
            result.append(serial)
        i += 1
    return result

def calculate_total_lucky_tickets():
    result = []
    total = 0
    i = 0
    for i in range(10 ** 6):
        serial = str(i).zfill(6)
        if is_lucky(serial):
            #result.append(serial)
            total += 1
    return result

if __name__ == "__main__":
   pass

