def fi(n):
    i = 3
    result = []
    result[0]=1
    if n ==1:
        return 1
    elif n==2:
        return 2
    else:
        while i<n:
            result[i] = result[i-1] + result[i-2]
            i +=1
        return result[n-1]


if __name__ == "__main__":
    print(fi(n))
