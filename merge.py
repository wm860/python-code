def merge(l1, l2):
    i, j = 0, 0
    result = []

    while i < len(l1) and j< len(l2):
        if l1[i]<=l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i,:])
    result.extend(l2[j,:])
    return result
if __name__ == "__main__":